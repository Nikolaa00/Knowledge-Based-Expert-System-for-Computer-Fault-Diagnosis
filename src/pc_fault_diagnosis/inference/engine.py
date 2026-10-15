from typing import Protocol

from pc_fault_diagnosis.domain.errors import UnknownSymptomError
from pc_fault_diagnosis.domain.models import (
    ConclusionKind,
    Diagnosis,
    DiagnosisResult,
    DiagnosisStatus,
    Evidence,
    ItemKind,
    KnowledgeBase,
    KnowledgeItem,
    Rule,
    RuleMatch,
)
from pc_fault_diagnosis.knowledge.repository import KnowledgeRepository

PARTIAL_SCORE_THRESHOLD = 0.5


class InferenceEngine(Protocol):
    def catalog(self) -> KnowledgeBase:
        """Return subsystems, symptoms, faults, facts, and rules."""
        ...

    def infer(self, evidence: Evidence) -> DiagnosisResult:
        """Rank faults for the selected symptoms and explain the rules."""
        ...


class ForwardChainingEngine:
    """Forward-chaining diagnosis over production rules.

    A condition in ``when_present`` is satisfied when its id is in working
    memory. A condition in ``when_absent`` is satisfied when its id is not.
    ``score`` is satisfied conditions divided by all conditions. A fact is
    added to memory only when the rule that concludes it scores 1. A fault is
    returned when one of its rules scores at least 0.5 and at least one
    required id is in memory. The diagnosis score is the highest fault-rule
    score. Fact rules appear in the trace only to explain that score.
    """

    def __init__(self, repository: KnowledgeRepository) -> None:
        self._repository = repository

    def catalog(self) -> KnowledgeBase:
        return self._load()

    def infer(self, evidence: Evidence) -> DiagnosisResult:
        knowledge = self._load()
        if not evidence.present_symptom_ids:
            return DiagnosisResult(diagnoses=())
        known_symptoms = {symptom.id for symptom in knowledge.symptoms}
        for symptom_id in evidence.present_symptom_ids:
            if symptom_id not in known_symptoms:
                raise UnknownSymptomError(symptom_id)

        memory = set(evidence.present_symptom_ids)
        fired_order = self._fire_complete_rules(knowledge, memory)
        return self._rank(knowledge, memory, fired_order)

    def _load(self) -> KnowledgeBase:
        return self._repository.load()

    def _fire_complete_rules(self, knowledge: KnowledgeBase, memory: set[str]) -> list[str]:
        fired: set[str] = set()
        fired_order: list[str] = []
        for _ in knowledge.rules:
            progressed = False
            for rule in knowledge.rules:
                if rule.id in fired or self._score(rule, memory) != 1.0:
                    continue
                fired.add(rule.id)
                fired_order.append(rule.id)
                if rule.conclusion_kind is ConclusionKind.FACT:
                    memory.add(rule.conclusion_id)
                progressed = True
                break
            if not progressed:
                break
        return fired_order

    def _rank(
        self,
        knowledge: KnowledgeBase,
        memory: set[str],
        fired_order: list[str],
    ) -> DiagnosisResult:
        index = self._items(knowledge)
        rules_by_id = {rule.id: rule for rule in knowledge.rules}
        fact_ids = {fact.id for fact in knowledge.facts}
        faults_by_id = {fault.id: fault for fault in knowledge.faults}
        grouped: dict[str, list[tuple[Rule, RuleMatch]]] = {}
        for rule in knowledge.rules:
            if rule.conclusion_kind is not ConclusionKind.FAULT:
                continue
            score = self._score(rule, memory)
            if score < PARTIAL_SCORE_THRESHOLD:
                continue
            if not any(item in memory for item in rule.when_present):
                continue
            grouped.setdefault(rule.conclusion_id, []).append((rule, self._match(rule, memory, index, score)))

        diagnoses = []
        for fault_id, pairs in grouped.items():
            used_facts = {
                item
                for rule, _match in pairs
                for item in rule.when_present
                if item in fact_ids
            }
            fact_matches = tuple(
                self._match(rules_by_id[rule_id], memory, index, 1.0)
                for rule_id in fired_order
                if rules_by_id[rule_id].conclusion_kind is ConclusionKind.FACT
                and rules_by_id[rule_id].conclusion_id in used_facts
            )
            fault_matches = tuple(
                sorted(
                    (match for _rule, match in pairs),
                    key=lambda match: (-match.score, match.rule_id),
                )
            )
            score = max(match.score for match in fault_matches)
            status = DiagnosisStatus.CONFIRMED if score == 1.0 else DiagnosisStatus.PARTIAL
            diagnoses.append(
                Diagnosis(
                    fault=faults_by_id[fault_id],
                    score=score,
                    status=status,
                    matches=fact_matches + fault_matches,
                )
            )
        diagnoses.sort(key=lambda diagnosis: (-diagnosis.score, diagnosis.fault.id))
        return DiagnosisResult(diagnoses=tuple(diagnoses))

    def _score(self, rule: Rule, memory: set[str]) -> float:
        total = len(rule.when_present) + len(rule.when_absent)
        satisfied = sum(item in memory for item in rule.when_present)
        satisfied += sum(item not in memory for item in rule.when_absent)
        return satisfied / total

    def _match(self, rule: Rule, memory: set[str], index: dict[str, KnowledgeItem], score: float) -> RuleMatch:
        return RuleMatch(
            rule_id=rule.id,
            explanation_mk=rule.explanation_mk,
            recommendations_mk=rule.recommendations_mk,
            matched=tuple(index[item] for item in rule.when_present if item in memory),
            missing=tuple(index[item] for item in rule.when_present if item not in memory),
            contradicted=tuple(index[item] for item in rule.when_absent if item in memory),
            score=score,
        )

    def _items(self, knowledge: KnowledgeBase) -> dict[str, KnowledgeItem]:
        items = {
            symptom.id: KnowledgeItem(symptom.id, symptom.label_mk, ItemKind.SYMPTOM)
            for symptom in knowledge.symptoms
        }
        items.update(
            {fact.id: KnowledgeItem(fact.id, fact.label_mk, ItemKind.FACT) for fact in knowledge.facts}
        )
        return items
