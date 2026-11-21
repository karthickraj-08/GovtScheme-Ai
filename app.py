import streamlit as st
from pathlib import Path

from components.navbar import navbar
from components.footer import footer
from pages.home import render as home
from pages.find_schemes import render as find_schemes
from pages.recommendations import render as recommendations
from pages.scheme_explorer import render as scheme_explorer
from pages.scheme_details import render as scheme_details
from pages.document_checklist import render as document_checklist
from pages.saved_schemes import render as saved_schemes
from pages.about import render as about, privacy

st.set_page_config(page_title="SchemeFinder AI", page_icon="🇮🇳", layout="wide")

css = Path("assets/styles.css")
if css.exists():
    st.markdown(f"<style>{css.read_text()}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

navbar()

with st.sidebar:
    st.markdown("### Account")
    for label, key in [("My Profile","find"),("Recommended Schemes","recommendations"),("Saved Schemes","saved"),("Privacy & Disclaimer","privacy")]:
        if st.button(label, use_container_width=True, key=f"side_{key}_{label}"):
            st.session_state.page = key
            st.rerun()

page = st.session_state.page
if page == "home":
    home()
elif page == "find":
    find_schemes()
elif page == "recommendations":
    recommendations()
elif page == "explore":
    scheme_explorer()
elif page == "details":
    scheme_details()
elif page == "checklist":
    document_checklist()
elif page == "saved":
    saved_schemes()
elif page == "about":
    about()
elif page == "privacy":
    privacy()

footer()
