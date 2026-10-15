from pathlib import Path

import pytest

from pc_fault_diagnosis.domain.errors import KnowledgeBaseError
from pc_fault_diagnosis.domain.models import ConclusionKind
from pc_fault_diagnosis.knowledge.repository import YamlKnowledgeRepository

ROOT = Path(__file__).resolve().parents[1]


def test_real_catalog_has_the_expected_counts() -> None:
    knowledge = YamlKnowledgeRepository(ROOT / "knowledge" / "computer_faults.yaml").load()

    assert len(knowledge.subsystems) == 8
    assert len(knowledge.symptoms) == 34
    assert len(knowledge.faults) == 16
    assert len(knowledge.facts) == 2
    assert len(knowledge.rules) == 25
    rule = next(item for item in knowledge.rules if item.id == "rule_faulty_psu")
    assert rule.conclusion_kind is ConclusionKind.FAULT
    assert rule.conclusion_id == "faulty_psu"
    assert "power_path_dead" in rule.when_present


def test_duplicate_symptom_id_is_rejected(tmp_path: Path) -> None:
    path = _write(
        tmp_path,
        """
subsystems:
  - {id: power, label_mk: Напојување}
symptoms:
  - {id: a, subsystem: power, label_mk: А, description_mk: А}
  - {id: a, subsystem: power, label_mk: Б, description_mk: Б}
faults: []
facts: []
rules: []
""",
    )
    with pytest.raises(KnowledgeBaseError, match="Duplicate symptom id: a"):
        YamlKnowledgeRepository(path).load()


def test_unknown_condition_is_rejected(tmp_path: Path) -> None:
    path = _write(
        tmp_path,
        """
subsystems:
  - {id: power, label_mk: Напојување}
symptoms:
  - {id: a, subsystem: power, label_mk: А, description_mk: А}
faults:
  - {id: f, name_mk: Дефект, summary_mk: Опис}
facts: []
rules:
  - id: rule_missing
    when_present: [missing]
    when_absent: []
    conclude: {kind: fault, id: f}
    explanation_mk: Објаснување
    recommendations_mk: []
""",
    )
    with pytest.raises(KnowledgeBaseError, match="unknown condition 'missing'"):
        YamlKnowledgeRepository(path).load()


def test_rule_cannot_require_its_own_fact(tmp_path: Path) -> None:
    path = _write(
        tmp_path,
        """
subsystems: []
symptoms: []
faults: []
facts:
  - {id: loop, label_mk: Јамка}
rules:
  - id: rule_loop
    when_present: [loop]
    when_absent: []
    conclude: {kind: fact, id: loop}
    explanation_mk: Се повикува самото себе
    recommendations_mk: []
""",
    )
    with pytest.raises(KnowledgeBaseError, match="own conclusion 'loop'"):
        YamlKnowledgeRepository(path).load()


def _write(directory: Path, document: str) -> Path:
    path = directory / "knowledge.yaml"
    path.write_text(document.strip() + "\n", encoding="utf-8")
    return path
