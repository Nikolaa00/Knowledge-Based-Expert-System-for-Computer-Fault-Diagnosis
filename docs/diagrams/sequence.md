# Секвенциски дијаграми

## Успешна дијагноза со синџир

Корисникот избира `no_power_led`, `no_fans` и `psu_clicks`. Машината го активира `rule_power_path_dead`, го додава фактот `power_path_dead`, па го активира `rule_faulty_psu`. Резултатот е потврдена дијагноза „Неисправно напојување“.

```mermaid
sequenceDiagram
  actor User as Корисник
  participant UI as streamlit_app
  participant UseCase as DiagnoseComputer
  participant Engine as ForwardChainingEngine
  participant Repository as YamlKnowledgeRepository

  UI->>UseCase: catalog()
  UseCase->>Engine: catalog()
  Engine->>Repository: load()
  Repository-->>Engine: KnowledgeBase
  Engine-->>UseCase: KnowledgeBase
  UseCase-->>UI: KnowledgeBase
  User->>UI: no_power_led, no_fans, psu_clicks
  User->>UI: Дијагностицирај
  UI->>UseCase: diagnose(selected_symptom_ids)
  UseCase->>Engine: infer(evidence)
  Engine->>Repository: load()
  Repository-->>Engine: KnowledgeBase
  Engine->>Engine: rule_power_path_dead
  Engine->>Engine: rule_faulty_psu
  Engine-->>UseCase: DiagnosisResult
  UseCase-->>UI: DiagnosisResult
  UI-->>User: Неисправно напојување
```

## Празен избор

Корисникот притиска „Дијагностицирај“ без симптом. Предупредувањето останува на екранот. `DiagnoseComputer` не се повикува.

```mermaid
sequenceDiagram
  actor User as Корисник
  participant UI as streamlit_app

  User->>UI: Дијагностицирај
  UI-->>User: Избери барем еден симптом.
```
