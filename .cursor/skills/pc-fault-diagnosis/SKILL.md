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
