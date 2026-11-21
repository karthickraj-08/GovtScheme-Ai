import streamlit as st


def privacy():
    st.markdown('<span class="eyebrow">PRIVACY & DISCLAIMER</span><h1>Privacy and Disclaimer</h1>', unsafe_allow_html=True)
    st.markdown("""
SchemeFinder AI is an independent scheme discovery platform and is not affiliated with any government department.
Eligibility information is indicative. Final eligibility and approval are determined by the respective government authority.

**Privacy:** Profile details are retained only in session state unless MongoDB is configured. Uploaded documents are
processed only after consent and are not permanently stored by default. API keys and database credentials must be kept
in environment variables or Streamlit secrets.
""")


def render():
    st.markdown('<span class="eyebrow">ABOUT</span><h1>SchemeFinder AI</h1>', unsafe_allow_html=True)
    st.write("SchemeFinder AI helps Indian citizens discover relevant Central and Tamil Nadu government opportunities. It combines transparent, rule-based initial matching with optional Gemini assistance for structured extraction and explanations.")
    st.markdown("## How decisions work")
    st.write("The deterministic eligibility engine determines matching status. Gemini may structure or explain information, but never approves or rejects eligibility.")
    st.markdown("## Official sources")
    for name, url in [
        ("MyScheme","https://www.myscheme.gov.in/"),("India.gov.in","https://www.india.gov.in/"),
        ("Tamil Nadu Government","https://www.tn.gov.in/"),("Data.gov.in","https://www.data.gov.in/")
    ]:
        st.markdown(f"- [{name}]({url})")
