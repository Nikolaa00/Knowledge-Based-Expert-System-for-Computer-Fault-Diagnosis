from dataclasses import dataclass
from enum import Enum


class ItemKind(Enum):
    SYMPTOM = "symptom"
    FACT = "fact"


class ConclusionKind(Enum):
    FACT = "fact"
    FAULT = "fault"


class DiagnosisStatus(Enum):
    CONFIRMED = "confirmed"
    PARTIAL = "partial"


@dataclass(frozen=True)
class Subsystem:
    id: str
    label_mk: str


@dataclass(frozen=True)
class Symptom:
    id: str
    subsystem_id: str
    label_mk: str
    description_mk: str


@dataclass(frozen=True)
class Fault:
    id: str
    name_mk: str
    summary_mk: str


@dataclass(frozen=True)
class Fact:
    id: str
    label_mk: str


@dataclass(frozen=True)
class Rule:
    id: str
    when_present: tuple[str, ...]
    when_absent: tuple[str, ...]
    conclusion_kind: ConclusionKind
    conclusion_id: str
    explanation_mk: str
    recommendations_mk: tuple[str, ...]


@dataclass(frozen=True)
class KnowledgeBase:
    subsystems: tuple[Subsystem, ...]
    symptoms: tuple[Symptom, ...]
    faults: tuple[Fault, ...]
    facts: tuple[Fact, ...]
    rules: tuple[Rule, ...]


@dataclass(frozen=True)
class Evidence:
    present_symptom_ids: frozenset[str]


@dataclass(frozen=True)
class KnowledgeItem:
    id: str
    label_mk: str
    kind: ItemKind


@dataclass(frozen=True)
class RuleMatch:
    rule_id: str
    explanation_mk: str
    recommendations_mk: tuple[str, ...]
    matched: tuple[KnowledgeItem, ...]
    missing: tuple[KnowledgeItem, ...]
    contradicted: tuple[KnowledgeItem, ...]
    score: float


@dataclass(frozen=True)
class Diagnosis:
    fault: Fault
    score: float
    status: DiagnosisStatus
    matches: tuple[RuleMatch, ...]


@dataclass(frozen=True)
class DiagnosisResult:
    diagnoses: tuple[Diagnosis, ...]
