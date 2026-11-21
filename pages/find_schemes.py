import streamlit as st
from models.profile import UserProfile
from database.profile_repository import ProfileRepository
from services.profile_extraction import ProfileExtractionService
from services.document_service import extract_document_text, normalize_document_text
from services.i18n import pt


STATES = [
    "Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar",
    "Chandigarh","Chhattisgarh","Dadra and Nagar Haveli and Daman and Diu","Delhi",
    "Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand",
    "Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra",
    "Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
    "Uttarakhand","West Bengal",
]

DISTRICTS_BY_STATE = {
    "Tamil Nadu": ["Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi","Kanchipuram","Kanyakumari","Karur","Krishnagiri","Madurai","Mayiladuthurai","Nagapattinam","Namakkal","Nilgiris","Perambalur","Pudukkottai","Ramanathapuram","Ranipet","Salem","Sivaganga","Tenkasi","Thanjavur","Theni","Thoothukudi","Tiruchirappalli","Tirunelveli","Tirupathur","Tiruppur","Tiruvallur","Tiruvannamalai","Tiruvarur","Vellore","Villupuram","Virudhunagar","Other"],
    "Kerala": ["Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad","Other"],
    "Karnataka": ["Bengaluru Urban","Bengaluru Rural","Belagavi","Ballari","Mysuru","Dakshina Kannada","Other"],
    "Andhra Pradesh": ["Anantapur","Chittoor","East Godavari","Guntur","Krishna","Kurnool","Nellore","Prakasam","Srikakulam","Visakhapatnam","Vizianagaram","West Godavari","YSR Kadapa","Other"],
    "Telangana": ["Adilabad","Hyderabad","Karimnagar","Khammam","Mahbubnagar","Medak","Nalgonda","Nizamabad","Ranga Reddy","Warangal","Other"],
    "Maharashtra": ["Mumbai City","Mumbai Suburban","Pune","Nagpur","Thane","Nashik","Aurangabad","Solapur","Kolhapur","Other"],
    "Delhi": ["Central Delhi","East Delhi","New Delhi","North Delhi","North East Delhi","North West Delhi","South Delhi","South East Delhi","South West Delhi","West Delhi","Other"],
}

INCOME_OPTIONS = [
    ("Not sure / Prefer not to say", None),
    ("Up to ₹1 lakh", 100000),
    ("₹1 lakh – ₹2.5 lakh", 250000),
    ("₹2.5 lakh – ₹5 lakh", 500000),
    ("₹5 lakh – ₹8 lakh", 800000),
    ("₹8 lakh – ₹10 lakh", 1000000),
    ("Above ₹10 lakh", 1000001),
]

EDUCATION_OPTIONS = ["Below 10th","10th pass","12th pass","ITI / Polytechnic","Undergraduate","Postgraduate","Diploma","Professional degree","Not applicable"]
EMPLOYMENT_OPTIONS = ["Student","Employed","Self-employed","Job seeker","Unemployed","Homemaker","Retired","Farmer","Other"]
OCCUPATION_OPTIONS = ["Student","Farmer","Business owner","Employee","Daily wage worker","Skilled worker","Professional","Homemaker","Self-employed","Job seeker","Retired","Other"]


def render():
    st.markdown(f'<span class="eyebrow">{pt("eyebrow")}</span><h1>{pt("title")}</h1>', unsafe_allow_html=True)
    st.caption(pt("hint"))
    gemini_service = ProfileExtractionService().gemini
    if gemini_service.enabled:
        st.success("Gemini AI is configured.")
    else:
        st.error(
            "Gemini AI is not configured yet. In Streamlit Cloud open "
            "Manage app > Settings > Secrets and set exactly: "
            "GEMINI_API_KEY = \"<your-key>\". Save and reboot the app."
        )

    existing = st.session_state.get("profile")
    def val(field, default=""):
        return getattr(existing, field, default) if existing else default

    beneficiary_options = ["Student","Farmer","Business Owner","Job Seeker","General Public","Other"]
    beneficiary_labels = {"Student":pt("student"),"Farmer":pt("farmer"),"Business Owner":pt("business"),"Job Seeker":pt("job"),"General Public":pt("general"),"Other":pt("other")}
    beneficiary = st.selectbox(pt("category"), beneficiary_options,
                               index=beneficiary_options.index(val("beneficiary_type","General Public")) if val("beneficiary_type","General Public") in beneficiary_options else 4,
                               format_func=lambda value: beneficiary_labels[value])
    c1,c2,c3 = st.columns(3)
    name = c1.text_input(pt("name"), val("name",""))
    age = c2.number_input(pt("age"), min_value=1, max_value=120, value=int(val("age") or 18))
    gender_options = ["Prefer not to say","Female","Male","Non-binary","Other"]
    gender_labels = {"Prefer not to say":pt("gender_hide"),"Female":pt("female"),"Male":pt("male"),"Non-binary":pt("other_gender"),"Other":pt("other_gender")}
    gender = c3.selectbox(pt("gender"), gender_options,
                          index=gender_options.index(val("gender","Prefer not to say")) if val("gender") in gender_options else 0,
                          format_func=lambda value: gender_labels[value])
    c1,c2,c3 = st.columns(3)
    existing_state = val("state","Tamil Nadu")
    state = c1.selectbox(pt("state"), STATES,
                         index=STATES.index(existing_state) if existing_state in STATES else STATES.index("Tamil Nadu"))
    districts = DISTRICTS_BY_STATE.get(state, ["District not listed","Other"])
    existing_district = val("district","")
    district = c2.selectbox(pt("district"), districts,
                            index=districts.index(existing_district) if existing_district in districts else 0)
    residence_options = ["Rural","Urban","Semi-urban","Any"]
    residence_labels = {"Rural":pt("rural"),"Urban":pt("urban"),"Semi-urban":pt("semi"),"Any":pt("any")}
    residence = c3.selectbox(pt("residence"), residence_options,
                             index=residence_options.index(val("residence","Any")) if val("residence") in residence_options else 3,
                             format_func=lambda value: residence_labels[value])
    c1,c2,c3 = st.columns(3)
    existing_income = val("annual_income")
    income_label = "Not sure / Prefer not to say"
    if existing_income:
        for label, limit in INCOME_OPTIONS:
            if limit is not None and existing_income <= limit:
                income_label = label
                break
        else:
            income_label = "Above ₹10 lakh"
    income_choice = c1.selectbox(pt("income"), [label for label, _ in INCOME_OPTIONS],
                                 index=[label for label, _ in INCOME_OPTIONS].index(income_label))
    income = dict(INCOME_OPTIONS).get(income_choice)
    education = c2.selectbox(pt("education"), EDUCATION_OPTIONS,
                             index=EDUCATION_OPTIONS.index(val("education")) if val("education") in EDUCATION_OPTIONS else 0)
    existing_employment = val("employment")
    employment = c3.selectbox(pt("employment"), EMPLOYMENT_OPTIONS,
                              index=EMPLOYMENT_OPTIONS.index(existing_employment) if existing_employment in EMPLOYMENT_OPTIONS else 0)
    existing_occupation = val("occupation")
    occupation = st.selectbox(pt("occupation"), OCCUPATION_OPTIONS,
                              index=OCCUPATION_OPTIONS.index(existing_occupation) if existing_occupation in OCCUPATION_OPTIONS else 0)
    disability_options = ["No","Yes","Prefer not to say"]
    disability_labels = {"No":pt("no"),"Yes":pt("yes"),"Prefer not to say":pt("gender_hide")}
    disability = st.selectbox(pt("disability"), disability_options,
                              index=disability_options.index(val("disability_status","No")) if val("disability_status") in disability_options else 0,
                              format_func=lambda value: disability_labels[value])

    extra = {}
    if beneficiary == "Student":
        extra["education_level"] = st.text_input(pt("education_level"), val("education_level",""))
        extra["course_stream"] = st.text_input(pt("course"), val("course_stream",""))
        institution_options = ["School","College","University","ITI/Polytechnic","Other"]
        institution_labels = {"School":pt("school"),"College":pt("college"),"University":pt("university"),"ITI/Polytechnic":pt("iti"),"Other":pt("other_gender")}
        extra["institution_type"] = st.selectbox(pt("institution"), institution_options, index=0, format_func=lambda value: institution_labels[value])
        extra["academic_year"] = st.text_input(pt("academic"), val("academic_year",""))
    elif beneficiary == "Farmer":
        extra["farmer_status"] = st.selectbox(pt("farmer_status"), ["Owner cultivator","Tenant","Agricultural labourer","Fishery","Other"])
        extra["landholding"] = st.selectbox(pt("land_ownership"), ["Own land","Leased land","Shared tenancy","No land"])
        extra["landholding_size_acres"] = st.number_input(pt("land_size"), min_value=0.0, value=float(val("landholding_size_acres") or 0))
        extra["crop_activity"] = st.text_input(pt("crop"), val("crop_activity",""))
    elif beneficiary == "Business Owner":
        extra["business_type"] = st.text_input(pt("business_type"), val("business_type",""))
        extra["business_age_years"] = st.number_input(pt("business_age"), min_value=0, max_value=100, value=int(val("business_age_years") or 0))
        extra["business_turnover"] = st.number_input(pt("turnover"), min_value=0, value=int(val("business_turnover") or 0), step=10000)
        extra["msme_registered"] = st.selectbox(pt("msme"), ["Unknown","Yes","No"])
    elif beneficiary == "Job Seeker":
        extra["skills"] = st.text_area(pt("skills"))
        extra["work_experience_years"] = st.number_input(pt("experience"), min_value=0, max_value=60, value=int(val("work_experience_years") or 0))

    additional = st.text_area(pt("additional"))
    st.markdown(f"### {pt('documents')}")
    consent = st.checkbox(pt("consent"))
    document_kind = st.selectbox(pt("document_type"), [pt("income_doc"),pt("community_doc"),pt("education_doc"),pt("disability_doc"),pt("land_doc"),pt("other")])
    uploaded = st.file_uploader(pt("upload"), type=["pdf","jpg","jpeg","png"])
    if uploaded and consent:
        text, error = extract_document_text(uploaded)
        if error:
            st.error(error)
        else:
            st.success(f"{document_kind} processed for temporary extraction.")
            with st.expander("Review extracted text"):
                st.text(text[:3000] if text else "No readable text was extracted.")
            if text and not text.startswith("[Image"):
                with st.spinner("Normalizing document facts..."):
                    facts, ai_error = normalize_document_text(text)
                if ai_error:
                    st.caption(ai_error)
                elif facts:
                    st.json(facts)
    elif uploaded:
        st.warning("Consent is required before processing this document.")
    c1,c2,c3 = st.columns(3)
    save_profile = c1.button(pt("save"))
    ai_text = c2.text_area(pt("describe"), height=70)
    ai_extract = c3.button(pt("extract"))

    if ai_extract:
        if not ai_text.strip():
            st.warning("Enter a profile description first.")
        else:
            with st.spinner("Extracting structured profile..."):
                extracted_profile, error = ProfileExtractionService().extract(ai_text)
            if error:
                st.error(error)
            elif extracted_profile is not None:
                profile = extracted_profile
                with st.spinner("Analyzing profile keywords with Gemini..."):
                    analyzed_profile, analysis_error = ProfileExtractionService().analyze_profile(profile)
                if analyzed_profile is not None:
                    profile = analyzed_profile
                st.session_state.profile = profile
                st.success("Profile extracted. Review the form and submit.")
                if analysis_error:
                    st.caption("Gemini keyword analysis unavailable; deterministic matching remains active.")
                elif profile.ai_keywords:
                    st.write("**AI search keywords:** " + ", ".join(profile.ai_keywords))
                st.json(profile.model_dump())

    if save_profile:
        st.info("Profile saving to MongoDB is attempted; this demo session also keeps the profile locally.")

    if st.button(pt("submit"), type="primary"):
        if not state.strip():
            st.error("State is required.")
        else:
            missing = []
            if age is None: missing.append("Age")
            if income is None:
                missing.append("Annual family income")
            profile = UserProfile(
                name=name, age=age, gender=gender, state=state, district=district,
                residence=residence, annual_income=income, education=education,
                employment=employment, occupation=occupation, beneficiary_type=beneficiary,
                disability_status=disability, additional_information=additional,
                missing_fields=missing, needs_confirmation=bool(missing), **extra
            )
            with st.spinner("Gemini is reading the submitted form and extracting recommendation keywords..."):
                analyzed_profile, analysis_error = ProfileExtractionService().analyze_profile(profile)
            if analyzed_profile is not None:
                profile = analyzed_profile
            if not profile.ai_keywords:
                profile.ai_keywords = list(dict.fromkeys([
                    beneficiary.lower(),
                    occupation.lower(),
                    education.lower(),
                    employment.lower(),
                    state.lower(),
                    district.lower(),
                    *[word.lower() for word in additional.lower().split() if len(word) >= 4],
                ]))
            if analysis_error:
                st.caption("Gemini is unavailable. Local profile keywords are being used for relevance.")
            st.session_state.profile = profile
            saved = ProfileRepository().save_profile(profile)
            st.success("Profile saved to MongoDB." if saved else "Profile retained in demo session. MongoDB is not configured.")
            st.session_state.page = "recommendations"
            st.rerun()
