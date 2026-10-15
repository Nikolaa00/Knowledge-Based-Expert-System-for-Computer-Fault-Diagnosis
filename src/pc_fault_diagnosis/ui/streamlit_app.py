import streamlit as st

from pc_fault_diagnosis.composition import build_diagnose_computer
from pc_fault_diagnosis.domain.errors import KnowledgeBaseError
from pc_fault_diagnosis.domain.models import KnowledgeBase


def main() -> None:
    st.set_page_config(page_title="Дијагностика на дефект кај компјутер", layout="wide")
    st.title("Дијагностика на дефект кај компјутер")
    st.write(
        "Избери ги симптомите што ги гледаш. Системот ги споредува со правилата "
        "и објаснува како дошол до дијагнозата."
    )
    try:
        computer = build_diagnose_computer()
        catalog = computer.catalog()
    except KnowledgeBaseError as error:
        st.error(str(error))
        return

    selected = _symptom_picker(catalog)
    if st.button("Дијагностицирај") and not selected:
        st.warning("Избери барем еден симптом.")


def _symptom_picker(catalog: KnowledgeBase) -> list[str]:
    grouped: dict[str, list] = {subsystem.id: [] for subsystem in catalog.subsystems}
    for symptom in catalog.symptoms:
        grouped.setdefault(symptom.subsystem_id, []).append(symptom)

    selected: list[str] = []
    for subsystem in catalog.subsystems:
        with st.expander(subsystem.label_mk):
            for symptom in grouped.get(subsystem.id, []):
                if st.checkbox(symptom.label_mk, help=symptom.description_mk, key=f"symptom-{symptom.id}"):
                    selected.append(symptom.id)
    return selected
