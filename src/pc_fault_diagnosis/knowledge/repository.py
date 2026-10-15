from pathlib import Path
from typing import Protocol

import yaml

from pc_fault_diagnosis.domain.errors import KnowledgeBaseError
from pc_fault_diagnosis.domain.models import (
    ConclusionKind,
    Fact,
    Fault,
    KnowledgeBase,
    Rule,
    Subsystem,
    Symptom,
)

_KEYS = ("subsystems", "symptoms", "faults", "facts", "rules")


class KnowledgeRepository(Protocol):
    def load(self) -> KnowledgeBase:
        """Return the current knowledge base."""
        ...


class YamlKnowledgeRepository:
    """Load production rules from a YAML file on every call to ``load``."""

    def __init__(self, path: Path) -> None:
        self._path = path

    def load(self) -> KnowledgeBase:
        document = self._read_document()
        self._require_keys(document)
        subsystems = self._subsystems(document["subsystems"])
        symptoms = self._symptoms(document["symptoms"], subsystems)
        faults = self._faults(document["faults"])
        facts = self._facts(document["facts"], symptoms)
        rules = self._rules(document["rules"], symptoms, faults, facts)
        return KnowledgeBase(subsystems, symptoms, faults, facts, rules)

    def _read_document(self) -> dict:
        if not self._path.is_file():
            raise KnowledgeBaseError(f"Knowledge file not found: {self._path}")
        try:
            loaded = yaml.safe_load(self._path.read_text(encoding="utf-8"))
        except yaml.YAMLError as error:
            raise KnowledgeBaseError(f"Knowledge file is not valid YAML: {error}") from error
        if loaded is None:
            loaded = {}
        if not isinstance(loaded, dict):
            raise KnowledgeBaseError("Knowledge file must be a mapping")
        return loaded

    def _require_keys(self, document: dict) -> None:
        missing = [key for key in _KEYS if key not in document]
        if missing:
            raise KnowledgeBaseError(f"Knowledge file is missing keys: {', '.join(missing)}")

    def _subsystems(self, raw: object) -> tuple[Subsystem, ...]:
        items = self._as_list(raw, "subsystems")
        subsystems = tuple(
            Subsystem(id=self._text(item, "id", "subsystem"), label_mk=self._text(item, "label_mk", "subsystem"))
            for item in items
        )
        self._unique((item.id for item in subsystems), "subsystem")
        return subsystems

    def _symptoms(self, raw: object, subsystems: tuple[Subsystem, ...]) -> tuple[Symptom, ...]:
        known_subsystems = {item.id for item in subsystems}
        symptoms = []
        for item in self._as_list(raw, "symptoms"):
            subsystem_id = self._text(item, "subsystem", "symptom")
            symptom_id = self._text(item, "id", "symptom")
            if subsystem_id not in known_subsystems:
                raise KnowledgeBaseError(f"Symptom '{symptom_id}' points at unknown subsystem '{subsystem_id}'")
            symptoms.append(
                Symptom(
                    id=symptom_id,
                    subsystem_id=subsystem_id,
                    label_mk=self._text(item, "label_mk", "symptom"),
                    description_mk=self._text(item, "description_mk", "symptom"),
                )
            )
        self._unique((item.id for item in symptoms), "symptom")
        return tuple(symptoms)

    def _faults(self, raw: object) -> tuple[Fault, ...]:
        faults = tuple(
            Fault(
                id=self._text(item, "id", "fault"),
                name_mk=self._text(item, "name_mk", "fault"),
                summary_mk=self._text(item, "summary_mk", "fault"),
            )
            for item in self._as_list(raw, "faults")
        )
        self._unique((item.id for item in faults), "fault")
        return faults

    def _facts(self, raw: object, symptoms: tuple[Symptom, ...]) -> tuple[Fact, ...]:
        symptom_ids = {item.id for item in symptoms}
        facts = []
        for item in self._as_list(raw, "facts"):
            fact_id = self._text(item, "id", "fact")
            if fact_id in symptom_ids:
                raise KnowledgeBaseError(f"Fact '{fact_id}' uses a symptom id")
            facts.append(Fact(id=fact_id, label_mk=self._text(item, "label_mk", "fact")))
        self._unique((item.id for item in facts), "fact")
        return tuple(facts)

    def _rules(
        self,
        raw: object,
        symptoms: tuple[Symptom, ...],
        faults: tuple[Fault, ...],
        facts: tuple[Fact, ...],
    ) -> tuple[Rule, ...]:
        known_conditions = {item.id for item in symptoms} | {item.id for item in facts}
        fault_ids = {item.id for item in faults}
        fact_ids = {item.id for item in facts}
        rules = []
        for item in self._as_list(raw, "rules"):
            rule_id = self._text(item, "id", "rule")
            when_present = self._identifiers(item, "when_present", rule_id)
            when_absent = self._identifiers(item, "when_absent", rule_id)
            if not when_present:
                raise KnowledgeBaseError(f"Rule '{rule_id}' has no when_present conditions")
            conclusion_kind, conclusion_id = self._conclusion(item, rule_id)
            if conclusion_id in when_present:
                raise KnowledgeBaseError(f"Rule '{rule_id}' lists its own conclusion '{conclusion_id}'")
            for condition in when_present + when_absent:
                if condition not in known_conditions:
                    raise KnowledgeBaseError(f"Rule '{rule_id}' uses unknown condition '{condition}'")
            if conclusion_kind is ConclusionKind.FACT and conclusion_id not in fact_ids:
                raise KnowledgeBaseError(f"Rule '{rule_id}' concludes unknown fact '{conclusion_id}'")
            if conclusion_kind is ConclusionKind.FAULT and conclusion_id not in fault_ids:
                raise KnowledgeBaseError(f"Rule '{rule_id}' concludes unknown fault '{conclusion_id}'")
            rules.append(
                Rule(
                    id=rule_id,
                    when_present=when_present,
                    when_absent=when_absent,
                    conclusion_kind=conclusion_kind,
                    conclusion_id=conclusion_id,
                    explanation_mk=self._text(item, "explanation_mk", "rule"),
                    recommendations_mk=self._recommendations(item, rule_id),
                )
            )
        self._unique((item.id for item in rules), "rule")
        return tuple(rules)

    def _conclusion(self, item: dict, rule_id: str) -> tuple[ConclusionKind, str]:
        conclude = item.get("conclude")
        if not isinstance(conclude, dict):
            raise KnowledgeBaseError(f"Rule '{rule_id}' is missing conclude")
        kind = conclude.get("kind")
        conclusion_id = conclude.get("id")
        if kind == "fact":
            conclusion_kind = ConclusionKind.FACT
        elif kind == "fault":
            conclusion_kind = ConclusionKind.FAULT
        else:
            raise KnowledgeBaseError(f"Rule '{rule_id}' has unknown conclusion kind '{kind}'")
        if not isinstance(conclusion_id, str) or not conclusion_id:
            raise KnowledgeBaseError(f"Rule '{rule_id}' has an empty conclusion id")
        return conclusion_kind, conclusion_id

    def _recommendations(self, item: dict, rule_id: str) -> tuple[str, ...]:
        raw = item.get("recommendations_mk")
        if not isinstance(raw, list):
            raise KnowledgeBaseError(f"Rule '{rule_id}' is missing recommendations_mk")
        recommendations = []
        for entry in raw:
            if not isinstance(entry, str) or not entry:
                raise KnowledgeBaseError(f"Rule '{rule_id}' has an empty recommendation")
            recommendations.append(entry)
        return tuple(recommendations)

    def _identifiers(self, item: dict, key: str, rule_id: str) -> tuple[str, ...]:
        raw = item.get(key)
        if not isinstance(raw, list):
            raise KnowledgeBaseError(f"Rule '{rule_id}' is missing {key}")
        identifiers = []
        for entry in raw:
            if not isinstance(entry, str) or not entry:
                raise KnowledgeBaseError(f"Rule '{rule_id}' has an empty {key} id")
            identifiers.append(entry)
        return tuple(identifiers)

    def _as_list(self, raw: object, name: str) -> list[dict]:
        if not isinstance(raw, list):
            raise KnowledgeBaseError(f"'{name}' must be a list")
        items = []
        for entry in raw:
            if not isinstance(entry, dict):
                raise KnowledgeBaseError(f"Each {name} entry must be a mapping")
            items.append(entry)
        return items

    def _text(self, item: dict, key: str, kind: str) -> str:
        value = item.get(key)
        if not isinstance(value, str) or not value:
            identifier = item.get("id", "?")
            raise KnowledgeBaseError(f"{kind} '{identifier}' is missing {key}")
        return value

    def _unique(self, identifiers, kind: str) -> None:
        seen: set[str] = set()
        for identifier in identifiers:
            if identifier in seen:
                raise KnowledgeBaseError(f"Duplicate {kind} id: {identifier}")
            seen.add(identifier)
