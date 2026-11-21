from models.profile import UserProfile
from services.gemini_service import GeminiService


class ProfileExtractionService:
    def __init__(self):
        self.gemini = GeminiService()

    def extract(self, text: str):
        prompt = f"""
Extract the following Indian citizen profile into JSON only.
Use these fields: name, age, gender, state, district, residence,
annual_income, education, employment, occupation, beneficiary_type,
additional_information, caste_category, disability_status,
education_level, course_stream, institution_type, academic_year,
farmer_status, landholding, landholding_size_acres, crop_activity,
business_type, business_age_years, business_turnover, msme_registered,
skills, work_experience_years.
Identify missing_fields and needs_confirmation.
Do not infer eligibility or approval. Input: {text}
"""
        data, error = self.gemini.generate_json(prompt)
        if error:
            return None, error
        try:
            profile = UserProfile.model_validate(data)
            return profile, None
        except Exception as exc:
            return None, f"Extracted profile validation failed: {exc}"

    def analyze_profile(self, profile: UserProfile):
        prompt = f"""
Analyze this Indian citizen profile for government scheme discovery.
Return JSON only with: keywords (list of plain search terms), missing_fields (list),
and needs_confirmation (boolean). Do not approve eligibility.
Profile: {profile.model_dump_json()}
"""
        data, error = self.gemini.generate_json(prompt)
        if error:
            return profile, error
        try:
            keywords = data.get("keywords", []) if isinstance(data, dict) else []
            profile.ai_keywords = [str(item).strip().lower() for item in keywords if str(item).strip()]
            profile.missing_fields = data.get("missing_fields", profile.missing_fields) if isinstance(data, dict) else profile.missing_fields
            profile.needs_confirmation = bool(data.get("needs_confirmation", False)) if isinstance(data, dict) else False
            return profile, None
        except Exception as exc:
            return None, f"Profile analysis validation failed: {exc}"
