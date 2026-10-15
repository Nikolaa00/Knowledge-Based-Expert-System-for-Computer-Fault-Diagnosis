from typing import Protocol

from pc_fault_diagnosis.domain.models import DiagnosisResult, Evidence, KnowledgeBase
from pc_fault_diagnosis.knowledge.repository import KnowledgeRepository


class InferenceEngine(Protocol):
    def catalog(self) -> KnowledgeBase: ...

    def infer(self, evidence: Evidence) -> DiagnosisResult: ...


class ForwardChainingEngine:
    def __init__(self, repository: KnowledgeRepository) -> None:
        self._repository = repository

    def catalog(self) -> KnowledgeBase:
        return self._repository.load()

    def infer(self, evidence: Evidence) -> DiagnosisResult:
        raise NotImplementedError
