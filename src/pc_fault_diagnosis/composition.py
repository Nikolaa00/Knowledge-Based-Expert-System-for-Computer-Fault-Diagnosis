from pathlib import Path

from pc_fault_diagnosis.application.diagnose import DiagnoseComputer
from pc_fault_diagnosis.inference.engine import ForwardChainingEngine
from pc_fault_diagnosis.knowledge.repository import YamlKnowledgeRepository


# Resolves the path to the bundled computer_faults.yaml knowledge file.
def default_knowledge_path() -> Path:
    candidates = (
        Path(__file__).resolve().parents[2] / "knowledge" / "computer_faults.yaml",
        Path.cwd() / "knowledge" / "computer_faults.yaml",
    )
    for path in candidates:
        if path.is_file():
            return path
    return candidates[0]


# Wires the YAML repository, forward-chaining engine, and DiagnoseComputer for the app.
def build_diagnose_computer(knowledge_path: Path | None = None) -> DiagnoseComputer:
    repository = YamlKnowledgeRepository(knowledge_path or default_knowledge_path())
    engine = ForwardChainingEngine(repository)
    return DiagnoseComputer(engine)
