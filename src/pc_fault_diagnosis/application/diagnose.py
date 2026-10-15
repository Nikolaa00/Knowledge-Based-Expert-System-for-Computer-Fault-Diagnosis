from collections.abc import Sequence

from pc_fault_diagnosis.domain.models import DiagnosisResult, Evidence, KnowledgeBase
from pc_fault_diagnosis.inference.engine import InferenceEngine


class DiagnoseComputer:
    def __init__(self, engine: InferenceEngine) -> None:
        self._engine = engine

    def catalog(self) -> KnowledgeBase:
        return self._engine.catalog()

    def diagnose(self, selected_symptom_ids: Sequence[str]) -> DiagnosisResult:
        return self._engine.infer(Evidence(frozenset(selected_symptom_ids)))
