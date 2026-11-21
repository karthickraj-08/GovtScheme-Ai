from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Scheme(BaseModel):
    scheme_id: str
    scheme_name: str
    description: str = ""
    category: str = "Social Welfare"
    government_department: str = ""
    beneficiaries: list[str] = Field(default_factory=list)
    benefits: list[str] = Field(default_factory=list)
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    income_limit: Optional[int] = None
    eligible_states: list[str] = Field(default_factory=list)
    eligible_districts: list[str] = Field(default_factory=list)
    education_requirements: list[str] = Field(default_factory=list)
    employment_requirements: list[str] = Field(default_factory=list)
    occupation_requirements: list[str] = Field(default_factory=list)
    mandatory_rules: list[dict] = Field(default_factory=list)
    alternative_rules: list[list[dict]] = Field(default_factory=list)
    other_eligibility_rules: list[str] = Field(default_factory=list)
    required_documents: list[str] = Field(default_factory=list)
    optional_documents: list[str] = Field(default_factory=list)
    application_steps: list[str] = Field(default_factory=list)
    official_scheme_url: str = ""
    application_url: str = ""
    source_name: str = ""
    last_verified_at: Optional[str] = None
    verification_status: str = "unverified"
    is_demonstration: bool = True
