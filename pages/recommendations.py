import streamlit as st
from database.scheme_repository import SchemeRepository
from services.recommendation_service import recommendations_for
from services.i18n import t


def render():
    profile = st.session_state.get("profile")
    if not profile:
        st.warning(t("recommendation_profile_warning"))
        if st.button(t("go_profile"), type="primary"):
            st.session_state.page = "find"; st.rerun()
        return

    schemes = SchemeRepository().get_all()
    recommendations = recommendations_for(profile, schemes)
    st.markdown(f'<span class="eyebrow">{t("assessment")}</span><h1>{t("recommended_title")}</h1>', unsafe_allow_html=True)
    st.info(t("assessment_hint"))

    filter_status = st.pills("Status", ["All","Potentially Eligible","Needs More Information","Not Matching"], default="All")
    c1,c2 = st.columns([2,1])
    search = c1.text_input("Search schemes")
    category = c2.selectbox("Category", ["All"] + sorted(set(s["category"] for s in schemes)))
    scheme_map = {s["scheme_id"]: s for s in schemes}
    visible_count = 0

    for rec in recommendations:
        scheme = scheme_map.get(rec.scheme_id)
        if not scheme:
            continue
        if filter_status != "All" and rec.status != filter_status:
            continue
        if search and search.lower() not in scheme["scheme_name"].lower():
            continue
        if category != "All" and scheme["category"] != category:
            continue
        visible_count += 1
        css = "status-potential" if rec.status == "Potentially Eligible" else ("status-info" if rec.status == "Needs More Information" else "status-fail")
        st.markdown(f'<div class="scheme-card"><span class="status {css}">{rec.status}</span><h3 style="margin:.5rem 0">{scheme["scheme_name"]}</h3><p>{scheme["description"]}</p>', unsafe_allow_html=True)
        st.caption(f'{scheme["category"]} | {scheme.get("government_department","")} | Relevance: {rec.score}')
        if rec.matching_reasons:
            st.write("**Why it may match:** " + "; ".join(rec.matching_reasons))
        if rec.missing_information:
            st.write("**Needs more information:** " + ", ".join(rec.missing_information))
        if rec.failed_conditions:
            st.write("**Conditions that do not match:** " + "; ".join(rec.failed_conditions))
        a,b,c,d = st.columns(4)
        if a.button("View Details", key=f"details_{rec.scheme_id}"):
            st.session_state.selected_scheme = rec.scheme_id
            st.session_state.page = "details"; st.rerun()
        if b.button("Document Checklist", key=f"docs_{rec.scheme_id}"):
            st.session_state.selected_scheme = rec.scheme_id
            st.session_state.page = "checklist"; st.rerun()
        if c.button("Save Scheme", key=f"save_{rec.scheme_id}"):
            st.session_state.saved_schemes = set(st.session_state.get("saved_schemes", set())) | {rec.scheme_id}
            st.success("Saved.")
        if d.button("How to Apply", key=f"apply_{rec.scheme_id}"):
            st.session_state.selected_scheme = rec.scheme_id
            st.session_state.page = "details"
            st.rerun()
        if scheme.get("application_url"):
            st.link_button("Open Official Application Website", scheme["application_url"])
        st.markdown("</div>", unsafe_allow_html=True)
    if visible_count == 0:
        st.info("No schemes match these filters. Clear the status/category/search filters or add more profile details.")
