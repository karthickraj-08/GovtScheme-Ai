import streamlit as st
from database.scheme_repository import SchemeRepository
from services.i18n import t


def render():
    st.markdown(f'<span class="eyebrow">{t("shortlist")}</span><h1>{t("saved_title")}</h1>', unsafe_allow_html=True)
    ids = st.session_state.get("saved_schemes", set())
    if not ids:
        st.info("No saved schemes yet.")
        return
    for scheme in SchemeRepository().get_all():
        if scheme["scheme_id"] not in ids:
            continue
        st.markdown(f'<div class="scheme-card"><h3>{scheme["scheme_name"]}</h3><p>{scheme["description"]}</p></div>', unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        if c1.button("View Details", key=f"saved_view_{scheme['scheme_id']}"):
            st.session_state.selected_scheme = scheme["scheme_id"]; st.session_state.page="details"; st.rerun()
        if c2.button("Remove", key=f"saved_remove_{scheme['scheme_id']}"):
            ids.remove(scheme["scheme_id"])
            st.session_state.saved_schemes = set(ids)
            st.rerun()
