# Дијагностика на дефект кај компјутер

Експертски систем што од симптоми на компјутер дава рангирана дијагноза, објаснување кое правило се активирало и проверки што треба да се направат.

Проектна задача по Системи базирани на знаење, Никола Христовски, ИНКИ961.

## Пуштање

Потребен е Python 3.11 или понов.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
streamlit run app.py
```

Истата апликација се пушта и од една слика, без Compose и без база:

```bash
docker build -t pc-fault-diagnosis .
docker run --rm -p 8501:8501 pc-fault-diagnosis
```

Потоа отвори `http://127.0.0.1:8501`.

## Објавување (Streamlit Community Cloud)

Оваа апликација е Streamlit — не се хостира на Vercel. Најлесно е [Streamlit Community Cloud](https://share.streamlit.io/):

1. Push на GitHub (`origin/main`).
2. На share.streamlit.io: **Create app** → избери го repo-то → **Main file path:** `app.py` → **Deploy**.

Cloud автоматски го користи `requirements.txt` и `knowledge/computer_faults.yaml` од root на repo-то.

Алтернатива: **Render** со `render.yaml` и постоечкиот `Dockerfile` (Web Service → Blueprint).

## Влез и излез

Влез се симптомите што корисникот ги штиклира по потсистем, или примерен случај што ги штиклира без да постави дијагноза. Ако ништо не е избрано, екранот предупредува да се избере барем еден. Ако правилата не го достигнуваат прагот, јавува дека нема доволно совпаѓање. Инаку враќа рангирани картички со назив, статус, процент, објаснување, препораки и трага. „Исчисти“ го брише изборот и резултатот.

## Знаење

Правилата се во `knowledge/computer_faults.yaml`. Ново правило се додава таму, не во Python.

## Структура

- `src/pc_fault_diagnosis/domain` ги држи симптомите, правилата и резултатот
- `src/pc_fault_diagnosis/knowledge` ја чита YAML датотеката
- `src/pc_fault_diagnosis/inference` ги пали правилата
- `src/pc_fault_diagnosis/application` го врзува изборот со дијагнозата
- `src/pc_fault_diagnosis/ui` е само екранот
- `src/pc_fault_diagnosis/composition.py` ги составува конкретните класи
- `docs/report/izvestaj.md` е извештајот, а `docs/diagrams` ги држи дијаграмите
- `tests` ја покриваат базата и машината, не виџетите

Фазите со кои е воден проектот се во `prompts/` и во `PROMPTS.md`.
