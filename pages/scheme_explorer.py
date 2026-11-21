import streamlit as st
from database.scheme_repository import SchemeRepository
from services.i18n import t


def render():
    st.markdown(f'<span class="eyebrow">{t("explorer")}</span><h1>{t("explorer_title")}</h1>', unsafe_allow_html=True)
    schemes = SchemeRepository().get_all()
    c1,c2,c3 = st.columns(3)
    search = c1.text_input("Search scheme name")
    category = c2.selectbox("Category", ["All","Agriculture","Education","Healthcare","Employment","Women & Child","Business","Housing","Financial Inclusion","Social Welfare","Senior Citizens","Disability Support"],
                            index=(["All","Agriculture","Education","Healthcare","Employment","Women & Child","Business","Housing","Financial Inclusion","Social Welfare","Senior Citizens","Disability Support"].index(st.session_state.get("explorer_category","All")) if st.session_state.get("explorer_category","All") in ["All","Agriculture","Education","Healthcare","Employment","Women & Child","Business","Housing","Financial Inclusion","Social Welfare","Senior Citizens","Disability Support"] else 0))
    state = c3.selectbox("State", ["All","Tamil Nadu","All India"])

    st.markdown('<div class="source-note">Demonstration records are included for interface and matching tests. Verify every benefit and condition on the official source before applying.</div>', unsafe_allow_html=True)
    filtered = []
    for scheme in schemes:
        if search and search.lower() not in scheme["scheme_name"].lower():
            continue
        if category != "All" and scheme["category"] != category:
            continue
        states = scheme.get("eligible_states") or []
        if state == "Tamil Nadu" and states and "Tamil Nadu" not in states:
            continue
        if state == "All India" and states:
            continue
        filtered.append(scheme)

    st.write(f"**{len(filtered)} schemes**")
    for scheme in filtered:
        st.markdown(f'<div class="scheme-card"><span class="status status-info">{scheme["category"]}</span><h3>{scheme["scheme_name"]}</h3><p>{scheme["description"]}</p><p><strong>Department:</strong> {scheme.get("government_department","Not listed")}</p></div>', unsafe_allow_html=True)
        a,b = st.columns(2)
        if a.button("View Details", key=f"exp_{scheme['scheme_id']}"):
            st.session_state.selected_scheme = scheme["scheme_id"]
            st.session_state.page = "details"; st.rerun()
        if b.button("Save Scheme", key=f"exp_save_{scheme['scheme_id']}"):
            st.session_state.saved_schemes = set(st.session_state.get("saved_schemes", set())) | {scheme["scheme_id"]}
            st.success("Saved.")
