# Промптови по фази

Сите фази за системот за дијагностика на дефект кај компјутер, собрани во еден фајл. Истиот текст е поделен во `prompts/`, за да се копира една фаза во нов разговор.

Се работи само на `main`. Секоја фаза има повеќе мали commit-и. Далечинското репо е `https://github.com/Nikolaa00/Knowledge-Based-Expert-System-for-Computer-Fault-Diagnosis.git`. Нема база на податоци. Еден Dockerfile доаѓа во последната фаза.


---

# Фаза 00 — Репозиториум и комитети

Копирај го целиот овој фајл во нов агентски разговор ако репото уште не е врзано. Оваа фаза не гради систем. Ги остава промптовите и правилото за историјата на `main`.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом. Стек: Python 3.11 и Streamlit.

Целиот текст на секоја фаза стои и во [PROMPTS.md](../PROMPTS.md). Тој фајл се чита од почеток до крај. Фајловите во `prompts/` се истиот текст, поделен за да се копира една фаза.

## Репозиториум

Далечинското репо е:

`https://github.com/Nikolaa00/Knowledge-Based-Expert-System-for-Computer-Fault-Diagnosis.git`

Ако далечинскиот `github` го нема:

```bash
git remote add github https://github.com/Nikolaa00/Knowledge-Based-Expert-System-for-Computer-Fault-Diagnosis.git
```

Работи само на `main`. Не отворај гранка: на проектот работи еден студент. Не прави pull request.

Секоја фаза се дели на повеќе мали commit-и, таму каде резот е логичен. Еден commit една намера. Пораката е на англиски, во наредно време, кратка, без точка на крајот. Се чита без отворање на diff-от.

Не комитирај `.venv/`, `__pycache__/`, `.pytest_cache/`, тајни или датотеки на уредувачот. Не менувај ја историјата со rebase или force push.

По секоја затворена фаза:

```bash
git push github main
```

Ако постои и `origin`, пушти го истиот `main` и таму, без да го препишуваш.

## Што не се додава

Нема база на податоци. Базата на знаење е `knowledge/computer_faults.yaml`, за секое правило да е прегледлив commit, не миграција. Нема Docker Compose и нема втор сервис. Во фазата 09 има еден `Dockerfile` само за да се пушти истата Python околина.

## Комитети по фаза

Фаза 01, правила:

- `Add architecture rule for the expert system`
- `Add course deliverable rule`
- `Add project skill for fault diagnosis`

Фаза 02, архитектура:

- `Add package metadata and gitignore`
- `Add domain models and errors`
- `Add YAML repository validation`
- `Add inference boundary and use case`
- `Add composition root and placeholder screen`

Фаза 03, знаење:

- `Add symptom and fault catalog`
- `Add diagnostic production rules`

Фаза 04, машина:

- `Score rules against working memory`
- `Chain matched facts into diagnoses`

Фаза 05, екран:

- `Return the catalog through the use case`
- `Select symptoms by subsystem`
- `Show ranked diagnoses and explanations`

Фаза 06, тестови:

- `Test knowledge base validation`
- `Test forward chaining cases`
- `Test the diagnose use case`

Фаза 07, дијаграми:

- `Describe the use case scenario`
- `Draw the component interfaces`
- `Draw the diagnosis sequences`

Фаза 08, извештај:

- `Draft the project report`
- `Add checked references`

Фаза 09, документација:

- `Document the public boundaries`
- `Write the run instructions`
- `Run the app from one Docker image`

Ако некој рез не постои во кодот, не прави празен commit за да се исполни листата. Ако се појави нов логичен рез, додај commit со ист стил.

## Критериуми за прифаќање

- `github` покажува кон репото горе.
- Тековната гранка е `main`.
- `PROMPTS.md` ги содржи фазите 00 до 09.
- Нема код на системот во оваа фаза, ако фазите по неа уште не се извршени.

## Забрани

Не ставај токен во репото. Не отворај гранка. Не додавај база. Не ги спојувај фазите во еден commit.

---

# Фаза 01 — Правила и skill

Копирај го целиот овој фајл во нов агентски разговор. Запри кога ќе ги исполниш критериумите. Не ја почнувај фазата 02.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Одобрена е Тема 4, домен „дијагностика на дефект кај компјутер според симптом“. Стек: Python 3.11 и Streamlit. Излез од целиот проект, не од оваа фаза: функционална апликација што оперира со знаење и технички извештај.

Оваа фаза само ги заклучува правилата по кои ќе се гради системот. Не создавај Python пакет, YAML база, тестови, дијаграми, извештај, ниту README на апликацијата.

## Што да создадеш

Два rule фајла и еден skill, со содржината подолу, без дополнителни правила и без втор skill.

### `.cursor/rules/architecture.mdc`

```markdown
---
description: Граници на експертскиот систем за дијагностика на компјутерски дефект
alwaysApply: true
---

# Архитектура

Домен: дијагностика на дефект кај компјутер според симптоми. Python 3.11 и Streamlit. Знаењето е податок во `knowledge/computer_faults.yaml`, не гранки во кодот.

Дрво:

- `src/pc_fault_diagnosis/domain/models.py` — замрзнати dataclass модели
- `src/pc_fault_diagnosis/domain/errors.py` — `UnknownSymptomError`, `KnowledgeBaseError`
- `src/pc_fault_diagnosis/knowledge/repository.py` — `KnowledgeRepository`, `YamlKnowledgeRepository`
- `src/pc_fault_diagnosis/inference/engine.py` — `InferenceEngine`, `ForwardChainingEngine`
- `src/pc_fault_diagnosis/application/diagnose.py` — `DiagnoseComputer`
- `src/pc_fault_diagnosis/composition.py` — единствено поврзување на конкретните класи
- `src/pc_fault_diagnosis/ui/streamlit_app.py` — адаптер за екран
- `app.py` — влез за Streamlit, само повик кон UI
- `knowledge/computer_faults.yaml`
- `tests/`
- `docs/diagrams/`
- `docs/report/`

Дозволени повици:

- UI смее да ги повика само `DiagnoseComputer.catalog` и `DiagnoseComputer.diagnose`
- `DiagnoseComputer` смее да ги повика само `InferenceEngine.catalog` и `InferenceEngine.infer`
- `ForwardChainingEngine` го повикува само `KnowledgeRepository.load`
- `YamlKnowledgeRepository` го чита само YAML фајлот
- `composition.py` е единственото место каде се создаваат `YamlKnowledgeRepository`, `ForwardChainingEngine` и `DiagnoseComputer`

Протоколи се само `KnowledgeRepository` и `InferenceEngine`. Не додавај протокол, апстрактна класа или интерфејс за другите класи.

Имиња на модули, фајлови, класи, методи, аргументи и променливи: англиски, `snake_case` за модули и функции, `PascalCase` за класи, `UPPER_SNAKE` за константи. Текстот за корисникот и извештајот: македонски.

Формула, иста во машината и во тестовите:

- услов од `when_present` е исполнет ако идентификаторот е во работната меморија
- услов од `when_absent` е исполнет ако идентификаторот не е во работната меморија
- `score = исполнети услови / сите услови`
- противречен симптом е избран симптом што правилото го бара како отсутен; тој услов не е исполнет, па резултатот е понизок
- факт влегува во работната меморија само кога правилото што го заклучува има `score == 1`
- дефект се прикажува ако барем еден негов rule match има `score >= 0.5` и барем еден `when_present` елемент е во меморијата
- статус `confirmed` само кога `score == 1`
- статус `partial` кога `0.5 <= score < 1`
- еден дефект се појавува еднаш; неговиот `score` е највисокиот меѓу правилата што водат до него

Константи: `PARTIAL_SCORE_THRESHOLD = 0.5` во inference модулот. Не ја повторувај бројката низ UI.

Не додавај база, најава, веб-сервис, машинско учење, Bayesian мрежа, MYCIN аритметика, онтологија, уредувач на правила, `utils.py`, `helpers.py`, `base.py`, ниту слој што никој не го повикува. Нов дефект се додава во YAML и со тест, не со нова гранка во UI.
```

### `.cursor/rules/course-deliverables.mdc`

```markdown
---
description: Испораки за проектната задача по Системи базирани на знаење
alwaysApply: true
---

# Испораки на предметот

Апликацијата оперира со знаење: база на правила, работна меморија и inference engine. Покрај апликацијата стои техничка документација.

Извештајот во `docs/report/izvestaj.md` има Вовед, Главен дел и Заклучок. Главниот дел мора да ги покрие, со содржина од вистинскиот систем:

- прецизен опис на апликацијата
- конечно use case сценарио и use case дијаграм
- компонентен дијаграм со сите компоненти и интеграцискиот интерфејс меѓу нив
- секвенциски дијаграми за текот на настаните
- резултати: кои влезови се бараат и кои излези се произведуваат

Референците се нумерирани. Секоја има наслов, автори или организација, URL и причина за избор. Годината на објавување е 2021 или понова. Исклучок е дозволен само за врвно, високо цитирано дело, со една реченица зошто исклучокот е потребен. Извор што не е отворен и проверен не се наведува.

Дијаграмите живеат во `docs/diagrams/` и се вградени во извештајот. Не цртај компоненти што кодот ги нема.
```

### `.cursor/skills/pc-fault-diagnosis/SKILL.md`

```markdown
---
name: pc-fault-diagnosis
description: Use when changing the PC fault diagnosis expert system, its YAML knowledge base, forward-chaining engine, Streamlit UI, tests, diagrams, or the course report.
---

# Дијагностика на компјутерски дефект

Прочитај ги `.cursor/rules/architecture.mdc` и `.cursor/rules/course-deliverables.mdc` пред измена.

Знаењето се менува само во `knowledge/computer_faults.yaml`. По секое ново или сменето правило додај или прилагоди фокусиран тест. Не кодирај правила во Python.

Машината за заклучување ја држи формулата од архитектонското правило. Ако ја менуваш формулата, во истата измена ги менуваш тестовите и описот во извештајот. Не воведувај втор начин на бодување.

UI увезува `build_diagnose_computer` од `composition.py` и ги повикува само `catalog` и `diagnose`. Не увезува engine, repository, ниту PyYAML.

Корисничките реченици се на македонски. Имињата во кодот остануваат на англиски.

Не проширувај го опсегот: нема база, најава, машинско учење, ниту втор домен.
```

## Начин на работа

- Создај ги фајловите со таа содржина. Не додавај воведни коментари околу неа.
- Не создавај `AGENTS.md`, втор skill, ниту правила за стил на код што веќе се кажани.
- Не почнувај имплементација на системот.

## Критериуми за прифаќање

- Постојат точно два `.mdc` фајла и точно еден `SKILL.md`, на патеките горе.
- Двата rule фајла имаат `alwaysApply: true`.
- Skill-от има `name` и `description` во frontmatter.
- Нема `src/`, `knowledge/`, `tests/`, `docs/`, ниту `pyproject.toml`.
- Формулата, дрвото и забраните се запишани еднаш во правилата, не во нов документ.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не ја имплементирај апликацијата. Не ги менувај фајловите во `prompts/`. Не додавај слајдови, CI, база или уште еден слој правила.

---

# Фаза 02 — Архитектура

Копирај го целиот овој фајл во нов агентски разговор. Запри на скелетот. Не ја полни базата со дефекти и не пишувај алгоритам за заклучување.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом. Python 3.11, Streamlit, знаење во YAML.

Фазата 01 веќе ги има ставено `.cursor/rules/architecture.mdc`, `.cursor/rules/course-deliverables.mdc` и `.cursor/skills/pc-fault-diagnosis/SKILL.md`. Прочитај ги пред првата измена и држи се до нив. Ако некој детаљ од овој промпт го прецизира правилото, овој промпт е изворот за имињата на типовите.

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
- Не пишувај тестови во оваа фаза. Нив ги носи фазата 06.
- Не го менувај кореновиот README. Него го заменува фазата 09.

## Критериуми за прифаќање

- Дрвото од правилото постои и нема дополнителни пакети.
- Конкретните класи се создаваат само во `composition.py`.
- UI не увезува engine, repository, ниту PyYAML.
- Празен YAML се вчитува. Погрешен идентификатор фрла `KnowledgeBaseError`.
- Нема правила за вистински дефекти и нема forward chaining.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не ја полни базата. Не ја имплементирај формулата. Не додавај страници, најава, база на податоци, кеш, логови, ниту конфигурациски објект. Не ги менувај `prompts/` ниту `.cursor/rules`.

---

# Фаза 03 — База на знаење

Копирај го целиот овој фајл во нов агентски разговор. Оваа фаза го полни знаењето. Не ја имплементира машината и не го менува екранот.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом.

Фазите 01 и 02 веќе ги имаат правилата, skill-от и скелетот. Прочитај ги `.cursor/rules/architecture.mdc` и `src/pc_fault_diagnosis/knowledge/repository.py` пред измена. Репозиториумот веќе го валидира обликот. Не го олабавувај за да помине базата.

## Што веќе постои

Празен `knowledge/computer_faults.yaml` и репозиториум што ја вчитува базата на потсистеми, симптоми, дефекти, факти и правила. `ForwardChainingEngine.infer` сè уште фрла `NotImplementedError`. Така и останува.

## Што да направиш

Замени го празниот YAML со каталогот подолу. Зачувај ги идентификаторите, врските и македонските текстови. Текстот е дел од знаењето: краток, конкретен, како што би го кажал техничар. Не додавај симптоми, дефекти или правила што ги нема овде. Секој симптом влегува во барем едно правило, и тоа веќе е исполнето со овој каталог.

Фајлот останува UTF-8. По полнењето, вчитај го преку `YamlKnowledgeRepository` и поправи ја валидацијата само ако каталогот открие вистинска грешка во репозиториумот. Не менувај го договорот за полињата.

### Каталог

```yaml
subsystems:
  - id: power
    label_mk: Напојување
  - id: boot
    label_mk: Бутање
  - id: display
    label_mk: Екран
  - id: storage
    label_mk: Диск
  - id: memory
    label_mk: Меморија
  - id: network
    label_mk: Мрежа
  - id: performance
    label_mk: Перформанси
  - id: peripherals
    label_mk: Периферни уреди

symptoms:
  - id: no_power_led
    subsystem: power
    label_mk: Не свети индикаторот за напојување
    description_mk: Куќиштето не дава знак дека добива струја.
  - id: no_fans
    subsystem: power
    label_mk: Вентилаторите не се вртат
    description_mk: По притискање на копчето нема вртење ниту шум од вентилатор.
  - id: burning_smell
    subsystem: power
    label_mk: Мирис на изгорено
    description_mk: Од куќиштето се чувствува мирис на изгорена електроника.
  - id: psu_clicks
    subsystem: power
    label_mk: Напојувањето кликнува и се гаси
    description_mk: Се слуша клик, уредот за миг фаќа струја и пак се гаси.
  - id: works_after_reseating_cable
    subsystem: power
    label_mk: Работи откако ќе се помрдне кабелот
    description_mk: Се вклучува само кога кабелот за струја ќе се притисне повторно.
  - id: no_post
    subsystem: boot
    label_mk: Нема POST
    description_mk: Нема обичен екран за проверка и системот не продолжува кон бутање.
  - id: beeps_continuous
    subsystem: boot
    label_mk: Континуирани звучни сигнали
    description_mk: Звучникот на плочата писка без прекин.
  - id: beeps_one_long
    subsystem: boot
    label_mk: Еден долг звучен сигнал
    description_mk: Се слуша еден долг сигнал при вклучување.
  - id: restarts_before_os
    subsystem: boot
    label_mk: Се рестартира пред системот
    description_mk: Уредот се гаси и пали повторно пред да се појави оперативниот систем.
  - id: bios_resets
    subsystem: boot
    label_mk: BIOS поставките се ресетираат
    description_mk: Датумот и поставките се губат по исклучување од струја.
  - id: no_signal
    subsystem: display
    label_mk: Мониторот јавува нема сигнал
    description_mk: Мониторот е вклучен, но јавува дека нема видеосигнал.
  - id: artifacts
    subsystem: display
    label_mk: Линии или коцки на сликата
    description_mk: На екранот има погрешни бои, линии или коцки.
  - id: backlight_only
    subsystem: display
    label_mk: Екранот е црн, светлото работи
    description_mk: Панелот свети слабо, но нема слика.
  - id: external_display_ok
    subsystem: display
    label_mk: Надворешниот монитор е исправен
    description_mk: Истата слика е добра на друг монитор или телевизор.
  - id: slow_boot_disk
    subsystem: storage
    label_mk: Долго бутање со активен диск
    description_mk: Логото стои долго, а дискот постојано работи.
  - id: clicking_disk
    subsystem: storage
    label_mk: Чукање од дискот
    description_mk: Се слуша ритмичко чукање или стругање од дискот.
  - id: files_disappear
    subsystem: storage
    label_mk: Датотеки не се отвораат
    description_mk: Датотеки исчезнуваат, се оштетуваат или не се отвораат.
  - id: smart_warning
    subsystem: storage
    label_mk: Предупредување за дискот
    description_mk: Системот јавува дека дискот може да откаже.
  - id: random_freeze
    subsystem: memory
    label_mk: Случајно замрзнување
    description_mk: Сликата застанува без порака и помага само рестарт.
  - id: bsod_memory
    subsystem: memory
    label_mk: Син екран поврзан со меморија
    description_mk: Синиот екран споменува меморија или memory management.
  - id: passes_one_stick
    subsystem: memory
    label_mk: Работи со една мемориска плочка
    description_mk: Со едната плочка бута, со двете не бута.
  - id: memtest_errors
    subsystem: memory
    label_mk: MemTest јавува грешки
    description_mk: Тестот на меморијата пријавува грешки.
  - id: no_wifi
    subsystem: network
    label_mk: Нема Wi-Fi мрежи
    description_mk: Адаптерот не прикажува ниту една безжична мрежа.
  - id: wifi_drops
    subsystem: network
    label_mk: Wi-Fi врската се кине
    description_mk: Врската се воспоставува и пак исчезнува по кратко време.
  - id: ethernet_dead
    subsystem: network
    label_mk: Кабелската мрежа не добива адреса
    description_mk: Приклучен кабел не добива мрежна адреса.
  - id: other_devices_online
    subsystem: network
    label_mk: Другите уреди се на мрежа
    description_mk: Телефон или друг компјутер на истата мрежа работи нормално.
  - id: high_cpu_idle
    subsystem: performance
    label_mk: Висок процесор во мирување
    description_mk: Процесорот е зафатен иако не е отворена тешка програма.
  - id: thermal_shutdown
    subsystem: performance
    label_mk: Се гаси под оптоварување
    description_mk: Уредот се исклучува кога ќе се загрее при работа.
  - id: loud_fans_hot
    subsystem: performance
    label_mk: Гласни вентилатори и топол воздух
    description_mk: Вентилаторите вијат, а воздухот од куќиштето е топол.
  - id: stutter_games
    subsystem: performance
    label_mk: Сецкање во игри и 3D
    description_mk: Сецкањето се јавува во игри или други тродимензионални програми.
  - id: usb_not_detected
    subsystem: peripherals
    label_mk: USB уредот не се препознава
    description_mk: Уредот е приклучен, но не се појавува во системот.
  - id: usb_power_only
    subsystem: peripherals
    label_mk: USB уредот само добива струја
    description_mk: Свети лампичката на уредот, но компјутерот не го гледа.
  - id: keyboard_repeat
    subsystem: peripherals
    label_mk: Тастатурата повторува или молчи
    description_mk: Знаците се повторуваат, или дел од типките не реагираат.
  - id: works_on_other_port
    subsystem: peripherals
    label_mk: Работи на друга порта
    description_mk: Истиот уред работи кога ќе се префрли на друга порта.

facts:
  - id: power_path_dead
    label_mk: Плочата не добива струја
  - id: memory_subsystem_suspect
    label_mk: Сомнителен мемориски потсистем

faults:
  - id: faulty_psu
    name_mk: Неисправно напојување
    summary_mk: Напојувањето не испорачува стабилна струја до плочата.
  - id: loose_power_cable
    name_mk: Лабав кабел за напојување
    summary_mk: Струјата се губи на кабелот или на приклучокот.
  - id: burnt_component
    name_mk: Изгорена компонента
    summary_mk: Има знак за изгорена компонента во патеката на напојување.
  - id: loose_ram
    name_mk: Лошо наместена меморија
    summary_mk: Мемориската плочка не прави сигурен контакт.
  - id: faulty_ram
    name_mk: Неисправна меморија
    summary_mk: Меморијата враќа грешки или го запира бутањето.
  - id: dead_cmos_battery
    name_mk: Испразнета CMOS батерија
    summary_mk: Батеријата на плочата не ги чува поставките.
  - id: faulty_gpu
    name_mk: Неисправна графичка картичка
    summary_mk: Графичката картичка дава погрешна или никаква слика.
  - id: faulty_display_panel
    name_mk: Неисправен екран
    summary_mk: Панелот на екранот не ја прикажува сликата што уредот ја испраќа.
  - id: failing_disk
    name_mk: Диск што откажува
    summary_mk: Дискот има механички или SMART знак дека откажува.
  - id: corrupted_filesystem
    name_mk: Оштетен датотечен систем
    summary_mk: Податоците се оштетени без знак дека дискот механички откажува.
  - id: faulty_wifi_adapter
    name_mk: Неисправен безжичен адаптер
    summary_mk: Безжичниот адаптер не држи врска, а мрежата инаку работи.
  - id: bad_ethernet_cable_or_port
    name_mk: Лош кабел или мрежна порта
    summary_mk: Кабелската врска не добива адреса иако мрежата работи за другите.
  - id: overheating
    name_mk: Прегревање
    summary_mk: Уредот се гаси затоа што не се лади доволно.
  - id: background_cpu_load
    name_mk: Позадинско оптоварување
    summary_mk: Процесорот го троши процес што работи во позадина.
  - id: faulty_usb_port
    name_mk: Неисправна USB порта
    summary_mk: Портата дава струја или контакт, но не ја држи врската стабилно.
  - id: faulty_keyboard
    name_mk: Неисправна тастатура
    summary_mk: Тастатурата повторува знаци или не реагира на сите типки.

rules:
  - id: rule_power_path_dead
    when_present: [no_power_led, no_fans]
    when_absent: [burning_smell]
    conclude: {kind: fact, id: power_path_dead}
    explanation_mk: Нема светло и нема вртење на вентилаторите, без мирис на изгорено. Плочата не добива струја.
    recommendations_mk: []
  - id: rule_faulty_psu
    when_present: [power_path_dead, psu_clicks]
    when_absent: [works_after_reseating_cable]
    conclude: {kind: fault, id: faulty_psu}
    explanation_mk: Патеката на струја е мртва, а напојувањето кликнува и се гаси. Тоа е знак за неисправно напојување.
    recommendations_mk:
      - Исклучи го кабелот и провери дали има мирис на изгорено пред повторно вклучување.
      - Испитај со друго познато исправно напојување.
  - id: rule_loose_cable
    when_present: [power_path_dead, works_after_reseating_cable]
    when_absent: [psu_clicks]
    conclude: {kind: fault, id: loose_power_cable}
    explanation_mk: Струјата се појавува дури откако кабелот ќе се помрдне. Контактот на кабелот е лабав.
    recommendations_mk:
      - Замени го кабелот за напојување.
      - Провери ја утичницата и продолжниот кабел со друг уред.
  - id: rule_burnt_component
    when_present: [burning_smell]
    when_absent: [works_after_reseating_cable]
    conclude: {kind: fault, id: burnt_component}
    explanation_mk: Се чувствува мирис на изгорено. Не вклучувај го уредот повторно.
    recommendations_mk:
      - Остави го уредот исклучен од струја.
      - Отвори го само ако знаеш што бараш, или однеси го на преглед.
  - id: rule_boot_loop_psu
    when_present: [restarts_before_os, psu_clicks]
    when_absent: [burning_smell, no_power_led, no_fans]
    conclude: {kind: fault, id: faulty_psu}
    explanation_mk: Уредот се рестартира пред системот, а напојувањето кликнува. Напојувањето не ја држи струјата.
    recommendations_mk:
      - Исклучи ги непотребните USB уреди и пробај уште еднаш.
      - Ако кликот остане, замени го напојувањето.
  - id: rule_memory_suspect
    when_present: [no_post, beeps_continuous]
    when_absent: []
    conclude: {kind: fact, id: memory_subsystem_suspect}
    explanation_mk: Нема POST, а звучникот писка без прекин. Плочата укажува на меморија.
    recommendations_mk: []
  - id: rule_memory_suspect_long_beep
    when_present: [no_post, beeps_one_long]
    when_absent: []
    conclude: {kind: fact, id: memory_subsystem_suspect}
    explanation_mk: Нема POST и се слуша еден долг сигнал. Проверката застанува на меморијата.
    recommendations_mk: []
  - id: rule_loose_ram
    when_present: [memory_subsystem_suspect, passes_one_stick]
    when_absent: [memtest_errors]
    conclude: {kind: fault, id: loose_ram}
    explanation_mk: Со една плочка бута, а тестот не јавува грешка. Контактот на плочката е поверојатен од изгорена меморија.
    recommendations_mk:
      - Извади ги плочките, исчисти го контактот и намести ги повторно.
      - Пробај ја секоја плочка во првиот слот.
  - id: rule_faulty_ram
    when_present: [memory_subsystem_suspect, memtest_errors]
    when_absent: []
    conclude: {kind: fault, id: faulty_ram}
    explanation_mk: Знакот при бутање води до меморија, а MemTest потврдува грешки.
    recommendations_mk:
      - Тестирај ја секоја плочка одделно.
      - Замени ја плочката што јавува грешка.
  - id: rule_faulty_ram_bsod
    when_present: [bsod_memory, random_freeze]
    when_absent: [thermal_shutdown]
    conclude: {kind: fault, id: faulty_ram}
    explanation_mk: Син екран за меморија и замрзнување, без гасење од топлина. Меморијата е неисправна.
    recommendations_mk:
      - Пушти MemTest од USB.
      - Ако грешката се повторува на една плочка, замени ја.
  - id: rule_cmos_battery
    when_present: [bios_resets]
    when_absent: [no_power_led]
    conclude: {kind: fault, id: dead_cmos_battery}
    explanation_mk: Поставките се губат иако уредот инаку добива струја. CMOS батеријата не држи.
    recommendations_mk:
      - Замени ја CR2032 батеријата на плочата.
      - По замена постави датум и провери дали се задржува.
  - id: rule_faulty_gpu
    when_present: [artifacts, stutter_games]
    when_absent: [external_display_ok]
    conclude: {kind: fault, id: faulty_gpu}
    explanation_mk: Има артефакти и сецкање во 3D, а сликата не е добра ни на друг екран.
    recommendations_mk:
      - Извади ја картичката и намести ја повторно.
      - Пробај со друга картичка или со вградената графика.
  - id: rule_no_signal_gpu
    when_present: [no_signal, no_post]
    when_absent: [no_power_led]
    conclude: {kind: fault, id: faulty_gpu}
    explanation_mk: Струја има, но нема POST ниту видеосигнал. Графичкиот излез не тргнува.
    recommendations_mk:
      - Провери дали кабелот е во картичката, не во плочата.
      - Отстрани ја дискретната картичка и пробај со вградената графика.
  - id: rule_display_panel
    when_present: [backlight_only, external_display_ok]
    when_absent: []
    conclude: {kind: fault, id: faulty_display_panel}
    explanation_mk: Надворешниот екран е добар, а вградениот панел останува црн. Панелот или неговиот кабел е неисправен.
    recommendations_mk:
      - Провери го кабелот на панелот ако уредот се отвора лесно.
      - Користи надворешен монитор до замена на панелот.
  - id: rule_failing_disk
    when_present: [clicking_disk, slow_boot_disk]
    when_absent: []
    conclude: {kind: fault, id: failing_disk}
    explanation_mk: Дискот чука и бутањето е долго. Тоа е механички знак дека дискот откажува.
    recommendations_mk:
      - Не инсталирај систем одново пред да ги ископираш важните податоци.
      - Замени го дискот и провери го стариот од друг компјутер само за копирање.
  - id: rule_smart_disk
    when_present: [smart_warning, slow_boot_disk]
    when_absent: []
    conclude: {kind: fault, id: failing_disk}
    explanation_mk: Системот предупредува за дискот, а бутањето е бавно. Дискот откажува.
    recommendations_mk:
      - Ископирај ги податоците веднаш.
      - Замени го дискот; не го игнорирај предупредувањето.
  - id: rule_corrupted_filesystem
    when_present: [files_disappear, slow_boot_disk]
    when_absent: [clicking_disk]
    conclude: {kind: fault, id: corrupted_filesystem}
    explanation_mk: Датотеките не се отвораат и бутањето е бавно, без чукање. Датотечниот систем е оштетен.
    recommendations_mk:
      - Пушти проверка на дискот од системот.
      - Прекини го запишувањето додека не се ископира она што сè уште се отвора.
  - id: rule_wifi_adapter
    when_present: [no_wifi, other_devices_online]
    when_absent: [ethernet_dead]
    conclude: {kind: fault, id: faulty_wifi_adapter}
    explanation_mk: Другите уреди ја гледаат мрежата, а овој не прикажува ниту една Wi-Fi мрежа.
    recommendations_mk:
      - Вклучи го адаптерот со функциското копче или од поставките.
      - Ако и по драјвер не гледа мрежа, адаптерот е неисправен.
  - id: rule_wifi_drops
    when_present: [wifi_drops, other_devices_online]
    when_absent: []
    conclude: {kind: fault, id: faulty_wifi_adapter}
    explanation_mk: Врската се кине само на овој уред. Безжичниот адаптер не ја држи мрежата.
    recommendations_mk:
      - Заборави ја мрежата и поврзи се повторно.
      - Пробај USB адаптер за да видиш дали вградениот откажува.
  - id: rule_ethernet
    when_present: [ethernet_dead, other_devices_online]
    when_absent: [no_wifi]
    conclude: {kind: fault, id: bad_ethernet_cable_or_port}
    explanation_mk: Кабелот не добива адреса, а другите уреди се на мрежа. Кабелот или портата не ја носат врската.
    recommendations_mk:
      - Пробај друг кабел и друга порта на рутерот.
      - Ако друг кабел работи, замени го кабелот; ако не работи, портата на компјутерот е сомнителна.
  - id: rule_overheating
    when_present: [thermal_shutdown, loud_fans_hot]
    when_absent: [no_fans]
    conclude: {kind: fault, id: overheating}
    explanation_mk: Вентилаторите работат гласно, воздухот е топол и уредот се гаси под товар.
    recommendations_mk:
      - Исчисти ја прашината и провери дали вентилаторот навистина се врти.
      - Провери ја пастата и дали уредот има воздух околу отворите.
  - id: rule_background_cpu
    when_present: [high_cpu_idle]
    when_absent: [thermal_shutdown]
    conclude: {kind: fault, id: background_cpu_load}
    explanation_mk: Процесорот е зафатен во мирување, без гасење од топлина. Товарот доаѓа од позадински процес.
    recommendations_mk:
      - Отвори го управувачот на задачи и подреди по процесор.
      - Запри го процесот што троши и провери дали се враќа по рестарт.
  - id: rule_usb_port
    when_present: [usb_not_detected, works_on_other_port]
    when_absent: []
    conclude: {kind: fault, id: faulty_usb_port}
    explanation_mk: Уредот се гледа на друга порта, значи уредот е исправен, а оваа порта не е.
    recommendations_mk:
      - Користи ја портата што работи.
      - Ако повеќе порти на иста група не работат, провери го кабелот на предниот панел.
  - id: rule_usb_power_only
    when_present: [usb_power_only, usb_not_detected]
    when_absent: []
    conclude: {kind: fault, id: faulty_usb_port}
    explanation_mk: Уредот добива струја, но системот не го препознава. Портата не ја носи податочната врска.
    recommendations_mk:
      - Пробај директно на порта од задниот панел.
      - Избегни незасилен USB разгранувач за проверка.
  - id: rule_keyboard
    when_present: [keyboard_repeat]
    when_absent: [works_on_other_port]
    conclude: {kind: fault, id: faulty_keyboard}
    explanation_mk: Тастатурата повторува или молчи и проблемот не исчезнува на друга порта.
    recommendations_mk:
      - Пробај друга тастатура на истата порта.
      - Ако другата работи, замени ја тастатурата.
```

Ова се 8 потсистеми, 34 симптоми, 2 факти, 16 дефекти и 25 правила. Две правила заклучуваат факт што подоцна го користи правило за дефект: `power_path_dead` и `memory_subsystem_suspect`. Тоа е синџирот што машината во следната фаза мора да го помине. Не додавај трет факт.

## Начин на работа

- Вчитај ја базата преку постоечкиот репозиториум и испечати ги броевите на симптоми, дефекти, факти и правила.
- Провери ги броевите: 34, 16, 2, 25.
- Не пишувај pytest фајлови. Не повикувај `infer`.
- Ако некој македонски текст во каталогот има печатна грешка што ја менува смислата, поправи ја смислата без да го менуваш идентификаторот.

## Критериуми за прифаќање

- `load()` завршува без `KnowledgeBaseError`.
- Идентификаторите се точно оние од каталогот.
- Секој симптом има потсистем, назив и опис на македонски.
- Секое правило за дефект има објаснување и барем една препорака. Правилата за факти имаат празни препораки.
- UI и `infer` не се сменети.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не кодирај правила во Python. Не додавај сигурносни фактори, тежини, веројатности, ниту втор фајл со знаење. Не ги менувај `prompts/` и `.cursor/rules`.

---

# Фаза 04 — Inference engine

Копирај го целиот овој фајл во нов агентски разговор. Имплементирај го заклучувањето. Не гради го екранот и не пишувај го тест-пакетот; работните примери пушти ги како кратко привремено проверување и отстрани го скриптот.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом.

Фазите 01–03 ги имаат правилата, скелетот и `knowledge/computer_faults.yaml`. Прочитај ги `.cursor/rules/architecture.mdc`, `domain/models.py` и каталогот. Формулата од правилото е договорот. Овој промпт ја прецизира постапката.

## Што веќе постои

`ForwardChainingEngine.infer` фрла `NotImplementedError`. Репозиториумот ја вчитува полната база. `DiagnoseComputer.diagnose` веќе го предава изборот на `infer`. UI сè уште не повикува дијагноза.

## Постапка

`catalog` веќе ја вчитува базата. `infer` нека ја користи истата приватна патека, одново при секој повик. Не чувај кеш и не додавај втор начин на вчитување.

1. Ако некој идентификатор од `Evidence.present_symptom_ids` не е симптом од каталогот, фрли `UnknownSymptomError` со тој `symptom_id`. Факт не е дозволен влез од корисникот.
2. Работната меморија почнува како множество од избраните симптоми.
3. Мини ги правилата по редот од фајлот. Правило со `score == 1` е целосно активирано. Ако заклучува факт, додај го фактот во меморијата и продолжи од првото правило, за следното правило да го види новиот факт во истата рунда. Веќе целосно активирано правило не се активира повторно.
4. Границата на рунди е бројот на правила. Тоа го запира циклусот ако две правила се хранат едно со друго. Не додавај библиотека за граф.
5. По целосното активирање, пресметај го резултатот на секое правило уште еднаш врз конечната меморија. Во резултатот за корисникот влегуваат само правила што заклучуваат дефект, имаат `score >= PARTIAL_SCORE_THRESHOLD` и имаат барем еден `when_present` елемент во меморијата.
6. Целосно активирано правило за факт не е дијагноза. Во трагата на дефект влегува само ако тој дефект го користи фактот во `when_present` и правилото за фактот е целосно активирано. Трагата го става правилото за фактот прво, по редот на активирање, па правилото за дефектот. Едно ниво на факт е доволно; не гради општо дрво на објаснување.
7. Групирај ги преостанатите правила по дефект. Еден дефект, една `Diagnosis`. Нејзиниот `score` е највисокиот score меѓу нејзините rule match ставки. Статусот е `confirmed` ако тој score е 1, инаку `partial`.
8. Подреди ги дијагнозите по опаѓачки score, па по `fault.id` растечки. Внатре во дијагнозата, правилата за дефект по опаѓачки score, па по `rule_id` растечки. Правилата за факти остануваат пред нив.
9. `matched`, `missing` и `contradicted` носат `KnowledgeItem` со македонски назив и `ItemKind`. Препораките на дијагнозата се препораките од правилата за тој дефект, по редот на трагата, без повторување. UI ги чита од `matches`, не од посебно поле.

Формула, за секое правило, врз тековната меморија:

- `total = len(when_present) + len(when_absent)`
- исполнет `when_present` елемент е оној што е во меморијата
- исполнет `when_absent` елемент е оној што не е во меморијата
- противречен е `when_absent` елемент што е во меморијата
- `score = исполнети / total`

`PARTIAL_SCORE_THRESHOLD = 0.5` е константа во `inference/engine.py`.

Празен доказ не фрла грешка и враќа `DiagnosisResult` без дијагнози. Не третирај го празниот доказ како непознат симптом.

Не менувај го YAML за да ти биде полесен алгоритмот.

## Работени примери

Провери ги по имплементацијата. Очекувањата се договор за фазата 06.

1. Симптоми `no_power_led`, `no_fans`, `psu_clicks`. `rule_power_path_dead` има score 1 и го додава `power_path_dead`. `rule_faulty_psu` има score 1. Една потврдена дијагноза `faulty_psu`. Трагата е `rule_power_path_dead`, па `rule_faulty_psu`.
2. Симптоми `thermal_shutdown`, `loud_fans_hot`, `no_fans`. `rule_overheating` има 2 од 3 услови, score `2/3`, статус `partial`. Не е `confirmed`.
3. Симптом само `slow_boot_disk`. `failing_disk` има score `0.5`. `corrupted_filesystem` има score `2/3`. Редослед: прво `corrupted_filesystem`, потоа `failing_disk`. Двата се `partial`. Трагата на дискот е `rule_failing_disk`, па `rule_smart_disk`.
4. Симптоми `clicking_disk`, `slow_boot_disk`, `smart_warning`, `high_cpu_idle`. `failing_disk` и `background_cpu_load` се `confirmed` со score 1. Редослед по идентификатор: `background_cpu_load`, па `failing_disk`. Трагата на дискот ги содржи `rule_failing_disk` и `rule_smart_disk`.
5. Празен доказ. Нема дијагнози и нема исклучок.
6. Симптом `not_a_symptom`. `UnknownSymptomError` со тој идентификатор.

## Начин на работа

- Држи ја пресметката во `ForwardChainingEngine`. Не ја дели на стратегија, политика и сервис.
- Приватен метод во истата класа е во ред ако `infer` инаку стане нечитлив. Не прави нова датотека за еден помошен метод.
- Docstring на класата, во неколку реченици, ја кажува формулата и дека факт влегува во меморијата само при score 1. Тоа е изворот за читателот на кодот.
- Привременото проверување избриши го пред да завршиш. Не оставај `scripts/`, `print` во engine, ниту тестови; тестовите се фаза 06.
- Не го менувај UI, освен ако увозот кон engine се скршил од преименување. Не преименувај.

## Критериуми за прифаќање

- Шесте примери даваат токму таков статус, score, редослед и трага.
- Engine не увезува PyYAML и не ја отвора датотеката сам.
- `DiagnoseComputer` сè уште не го познава репозиториумот.
- Каталогот не е сменет за да се наместат примерите.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Нема MYCIN, тежини, Bayesian пресметка, втор engine, ниту прашања што системот сам ги поставува. Не ја менувај формулата за да изгледа попаметно. Не ги менувај `prompts/` и `.cursor/rules`.

---

# Фаза 05 — Апликација и екран

Копирај го целиот овој фајл во нов агентски разговор. Поврзи го use case со екранот. Не пишувај pytest пакет, дијаграми, ниту извештај.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом.

Фазите 01–04 ги имаат правилата, моделите, YAML каталогот и `ForwardChainingEngine`. Прочитај ги architecture правилото, `DiagnoseComputer` и `streamlit_app.py`. Екранот е адаптер. Не го преместувај заклучувањето во него.

## Што веќе постои

`DiagnoseComputer.diagnose` го повикува `infer`. `build_diagnose_computer` ги составува репозиториумот, машината и use case. Страницата е само наслов. Каталогот има 8 потсистеми и 34 симптоми на македонски.

## Use case

Остави го `DiagnoseComputer` тенок:

- `catalog` го проследува каталогот од engine
- празен избор враќа `DiagnosisResult` без дијагнози и не повикува `infer`
- непразен избор гради `Evidence` и го предава на engine
- не фаќај `UnknownSymptomError` во use case; нека стигне до UI
- use case и понатаму не го познава YAML ниту конкретниот engine

Не додавај трет метод.

## Екран

`main()` ја добива апликацијата од `build_diagnose_computer()`. Каталогот доаѓа од `catalog()`. Ако тој повик фрли `KnowledgeBaseError`, покажи `st.error` со техничката порака и не цртај избор. Од каталогот користи ги само `subsystems` и `symptoms`, по редот од фајлот. Не читај правила во UI и не донесувај дијагноза од нив. Не вчитувај YAML во UI.

### Распоред

- `st.set_page_config` со наслов „Дијагностика на дефект кај компјутер“
- наслов и една реченица: „Избери ги симптомите што ги гледаш. Системот ги споредува со правилата и објаснува како дошол до дијагнозата.“
- на широк екран две колони: лево избор, десно резултат; на тесен екран Streamlit ги реди една под друга, не пишувај посебен мобилен распоред
- симптомите се по потсистем, секој потсистем во `st.expander`, називот е `label_mk`
- секој симптом е `st.checkbox` со `label_mk`, `help` од `description_mk` и стабилен `key` од идентификаторот

### Тек на настани

Копче „Дијагностицирај“.

- ако ништо не е избрано, `st.warning` со „Избери барем еден симптом.“ и не повикувај `diagnose`; избриши го претходниот резултат од `st.session_state`
- ако има избор, повикај `diagnose` со идентификаторите по редот на каталогот и зачувај го резултатот заедно со точната торка идентификатори
- по повторен rerun, ако изборот е ист, покажи го зачуваниот резултат; ако изборот е сменет, не покажувај стари картички, туку реченица „Изборот е сменет. Притисни Дијагностицирај повторно.“
- `UnknownSymptomError` станува `st.error`: „Симптомот „{id}“ не постои во базата на знаење.“

Не воведувај `st.form`, сесија за секое поле, ниту сопствен state објект надвор од тие две вредности.

### Резултат

- нема дијагнози: „Нема доволно совпаѓање со познатите дефекти.“ и листа на избраните називи
- секоја дијагноза е блок со `fault.name_mk`, статус „Потврдена“ или „Можна“, и резултат во цели проценти преку `int(score * 100 + 0.5)`
- под називот, `fault.summary_mk`
- објаснувањата од `matches` по редот на трагата, како одделни реченици
- препораките од rule match ставките што имаат препораки, еднаш, по тој редослед, како листа
- `st.expander` „Како се дојде до заклучокот“ ги покажува, за секој match, називите што се совпаднати, што недостасуваат и што се противречни; ако листата е празна, не ја пишувај таа реченица

Не прикажувај англиски идентификатори на корисникот. Не прикажувај факт како дефект; фактот се појавува само внатре во трагата, со својот македонски назив.

## Проверка

Пушти `streamlit run app.py` и помини го овој тек:

- празно копче дава предупредување
- `Не свети индикаторот за напојување`, `Вентилаторите не се вртат`, `Напојувањето кликнува и се гаси` дава потврдена дијагноза „Неисправно напојување“ и трага што го споменува и мртвиот пат на струја
- само `Долго бутање со активен диск` дава две можни дијагнози, прво оштетен датотечен систем
- смена на изборот без ново копче не остава стара дијагноза на екранот

Поправи го она што не го држи тој тек. Запри го серверот пред крај.

## Критериуми за прифаќање

- UI увезува само composition и доменски типови што му требаат за приказ, не repository и не PyYAML.
- Има празна состојба, состојба без совпаѓање и состојба со ранг, објаснување и препораки.
- Текстот на екранот е на македонски.
- Формулата не е препишана во UI.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Нема најава, историја на дијагнози, уредувач на правила, графикони, втор екран, ниту сопствен CSS рамковен систем. Не ги менувај `prompts/`, правилата и YAML, освен ако проверката открие погрешен македонски назив; тогаш поправи го само називот.

---

# Фаза 06 — Тестови

Копирај го целиот овој фајл во нов агентски разговор. Покриј ја машината и базата со pytest. Не тестирај виџети и не менувај го екранот за да биде полесен за тест.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом.

Фазите 01–05 го имаат системот: YAML каталог, forward chaining и Streamlit. Прочитај ги architecture правилото, `inference/engine.py` и `knowledge/computer_faults.yaml`. Тестовите ја штитат формулата, не ја прераскажуваат.

## Што веќе постои

Работените примери од фазата 04 се договорот. Каталогот има 8 потсистеми, 34 симптоми, 16 дефекти, 2 факти и 25 правила. `DiagnoseComputer` за празен избор не повикува `infer`.

## Што да напишеш

Три фајла, и ништо повеќе:

- `tests/test_repository.py`
- `tests/test_inference.py`
- `tests/test_diagnose.py`

Користи го pytest што е веќе dev зависност. Не додавај coverage, snapshot, ниту pytest додаток.

Заедничко: споредувај score со `pytest.approx`. Статусите споредувај ги со `DiagnosisStatus`. Редоследот на дијагнозите и на `rule_id` во трагата е дел од тврдењето.

### Репозиториум

Вчитај го вистинскиот `knowledge/computer_faults.yaml` преку `YamlKnowledgeRepository` и патот од коренот на репозиториумот.

- броевите се 8, 34, 16, 2 и 25
- `rule_faulty_psu` заклучува дефект `faulty_psu` и во `when_present` го има фактот `power_path_dead`

Со привремен YAML во `tmp_path`, очекувај `KnowledgeBaseError` за:

- повторен идентификатор на симптом
- услов што не е ниту симптом ниту факт
- правило што во `when_present` го наведува сопствениот факт

Не копирај го целиот каталог во тестот. За негативните случаи доволен е најмал YAML со еден потсистем и правилата што ја предизвикуваат грешката.

### Машина

Вистинската база, преку composition или репозиториум со апсолутен пат:

1. `no_power_led`, `no_fans`, `psu_clicks` → една дијагноза `faulty_psu`, `confirmed`, score 1. Трага: `rule_power_path_dead`, па `rule_faulty_psu`.
2. `thermal_shutdown`, `loud_fans_hot`, `no_fans` → `overheating`, `partial`, score `2/3`. Нема `confirmed`.
3. само `slow_boot_disk` → прво `corrupted_filesystem` со `2/3`, потоа `failing_disk` со `0.5`, двата `partial`. Трагата на дискот е `rule_failing_disk`, па `rule_smart_disk`.
4. `clicking_disk`, `slow_boot_disk`, `smart_warning`, `high_cpu_idle` → прво `background_cpu_load`, па `failing_disk`, двата `confirmed`. Трагата на дискот ги содржи `rule_failing_disk` и `rule_smart_disk`.
5. празен `Evidence` → нема дијагнози и нема исклучок.
6. `not_a_symptom` → `UnknownSymptomError` со тој `symptom_id`.

Еден тест со лажен репозиториум во истиот фајл, не во производствен модул. Лажната база има еден факт, еден дефект и две правила: правилото за фактот се активира од еден симптом, правилото за дефектот го бара тој факт и уште еден симптом. Со двата симптоми, дијагнозата е `confirmed`, а трагата го има правилото за фактот пред правилото за дефектот. Со ова машината докажува дека чита преку `KnowledgeRepository`, не преку глобален YAML.

### Use case

Лажен engine во тест-фајлот:

- `diagnose(())` и `diagnose([])` враќаат празен резултат, а `infer` не е повикан
- `diagnose` со идентификатори ги предава на `infer` како `Evidence`
- ако лажниот engine фрли `UnknownSymptomError`, `diagnose` не го голта

Не пуштај Streamlit и не го увезувај `streamlit` во тестовите.

## Начин на работа

- Пушти `pytest`. Поправи го производството само ако тестот открие вистинско отстапување од формулата. Не ја менувај формулата за да помине тест напишан спротивно на овие случаи.
- Ако некој случај покаже дека фазата 04 оставила друг редослед, исправи ја машината, не очекувањето.
- Не додавај тест за секое од 25-те правила.

## Критериуми за прифаќање

- `pytest` поминува.
- Тестовите не отвораат мрежа и не зависат од тековниот работен директориум.
- Нема `tests/fakes.py`, ниту тест за CSS и копчиња.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не го слабеј тврдењето со `score > 0`. Не бриши случај затоа што не поминува. Не ги менувај `prompts/` и `.cursor/rules`.

---

# Фаза 07 — Дијаграми

Копирај го целиот овој фајл во нов агентски разговор. Нацртај го системот што постои. Не додавај компоненти за да изгледа дијаграмот поцелосен и не менувај код за да личи на дијаграм.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом.

Упатството бара конечна верзија на use case сценарио и use case дијаграм, компонентен дијаграм со интеграциските интерфејси и секвенциски дијаграми за текот на настаните. Фазите 01–06 веќе го имаат кодот и тестовите. Прочитај ги `composition.py`, `diagnose.py`, `engine.py`, `repository.py` и `streamlit_app.py` пред да црташ. Имињата на дијаграмот се имињата од кодот.

## Што да напишеш

Три markdown фајла со Mermaid. Текстот околу дијаграмот е на македонски. Не извезувај слики и не воведувај PlantUML.

### `docs/diagrams/use-case.md`

Актор е корисникот што го пушта системот за да дознае дефект. Use case случаи:

- избира симптоми
- поставува дијагноза
- ја чита трагата на заклучување
- ги чита препорачаните проверки

Напиши го главното сценарио во нумерирани чекори: отворање, избор по потсистем, копче „Дијагностицирај“, рангирани дијагнози, објаснување и препораки. Потоа две продолженија, исто нумерирани: ниту еден симптом не е избран; ниту едно правило не го достигнува прагот 0,5. Mermaid дијаграмот го поврзува акторот со тие случаи. Не цртај администратор, најава, ниту уредување на правила.

### `docs/diagrams/component.md`

Компоненти што постојат, и само тие:

- `app.py`
- `streamlit_app`
- `composition`
- `DiagnoseComputer`
- `ForwardChainingEngine`
- `YamlKnowledgeRepository`
- `knowledge/computer_faults.yaml`

На секоја врска напиши го интеграцискиот интерфејс, со вистинскиот метод:

- екранот го повикува `catalog() -> KnowledgeBase` и `diagnose(selected_symptom_ids) -> DiagnosisResult`
- use case ги повикува `catalog` и `infer(evidence: Evidence) -> DiagnosisResult`
- машината повикува `load() -> KnowledgeBase`
- репозиториумот го чита YAML фајлот

Во пасус под дијаграмот кажи дека `composition.py` ги создава конкретните класи, а екранот не го познава engine ниту репозиториумот. Тоа е границата што дијаграмот мора да се гледа.

### `docs/diagrams/sequence.md`

Два секвенциски дијаграми.

Првиот е успешна дијагноза со синџир. Учесници: Корисник, `streamlit_app`, `DiagnoseComputer`, `ForwardChainingEngine`, `YamlKnowledgeRepository`. Тек: `catalog`, избор на `no_power_led`, `no_fans` и `psu_clicks`, `diagnose`, `infer`, `load`, активирање на `rule_power_path_dead`, па `rule_faulty_psu`, враќање на потврдена дијагноза „Неисправно напојување“.

Вториот е празен избор. Корисникот притиска „Дијагностицирај“ без симптом. Екранот покажува предупредување и не стигнува повик до `DiagnoseComputer`. Нацртај го тоа како порака што застанува на екранот, не како повик што враќа празен резултат.

## Начин на работа

- Провери дали секој метод од стрелките постои во кодот со тој потпис. Ако потписот во код е поинаков, дијаграмот го следи кодот, а овој промпт само го кажува намерата.
- Не вметнувај ги дијаграмите во извештајот овде. Тоа е фаза 08.
- Не додавај легенда што ги повторува стрелките една по една.

## Критериуми за прифаќање

- Трите фајла постојат и Mermaid блоковите се затворени.
- Се гледаат use case сценариото, компонентите со интерфејсите и двата тека на настани.
- Нема компонента за база на податоци, модел за машинско учење или корисничка сметка.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не прецртувај го кодот. Не додавај дијаграм за распоредување, класи или состојби. Не ги менувај `prompts/` и `.cursor/rules`.

---

# Фаза 08 — Технички извештај

Копирај го целиот овој фајл во нов агентски разговор. Напиши го извештајот според вистинскиот систем. Не измислувај функции, броеви или трудови.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом. Ова е писмениот дел од програмската опција: функционалната апликација веќе постои, извештајот ја придружува.

Прочитај го кодот, `knowledge/computer_faults.yaml`, тестовите и `docs/diagrams/` пред да пишуваш. Ако дијаграмите не се совпаѓаат со кодот, поправи ги дијаграмите, па цитирај ја исправената верзија.

## Структура

Еден фајл: `docs/report/izvestaj.md`. Јазик: македонски. Поглавја и подсекции токму вака:

1. Вовед
   - 1.1 Проблем
   - 1.2 Цел
   - 1.3 Опсег
2. Главен дел
   - 2.1 Опис на апликацијата
   - 2.2 Use case сценарио и use case дијаграм
   - 2.3 Компонентен дијаграм и интеграциски интерфејси
   - 2.4 Секвенциски дијаграми
   - 2.5 База на знаење и правила
   - 2.6 Inference engine
   - 2.7 Резултати: влезови и излези
3. Заклучок
4. Референци

Воведниот проблем е практичен: корисникот гледа симптоми, а не знае кој дефект е поверојатен ниту зошто. Целта е систем базиран на знаење што од симптоми дава рангирана дијагноза и објаснување. Опсегот ги кажува границите: еден компјутер, правила во YAML, без мерење на вистински хардвер, без машинско учење и без база.

Во 2.1 кажи што прави апликацијата од екранот до фајлот со знаење, со имињата на класите. Во 2.2 и 2.4 вгради ги Mermaid дијаграмите од `docs/diagrams/` и препиши го сценариото така што извештајот се чита и без отворање на другите фајлови. Во 2.3 наведи ги интерфејсите со потписите `catalog`, `diagnose`, `infer` и `load`.

Во 2.5 објасни го обликот на правилото: `when_present`, `when_absent`, заклучок што е факт или дефект, објаснување и препораки. Наведи ги вистинските броеви од каталогот. Опиши го синџирот `no_power_led` + `no_fans` → факт `power_path_dead` → `faulty_psu` кога има и `psu_clicks`. Не лепи ја целата YAML содржина.

Во 2.6 напиши ја формулата со зборови и со `score = исполнети услови / сите услови`. Кажи го прагот 0,5, разликата меѓу потврдена и можна дијагноза, и дека факт влегува во работната меморија само при целосно активирано правило. Еден краток пресметан пример: `thermal_shutdown`, `loud_fans_hot` и `no_fans` даваат 2/3 и можна, не потврдена, дијагноза за прегревање.

Во 2.7 биди конкретен. Влез: нула или повеќе симптоми од каталогот, избрани од корисникот. Излез: празно предупредување, порака дека нема доволно совпаѓање, или рангирана листа. За секоја дијагноза излезот носи назив, резиме, статус, процент, објаснување, препораки и трага. Кажи што се случува со непознат идентификатор.

Заклучокот кажува што системот го покажува на одбрана и една вистинска граница, на пример дека знаењето покрива чести дефекти, а не секој можен квар. Не ветувај следна верзија со невронска мрежа.

## Референци

Најмалку пет извори. Секој е проверен: отвори го URL-то и прочитај ја годината од самата страница. Годината е 2021 или понова. Исклучок само за врвно високо цитирано дело, со една реченица зошто правилото за годините не држи за него.

Барај по теми што навистина ја носат задачата: експертски систем за дијагностика на дефекти, forward chaining, објаснување на правила, официјална документација за Python dataclasses или typing.Protocol, Streamlit и PyYAML. Не ја полни листата со неповрзани трудови.

Формат на секоја ставка, како што бара упатството:

```text
Автори или организација. Наслов. Издавач или место, година. URL. Пристапено: датум.
Причина: една реченица зошто изворот е употребен во овој проект.
```

Пример од упатството е само пример за форма. Не го ставај тој труд за приватност во е-здравство, тој не е извор на овој проект.

Ако изворот не се отвора или годината не може да се утврди, не го наведувај. Не составувај автор, DOI или наслов по паметење.

## Начин на работа

- Пишувај конкретно. Пасус што само го повторува насловот избриши го.
- Не преведувај ги имињата на класите.
- Не додавај насловна страница, жив колонтитул, ниту втор формат. Markdown е документот.
- Не пишувај слајдови.

## Критериуми за прифаќање

- Постојат Вовед, Главен дел, Заклучок и Референци.
- Главниот дел ги има сите седум подсекции и вградените дијаграми.
- Влезовите и излезите се опишани така што читателот знае што се пишува и што се добива.
- Секоја референца има наслов, автор, URL, датум на пристап и причина. Нема непроверена ставка.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не измислувај мерења, точност во проценти или корисничка студија. Не ја менувај формулата во текстот за да звучи понаучно. Не ги менувај `prompts/` и `.cursor/rules`.

---

# Фаза 09 — README и документација

Копирај го целиот овој фајл во нов агентски разговор. Документирај го готовиот систем. Не додавај функции за да има што да се документира.

## Контекст

Предмет: Системи базирани на знаење, проф. Наташа Табаковска. Студент: Никола Христовски, ИНКИ961. Тема 4: дијагностика на дефект кај компјутер според симптом.

Фазите 01–08 го имаат кодот, тестовите, дијаграмите и `docs/report/izvestaj.md`. Во коренот сè уште може да стои индексот на промптовите. Оваа фаза го заменува со README на апликацијата. Промптовите во `prompts/` остануваат.

Прочитај ги `pyproject.toml`, `composition.py`, `engine.py` и извештајот, за README да не ветува нешто што кодот го нема.

## Docker

Додај еден `Dockerfile` на Python 3.11. Сликата го инсталира пакетот и ја пушта `streamlit run app.py` на порта 8501. Нема база на податоци и нема Compose: правилата се верзионираат во `knowledge/computer_faults.yaml`, не во табела.

## README

Замени го кореновиот `README.md`. Јазик: македонски, имињата на командите и класите на англиски. Делови:

- што е системот: експертски систем што од симптоми на компјутер дава рангирана дијагноза, објаснување и проверки
- една реченица за предметот, студентот и индексот ИНКИ961
- како се пушта: Python 3.11, виртуелна околина, `pip install -e ".[dev]"`, `pytest`, `streamlit run app.py`
- влез и излез: избрани симптоми; предупредување, нема совпаѓање, или листа со назив, статус, процент, објаснување, препораки и трага
- каде е знаењето: `knowledge/computer_faults.yaml`; ново правило се додава таму, не во Python
- дрво на проектот, кратко, само папките што постојат и по една реченица зошто постојат
- каде се извештајот и дијаграмите
- една реченица дека фазите се во `prompts/` и во `PROMPTS.md`

Не копирај го извештајот во README. Не наведувај тајна или услуга што проектот ја нема. Портата 8501 се споменува само кај Docker.

## Docstring

Краток docstring, на англиски, само на јавните граници:

- `KnowledgeRepository.load`
- `YamlKnowledgeRepository`, вклучително дека секој `load` го чита фајлот одново
- `InferenceEngine.catalog` и `InferenceEngine.infer`
- класата `ForwardChainingEngine`: формулата, прагот и дека факт влегува во меморијата само при score 1
- `DiagnoseComputer.diagnose`: празен избор не повикува `infer`

Не документирај го секое поле на dataclass. Не додавај коментар што го повторува името на методот. Ако некој од овие docstring веќе постои и е точен, остави го.

Празните `__init__.py` нека добијат по една реченица што е пакетот. Без реекспорт.

## Проверка

Од чиста виртуелна околина изврши ги командите од README: инсталација, `pytest` и кревање на `streamlit run app.py` додека страницата не одговори. Поправи го README ако некоја команда е погрешна. Запри го серверот.

Ако тестот падне, поправи ја причината само кога е очигледен прекин од претходна фаза. Не отворај нова функција.

## Критериуми за прифаќање

- Нов читател може да го инсталира проектот, да ги пушти тестовите и да го отвори екранот само со README.
- README не противречи на извештајот.
- Docstring постои на наведените граници и на ниту едно друго место „за секој случај“.
- `prompts/` не е изменет.


## Комитирање

Само `main`. По секој логичен рез направи посебен commit со кратка англиска порака во наредно време. Не собирај ја фазата во еден commit и не отворај друга гранка. Пораките за оваа фаза се наведени во фазата 00. На крај пушти `git push github main`. Не комитирај `.venv`, `__pycache__` или тајни.

## Забрани

Не пишувај Sphinx, MkDocs, API сајт, ниту англиски превод на извештајот. Не ги менувај `.cursor/rules` и фајловите во `prompts/`.
