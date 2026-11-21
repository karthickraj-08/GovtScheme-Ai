import streamlit as st
from services.i18n import LANGUAGES, t, init_language


def navbar():
    init_language()
    st.markdown('<div class="nav-wrap"><div class="brand">SchemeFinder <span>AI</span></div></div>', unsafe_allow_html=True)
    language = st.selectbox(
        "Language / भाषा / மொழி",
        list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(st.session_state.language_name),
        key="language_selector",
        label_visibility="collapsed",
    )
    if language != st.session_state.language_name:
        st.session_state.language_name = language
        st.rerun()

    labels = [t("home"), t("explore"), t("how"), t("about"), t("find")]
    keys = ["home", "explore", "how", "about", "find"]
    cols = st.columns([1, 1, 1, 1, 1])
    for col, label, key in zip(cols, labels, keys):
        with col:
            if st.button(label, use_container_width=True, key=f"nav_{key}", type="primary" if key == "find" else "secondary"):
                st.session_state.page = key
                st.rerun()
