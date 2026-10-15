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
