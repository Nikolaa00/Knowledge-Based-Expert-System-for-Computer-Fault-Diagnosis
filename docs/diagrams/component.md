# Компонентен дијаграм

`composition.py` ги создава `YamlKnowledgeRepository`, `ForwardChainingEngine` и `DiagnoseComputer`. Екранот не го познава engine ниту репозиториумот. Ги повикува само `catalog` и `diagnose`.

```mermaid
flowchart LR
  app[app.py]
  ui[streamlit_app]
  composition[composition]
  useCase[DiagnoseComputer]
  engine[ForwardChainingEngine]
  repository[YamlKnowledgeRepository]
  file[computer_faults.yaml]

  app -->|"main()"| ui
  composition -->|"build_diagnose_computer()"| ui
  ui -->|"catalog() -> KnowledgeBase"| useCase
  ui -->|"diagnose(selected_symptom_ids) -> DiagnosisResult"| useCase
  useCase -->|"catalog() -> KnowledgeBase"| engine
  useCase -->|"infer(evidence: Evidence) -> DiagnosisResult"| engine
  engine -->|"load() -> KnowledgeBase"| repository
  repository -->|"read"| file
```
