import streamlit as st
from database.scheme_repository import SchemeRepository


def render():
    scheme_id = st.session_state.get("selected_scheme")
    scheme = SchemeRepository().get_by_id(scheme_id)
    if not scheme:
        st.warning("Choose a scheme to build a document checklist.")
        return
    st.markdown(f'<span class="eyebrow">DOCUMENT CHECKLIST</span><h1>{scheme["scheme_name"]}</h1>', unsafe_allow_html=True)
    st.caption("A collected checklist item does not confirm that a document is valid or officially accepted.")
    key_items = []
    for item in scheme.get("required_documents") or []:
        key_items.append(("Required", item))
    for item in scheme.get("optional_documents") or []:
        key_items.append(("Optional", item))
    collected = 0
    for i, (kind, item) in enumerate(key_items):
        checked = st.checkbox(f"{kind}: {item}", key=f"doc_{scheme_id}_{i}")
        if checked: collected += 1
    progress = collected / max(1, len(key_items))
    st.progress(progress)
    st.write(f"**{collected} of {len(key_items)} checklist items marked collected**")
