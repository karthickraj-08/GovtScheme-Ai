import streamlit as st
from services.i18n import t


def opportunity_card(title, icon, description, accent, icon_bg, category):
    st.markdown(f'<div class="op-card" style="--accent:{accent};--icon-bg:{icon_bg}"><div class="op-icon">{icon}</div><h3>{title}</h3><p style="color:#60758A">{description}</p></div>', unsafe_allow_html=True)
    if st.button(f"Explore {title}", key=f"op_{category}", use_container_width=True):
        st.session_state.explorer_category = category
        st.session_state.page = "explore"
        st.rerun()


def render():
    c1, c2 = st.columns([1.08, .92], gap="large")
    with c1:
        st.markdown('<span class="eyebrow">GOVERNMENT BENEFITS, MADE SIMPLE</span>', unsafe_allow_html=True)
        st.markdown(f'<h1 style="font-size:3.1rem;line-height:1.08">{t("hero_title")}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p>{t("hero_subtitle")}</p>', unsafe_allow_html=True)
        a, b, _ = st.columns([1, 1, 1.4])
        if a.button(t("find"), type="primary", use_container_width=True):
            st.session_state.page = "find"; st.rerun()
        if b.button(t("explore"), use_container_width=True):
            st.session_state.page = "explore"; st.rerun()
        st.caption(t("trust"))
    with c2:
        st.markdown('<div style="height:330px;border-radius:24px;background:linear-gradient(145deg,#EDF5FC,#FFF5EB);display:flex;align-items:center;justify-content:center;font-size:7rem">🇮🇳</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<center><span class="eyebrow">{t("opportunities")}</span><h2>{t("op_title")}</h2><p>{t("op_subtitle")}</p></center>', unsafe_allow_html=True)
    cards = [
        ("Agriculture","🌾","Support for farmers and rural communities","#168A35","#EDF7EE","Agriculture"),
        ("Education","🎓","Scholarships and student assistance","#FF8C24","#FFF4E8","Education"),
        ("Healthcare","🏥","Health protection and medical support","#3D82C4","#EDF5FC","Healthcare"),
        ("Employment","💼","Skills, jobs and livelihood opportunities","#7B61A8","#F3EFF8","Employment"),
        ("Women & Child","👩‍👧","Women empowerment and child welfare","#D95B87","#FCEEF4","Women & Child"),
    ]
    r1 = st.columns(3)
    r2 = st.columns([.5, 1, 1, 1, .5])
    for i, card in enumerate(cards):
        if i < 3:
            with r1[i]: opportunity_card(*card)
        else:
            with r2[i-2]: opportunity_card(*card)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<center><span class="eyebrow">{t("how")}</span><h2>{t("how_title")}</h2><p>{t("how_subtitle")}</p></center>', unsafe_allow_html=True)
    steps = st.columns(3)
    for col, (num, title, desc) in zip(steps, [
        ("01",t("step1"),t("step1_desc")),
        ("02",t("step2"),t("step2_desc")),
        ("03",t("step3"),t("step3_desc")),
    ]):
        with col:
            st.markdown(f'<div class="step-card"><div class="step-num">{num}</div><h3>{title}</h3><p style="color:#60758A">{desc}</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="cta"><span style="color:#FFB16A;font-weight:800;font-size:.75rem">SCHEMEFINDER AI</span><h2>{t("cta_title")}</h2><p>{t("cta_subtitle")}</p></div>', unsafe_allow_html=True)
    if st.button(t("find_cta"), type="primary"):
        st.session_state.page = "find"; st.rerun()
