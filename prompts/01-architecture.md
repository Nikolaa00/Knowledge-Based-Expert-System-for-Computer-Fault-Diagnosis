# Фаза 01 — Архитектура

Копирај го целиот овој фајл во нов агентски разговор. Запри на скелетот. Не ја полни базата со дефекти и не пишувај алгоритам за заклучување.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом. Python 3.11, Streamlit, знаење во YAML.

Фазата 00 веќе ги има ставено `.cursor/rules/architecture.mdc`, `.cursor/rules/course-deliverables.mdc` и `.cursor/skills/pc-fault-diagnosis/SKILL.md`. Прочитај ги пред првата измена и држи се до нив. Ако некој детаљ од овој промпт го прецизира правилото, овој промпт е изворот за имињата на типовите.

## Што веќе постои

Правила и skill. Нема пакет, нема база, нема UI логика. Не препишувај ги правилата.

## Што да изградиш

Скелет што се увезува, се составува во `composition.py` и отвора празна Streamlit страница. Машината за заклучување во оваа фаза јавно кажува дека сè уште не заклучува.

### Пакување

`pyproject.toml` со:

- име на проектот `pc-fault-diagnosis`
- `requires-python = ">=3.11"`
- зависимости `streamlit` и `pyyaml`
- опционална dev зависност `pytest`
- setuptools и пакети од `src`

`.gitignore` за `.venv/`, `__pycache__/`, `.pytest_cache/`, `*.egg-info/` и `.streamlit/`.

Не замрзнувај точни верзии ако не си ги проверил. Не додавај линтер, formatter, pre-commit, ниту CI.

### Доменски модели

Во `src/pc_fault_diagnosis/domain/models.py`, замрзнати dataclass-ови, без методи што само го враќаат поле:

- `ItemKind`: `SYMPTOM`, `FACT`
- `ConclusionKind`: `FACT`, `FAULT`
- `DiagnosisStatus`: `CONFIRMED`, `PARTIAL`
- `Subsystem`: `id`, `label_mk`
- `Symptom`: `id`, `subsystem_id`, `label_mk`, `description_mk`
- `Fault`: `id`, `name_mk`, `summary_mk`
- `Fact`: `id`, `label_mk`
- `Rule`: `id`, `when_present`, `when_absent`, `conclusion_kind`, `conclusion_id`, `explanation_mk`, `recommendations_mk`
- `KnowledgeBase`: `subsystems`, `symptoms`, `faults`, `facts`, `rules` како торки
- `Evidence`: `present_symptom_ids` како `frozenset[str]`
- `KnowledgeItem`: `id`, `label_mk`, `kind`
- `RuleMatch`: `rule_id`, `explanation_mk`, `recommendations_mk`, `matched`, `missing`, `contradicted`, `score`
- `Diagnosis`: `fault`, `score`, `status`, `matches`
- `DiagnosisResult`: `diagnoses`

Полињата што се низи се торки, за објектите да останат непроменливи. Не прави втор DTO слој за UI.

Во `src/pc_fault_diagnosis/domain/errors.py`:

- `KnowledgeBaseError(Exception)` за расипан YAML; пораката е техничка, на англиски
- `UnknownSymptomError(Exception)` со поле `symptom_id`; без македонска реченица во исклучокот, реченицата ја составува UI

### Договор за YAML

`knowledge/computer_faults.yaml` во оваа фаза има празни листи, не дефекти:

```yaml
subsystems: []
symptoms: []
faults: []
facts: []
rules: []
```

Фајлот е UTF-8. Подоцнежната фаза го полни. Обликот што репозиториумот го прифаќа:

```yaml
subsystems:
  - id: power
    label_mk: Напојување
symptoms:
  - id: no_power_led
    subsystem: power
    label_mk: Не свети индикаторот за напојување
    description_mk: Куќиштето не дава знак дека добива струја.
faults:
  - id: faulty_psu
    name_mk: Неисправно напојување
    summary_mk: Напојувањето не испорачува стабилна струја.
facts:
  - id: power_path_dead
    label_mk: Плочата не добива струја
rules:
  - id: rule_power_path_dead
    when_present: [no_power_led, no_fans]
    when_absent: [burning_smell]
    conclude:
      kind: fact
      id: power_path_dead
    explanation_mk: Нема знак дека плочата добива струја.
    recommendations_mk: []
```

`conclude.kind` е `fact` или `fault`.

### Репозиториум

`KnowledgeRepository` е `Protocol` со `load(self) -> KnowledgeBase`.

`YamlKnowledgeRepository` го прима патот во конструкторот, го чита фајлот при секој `load` и не чува кеш. Празните листи се валидна база.

Валидација, секоја со `KnowledgeBaseError` што кажува кој идентификатор е проблемот:

- постојат клучевите `subsystems`, `symptoms`, `faults`, `facts`, `rules`
- идентификаторите во секоја од тие листи се уникатни, а факт и симптом не делат идентификатор
- секој симптом покажува кон постоечки потсистем
- секое правило има барем еден `when_present` елемент
- секој услов е или симптом или факт од каталогот
- `conclude.kind: fact` покажува кон факт, `fault` кон дефект
- правило не го наведува сопствениот заклучок во `when_present`
- празна низа `recommendations_mk` е дозволена

Не гради општ пронаоѓач на циклуси. Не додавај шема-библиотека.

### Машина и use case

`InferenceEngine` е `Protocol` со два методи:

- `catalog(self) -> KnowledgeBase`
- `infer(self, evidence: Evidence) -> DiagnosisResult`

`ForwardChainingEngine` го прима репозиториумот во конструкторот. `catalog` ја враќа базата од `load()`, без кеш. `infer` во оваа фаза фрла `NotImplementedError`. Не ставај празен резултат наместо тоа: празен резултат би изгледал како готова машина.

`DiagnoseComputer` го прима само engine. `catalog` го проследува повикот. `diagnose(self, selected_symptom_ids: Sequence[str]) -> DiagnosisResult` ја предава работата на `infer`. Не чита YAML и не го фаќа `NotImplementedError`.

### Составување и екран

`build_diagnose_computer(knowledge_path: Path | None = None) -> DiagnoseComputer` во `composition.py`. Стандардниот пат е `knowledge/computer_faults.yaml` во коренот на репозиториумот, пресметан од локацијата на фајлот, не од тековниот работен директориум.

`ui/streamlit_app.py` има `main()`. Страницата покажува наслов „Дијагностика на дефект кај компјутер“ и една реченица дека базата е поврзана, а заклучувањето сè уште не е вклучено. Не прикажува симптоми и не повикува `diagnose`.

`app.py` во коренот само ја повикува `main()`.

`__init__.py` фајловите се празни. Не реекспортирај јавен API.

## Начин на работа

- Провери дали `python -c "from pc_fault_diagnosis.composition import build_diagnose_computer"` работи од околината каде пакетот е инсталиран со `pip install -e .`
- Провери дали празниот YAML се вчитува преку репозиториумот.
- Провери дали `ForwardChainingEngine.infer` фрла `NotImplementedError`.
- Пушти ја страницата со `streamlit run app.py` само колку да видиш дека се отвора, па запри го серверот.
- Не пишувај тестови во оваа фаза. Нив ги носи фазата 05.
- Не го менувај кореновиот README. Него го заменува фазата 08.

## Критериуми за прифаќање

- Дрвото од правилото постои и нема дополнителни пакети.
- Конкретните класи се создаваат само во `composition.py`.
- UI не увезува engine, repository, ниту PyYAML.
- Празен YAML се вчитува. Погрешен идентификатор фрла `KnowledgeBaseError`.
- Нема правила за вистински дефекти и нема forward chaining.

## Забрани

Не ја полни базата. Не ја имплементирај формулата. Не додавај страници, најава, база на податоци, кеш, логови, ниту конфигурациски објект. Не ги менувај `prompts/` ниту `.cursor/rules`.
