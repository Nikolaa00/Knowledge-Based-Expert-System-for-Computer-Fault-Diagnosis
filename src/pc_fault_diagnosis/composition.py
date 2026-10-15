from pathlib import Path

from pc_fault_diagnosis.application.diagnose import DiagnoseComputer
from pc_fault_diagnosis.inference.engine import ForwardChainingEngine
from pc_fault_diagnosis.knowledge.repository import YamlKnowledgeRepository


def default_knowledge_path() -> Path:
    return Path(__file__).resolve().parents[2] / "knowledge" / "computer_faults.yaml"


def build_diagnose_computer(knowledge_path: Path | None = None) -> DiagnoseComputer:
    repository = YamlKnowledgeRepository(knowledge_path or default_knowledge_path())
    engine = ForwardChainingEngine(repository)
    return DiagnoseComputer(engine)
