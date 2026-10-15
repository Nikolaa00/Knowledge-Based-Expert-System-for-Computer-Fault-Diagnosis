class KnowledgeBaseError(Exception):
    """Raised when the knowledge file does not match the expected shape."""


class UnknownSymptomError(Exception):
    def __init__(self, symptom_id: str) -> None:
        self.symptom_id = symptom_id
        super().__init__(symptom_id)
