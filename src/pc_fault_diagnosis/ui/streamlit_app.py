import streamlit as st

from pc_fault_diagnosis.composition import build_diagnose_computer
from pc_fault_diagnosis.domain.errors import KnowledgeBaseError, UnknownSymptomError
from pc_fault_diagnosis.domain.models import DiagnosisResult, DiagnosisStatus, KnowledgeBase, Symptom

_STATUS_LABELS = {
    DiagnosisStatus.CONFIRMED: "Потврдена",
    DiagnosisStatus.PARTIAL: "Можна",
}


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

    if "diagnosis" not in st.session_state:
        st.session_state.diagnosis = None
        st.session_state.diagnosed_ids = ()

    labels = {symptom.id: symptom.label_mk for symptom in catalog.symptoms}
    choice, result = st.columns(2)
    with choice:
        selected = _symptom_picker(catalog)
        if st.button("Дијагностицирај"):
            _diagnose(computer, selected)
    with result:
        _show_result(selected, labels)


def _symptom_picker(catalog: KnowledgeBase) -> list[str]:
    grouped: dict[str, list[Symptom]] = {subsystem.id: [] for subsystem in catalog.subsystems}
    for symptom in catalog.symptoms:
        grouped.setdefault(symptom.subsystem_id, []).append(symptom)

    selected: list[str] = []
    for subsystem in catalog.subsystems:
        with st.expander(subsystem.label_mk):
            for symptom in grouped.get(subsystem.id, []):
                checked = st.checkbox(
                    symptom.label_mk,
                    help=symptom.description_mk,
                    key=f"symptom-{symptom.id}",
                )
                if checked:
                    selected.append(symptom.id)
    return selected


def _diagnose(computer, selected: list[str]) -> None:
    if not selected:
        st.session_state.diagnosis = None
        st.session_state.diagnosed_ids = ()
        st.warning("Избери барем еден симптом.")
        return
    try:
        st.session_state.diagnosis = computer.diagnose(selected)
        st.session_state.diagnosed_ids = tuple(selected)
    except UnknownSymptomError as error:
        st.session_state.diagnosis = None
        st.session_state.diagnosed_ids = ()
        st.error(f"Симптомот „{error.symptom_id}“ не постои во базата на знаење.")


def _show_result(selected: list[str], labels: dict[str, str]) -> None:
    diagnosis = st.session_state.diagnosis
    if diagnosis is None:
        return
    if tuple(selected) != st.session_state.diagnosed_ids:
        st.write("Изборот е сменет. Притисни Дијагностицирај повторно.")
        return
    _render_diagnosis(diagnosis, labels)


def _render_diagnosis(result: DiagnosisResult, labels: dict[str, str]) -> None:
    if not result.diagnoses:
        st.write("Нема доволно совпаѓање со познатите дефекти.")
        for symptom_id in st.session_state.diagnosed_ids:
            st.write(labels.get(symptom_id, symptom_id))
        return

    for diagnosis in result.diagnoses:
        percent = int(diagnosis.score * 100 + 0.5)
        st.subheader(diagnosis.fault.name_mk)
        st.write(f"{_STATUS_LABELS[diagnosis.status]} · {percent}%")
        st.write(diagnosis.fault.summary_mk)
        for match in diagnosis.matches:
            st.write(match.explanation_mk)
        recommendations = []
        for match in diagnosis.matches:
            for recommendation in match.recommendations_mk:
                if recommendation not in recommendations:
                    recommendations.append(recommendation)
        if recommendations:
            st.markdown("\n".join(f"- {item}" for item in recommendations))
        with st.expander("Како се дојде до заклучокот"):
            for match in diagnosis.matches:
                _write_items("Совпаднати", match.matched)
                _write_items("Недостасуваат", match.missing)
                _write_items("Противречни", match.contradicted)


def _write_items(title: str, items) -> None:
    if not items:
        return
    names = ", ".join(item.label_mk for item in items)
    st.write(f"{title}: {names}")
