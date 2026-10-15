import pytest

from pc_fault_diagnosis.application.diagnose import DiagnoseComputer
from pc_fault_diagnosis.domain.errors import UnknownSymptomError
from pc_fault_diagnosis.domain.models import DiagnosisResult, Evidence


class RecordingEngine:
    def __init__(self, error: Exception | None = None) -> None:
        self.calls: list[Evidence] = []
        self.error = error

    def catalog(self):
        raise AssertionError("catalog is not used by diagnose")

    def infer(self, evidence: Evidence) -> DiagnosisResult:
        self.calls.append(evidence)
        if self.error is not None:
            raise self.error
        return DiagnosisResult(diagnoses=())


def test_empty_selection_does_not_call_the_engine() -> None:
    engine = RecordingEngine()
    computer = DiagnoseComputer(engine)

    assert computer.diagnose(()).diagnoses == ()
    assert computer.diagnose([]).diagnoses == ()
    assert engine.calls == []


def test_selection_is_passed_as_evidence() -> None:
    engine = RecordingEngine()
    computer = DiagnoseComputer(engine)

    computer.diagnose(["b", "a"])

    assert engine.calls[0].present_symptom_ids == frozenset({"a", "b"})


def test_unknown_symptom_is_not_swallowed() -> None:
    engine = RecordingEngine(UnknownSymptomError("nope"))
    computer = DiagnoseComputer(engine)

    with pytest.raises(UnknownSymptomError) as caught:
        computer.diagnose(["nope"])

    assert caught.value.symptom_id == "nope"
