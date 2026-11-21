from typing import Optional
from pydantic import BaseModel, Field, field_validator


class UserProfile(BaseModel):
    name: str = Field(default="", max_length=100)
    age: Optional[int] = Field(default=None, ge=1, le=120)
    gender: Optional[str] = None
    state: str = ""
    district: str = ""
    residence: str = "Any"
    annual_income: Optional[int] = Field(default=None, ge=0)
    education: str = ""
    employment: str = ""
    occupation: str = ""
    beneficiary_type: str = "General Public"
    additional_information: str = ""
    caste_category: str = ""
    disability_status: str = "No"
    education_level: str = ""
    course_stream: str = ""
    institution_type: str = ""
    academic_year: str = ""
    farmer_status: str = ""
    landholding: str = ""
    landholding_size_acres: Optional[float] = Field(default=None, ge=0)
    crop_activity: str = ""
    business_type: str = ""
    business_age_years: Optional[int] = Field(default=None, ge=0)
    business_turnover: Optional[int] = Field(default=None, ge=0)
    msme_registered: str = "Unknown"
    skills: str = ""
    work_experience_years: Optional[int] = Field(default=None, ge=0)
    missing_fields: list[str] = Field(default_factory=list)
    needs_confirmation: bool = False
    ai_keywords: list[str] = Field(default_factory=list)

    @field_validator("state", "district", "education", "employment", "occupation")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        return " ".join(value.strip().split())
