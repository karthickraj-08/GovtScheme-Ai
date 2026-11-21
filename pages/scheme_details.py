import streamlit as st
from database.scheme_repository import SchemeRepository


def render():
    scheme_id = st.session_state.get("selected_scheme")
    scheme = SchemeRepository().get_by_id(scheme_id)
    if not scheme:
        st.warning("Select a scheme to view details.")
        return
    st.markdown(f'<span class="eyebrow">{scheme["category"]}</span><h1>{scheme["scheme_name"]}</h1>', unsafe_allow_html=True)
    st.markdown('<div class="source-note"><strong>Important:</strong> Demonstration summary. Verify eligibility and application requirements on the official source.</div>', unsafe_allow_html=True)
    st.markdown("## Overview")
    st.write(scheme["description"])
    st.markdown("## Benefits")
    for benefit in scheme.get("benefits") or []:
        st.write("- " + benefit)
    st.markdown("## Eligibility criteria")
    if scheme.get("eligible_states"):
        st.write("- States: " + ", ".join(scheme["eligible_states"]))
    if scheme.get("min_age") is not None:
        st.write("- Minimum age: " + str(scheme["min_age"]))
    if scheme.get("max_age") is not None:
        st.write("- Maximum age: " + str(scheme["max_age"]))
    for rule in scheme.get("other_eligibility_rules") or []:
        st.write("- " + rule)
    if not (scheme.get("other_eligibility_rules") or scheme.get("min_age") or scheme.get("max_age") or scheme.get("eligible_states")):
        st.write("Specific eligibility is not complete in this demonstration record.")

    st.markdown("## Documents")
    c1,c2 = st.columns(2)
    with c1:
        st.write("**Required**")
        for item in scheme.get("required_documents") or []: st.write("- " + item)
    with c2:
        st.write("**Optional**")
        for item in scheme.get("optional_documents") or []: st.write("- " + item)

    st.markdown("## Application guidance")
    for i, step in enumerate(scheme.get("application_steps") or [], 1):
        st.write(f"{i}. {step}")
    st.markdown("## Source")
    st.write(f"**Source:** {scheme.get('source_name','Official source not listed')}")
    st.write(f"**Last verification date:** {scheme.get('last_verified_at','Not verified')}")
    st.write(f"**Verification status:** {scheme.get('verification_status','unverified')}")
    if scheme.get("official_scheme_url"):
        st.link_button("View Official Scheme Website", scheme["official_scheme_url"])
    if scheme.get("application_url"):
        st.link_button("Apply on Official Website", scheme["application_url"])
