from pathlib import Path

import pytest

from pc_fault_diagnosis.domain.errors import UnknownSymptomError
from pc_fault_diagnosis.domain.models import (
    ConclusionKind,
    DiagnosisStatus,
    Evidence,
    Fact,
    Fault,
    KnowledgeBase,
    Rule,
    Subsystem,
    Symptom,
)
from pc_fault_diagnosis.inference.engine import ForwardChainingEngine
from pc_fault_diagnosis.knowledge.repository import YamlKnowledgeRepository

ROOT = Path(__file__).resolve().parents[1]


class MemoryRepository:
    def __init__(self, knowledge: KnowledgeBase) -> None:
        self.knowledge = knowledge

    def load(self) -> KnowledgeBase:
        return self.knowledge


def test_power_chain_is_confirmed() -> None:
    diagnosis = _only("no_power_led", "no_fans", "psu_clicks")

    assert diagnosis.fault.id == "faulty_psu"
    assert diagnosis.status is DiagnosisStatus.CONFIRMED
    assert diagnosis.score == pytest.approx(1)
    assert [match.rule_id for match in diagnosis.matches] == [
        "rule_power_path_dead",
        "rule_faulty_psu",
    ]


def test_contradicted_overheating_stays_partial() -> None:
    diagnosis = _only("thermal_shutdown", "loud_fans_hot", "no_fans")

    assert diagnosis.fault.id == "overheating"
    assert diagnosis.status is DiagnosisStatus.PARTIAL
    assert diagnosis.score == pytest.approx(2 / 3)


def test_one_disk_symptom_returns_two_partials() -> None:
    diagnoses = _infer("slow_boot_disk").diagnoses

    assert [item.fault.id for item in diagnoses] == ["corrupted_filesystem", "failing_disk"]
    assert diagnoses[0].score == pytest.approx(2 / 3)
    assert diagnoses[1].score == pytest.approx(0.5)
    assert all(item.status is DiagnosisStatus.PARTIAL for item in diagnoses)
    assert [match.rule_id for match in diagnoses[1].matches] == [
        "rule_failing_disk",
        "rule_smart_disk",
    ]


def test_two_confirmed_faults_are_ordered_by_id() -> None:
    diagnoses = _infer(
        "clicking_disk",
        "slow_boot_disk",
        "smart_warning",
        "high_cpu_idle",
    ).diagnoses

    assert [item.fault.id for item in diagnoses] == ["background_cpu_load", "failing_disk"]
    assert all(item.status is DiagnosisStatus.CONFIRMED for item in diagnoses)
    assert [match.rule_id for match in diagnoses[1].matches] == [
        "rule_failing_disk",
        "rule_smart_disk",
    ]


def test_empty_evidence_returns_no_diagnoses() -> None:
    assert _infer().diagnoses == ()


def test_unknown_symptom_is_rejected() -> None:
    with pytest.raises(UnknownSymptomError) as caught:
        _infer("not_a_symptom")
    assert caught.value.symptom_id == "not_a_symptom"


def test_engine_chains_a_fact_from_the_repository() -> None:
    symptom_a = Symptom("power_off", "power", "Нема струја", "Нема светло")
    symptom_b = Symptom("click", "power", "Клик", "Се слуша клик")
    knowledge = KnowledgeBase(
        subsystems=(Subsystem("power", "Напојување"),),
        symptoms=(symptom_a, symptom_b),
        faults=(Fault("psu", "Напојување", "Напојувањето не држи"),),
        facts=(Fact("dead", "Плочата не добива струја"),),
        rules=(
            Rule(
                "rule_fact",
                ("power_off",),
                (),
                ConclusionKind.FACT,
                "dead",
                "Нема патека на струја.",
                (),
            ),
            Rule(
                "rule_fault",
                ("dead", "click"),
                (),
                ConclusionKind.FAULT,
                "psu",
                "Напојувањето кликнува.",
                ("Замени го напојувањето.",),
            ),
        ),
    )
    result = ForwardChainingEngine(MemoryRepository(knowledge)).infer(
        Evidence(frozenset({"power_off", "click"}))
    )

    diagnosis = result.diagnoses[0]
    assert diagnosis.fault.id == "psu"
    assert diagnosis.status is DiagnosisStatus.CONFIRMED
    assert [match.rule_id for match in diagnosis.matches] == ["rule_fact", "rule_fault"]


def _infer(*symptom_ids: str):
    repository = YamlKnowledgeRepository(ROOT / "knowledge" / "computer_faults.yaml")
    return ForwardChainingEngine(repository).infer(Evidence(frozenset(symptom_ids)))


def _only(*symptom_ids: str):
    diagnoses = _infer(*symptom_ids).diagnoses
    assert len(diagnoses) == 1
    return diagnoses[0]
