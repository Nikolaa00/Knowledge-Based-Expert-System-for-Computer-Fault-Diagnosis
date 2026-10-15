import streamlit as st

from pc_fault_diagnosis.composition import build_diagnose_computer
from pc_fault_diagnosis.domain.errors import KnowledgeBaseError, UnknownSymptomError
from pc_fault_diagnosis.domain.models import DiagnosisResult, DiagnosisStatus, KnowledgeBase, Symptom

_STATUS_LABELS = {
    DiagnosisStatus.CONFIRMED: "Потврдена",
    DiagnosisStatus.PARTIAL: "Можна",
}

_SAMPLE_CASES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("Неисправно напојување", ("no_power_led", "no_fans", "psu_clicks")),
    ("Оштетен датотечен систем", ("slow_boot_disk",)),
    ("Прегревање", ("thermal_shutdown", "loud_fans_hot")),
    ("Неисправна меморија", ("no_post", "beeps_continuous", "memtest_errors")),
)


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
    all_ids = tuple(symptom.id for symptom in catalog.symptoms)
    choice, result = st.columns(2)
    with choice:
        _sample_cases(all_ids)
        selected = _symptom_picker(catalog)
        _show_selection(selected, labels)
        diagnose_col, clear_col = st.columns(2)
        with diagnose_col:
            diagnose_clicked = st.button("Дијагностицирај", use_container_width=True)
        with clear_col:
            st.button(
                "Исчисти",
                on_click=_clear_selection,
                args=(all_ids,),
                use_container_width=True,
            )
        if diagnose_clicked:
            _diagnose(computer, selected)
    with result:
        _show_result(selected, labels)


def _sample_cases(all_ids: tuple[str, ...]) -> None:
    with st.expander("Примерни случаи"):
        st.caption("Избери случај, па притисни Дијагностицирај.")
        for index, (label, symptom_ids) in enumerate(_SAMPLE_CASES):
            st.button(
                label,
                key=f"sample-{index}",
                on_click=_apply_sample,
                args=(symptom_ids, all_ids),
                use_container_width=True,
            )


def _apply_sample(symptom_ids: tuple[str, ...], all_ids: tuple[str, ...]) -> None:
    chosen = set(symptom_ids)
    for symptom_id in all_ids:
        st.session_state[f"symptom-{symptom_id}"] = symptom_id in chosen
    st.session_state.diagnosis = None
    st.session_state.diagnosed_ids = ()


def _clear_selection(all_ids: tuple[str, ...]) -> None:
    for symptom_id in all_ids:
        st.session_state[f"symptom-{symptom_id}"] = False
    st.session_state.diagnosis = None
    st.session_state.diagnosed_ids = ()


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


def _show_selection(selected: list[str], labels: dict[str, str]) -> None:
    st.write(f"Избрани симптоми: {len(selected)}")
    for symptom_id in selected:
        st.markdown(f"- {labels[symptom_id]}")


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
        st.info("Избери симптоми и притисни Дијагностицирај.")
        return
    if tuple(selected) != st.session_state.diagnosed_ids:
        st.write("Изборот е сменет. Притисни Дијагностицирај повторно.")
        return
    _render_diagnosis(diagnosis, labels)


def _render_diagnosis(result: DiagnosisResult, labels: dict[str, str]) -> None:
    if not result.diagnoses:
        st.write("Нема доволно совпаѓање со познатите дефекти.")
        for symptom_id in st.session_state.diagnosed_ids:
            st.markdown(f"- {labels[symptom_id]}")
        return

    for rank, diagnosis in enumerate(result.diagnoses, start=1):
        percent = _percent(diagnosis.score)
        with st.container(border=True):
            st.subheader(f"{rank}. {diagnosis.fault.name_mk}")
            st.write(f"{_STATUS_LABELS[diagnosis.status]} · {percent}%")
            st.progress(percent / 100)
            st.write(diagnosis.fault.summary_mk)
            for match in diagnosis.matches:
                st.write(match.explanation_mk)
            recommendations: list[str] = []
            for match in diagnosis.matches:
                for recommendation in match.recommendations_mk:
                    if recommendation not in recommendations:
                        recommendations.append(recommendation)
            if recommendations:
                st.markdown("**Препораки**")
                st.markdown("\n".join(f"- {item}" for item in recommendations))
            with st.expander("Како се дојде до заклучокот"):
                for match in diagnosis.matches:
                    st.write(match.explanation_mk)
                    st.write(f"{_percent(match.score)}%")
                    _write_items("Совпаднати", match.matched)
                    _write_items("Недостасуваат", match.missing)
                    _write_items("Противречни", match.contradicted)


def _percent(score: float) -> int:
    return int(score * 100 + 0.5)


def _write_items(title: str, items) -> None:
    if not items:
        return
    lines = "\n".join(f"- {item.label_mk}" for item in items)
    st.markdown(f"**{title}**\n\n{lines}")
