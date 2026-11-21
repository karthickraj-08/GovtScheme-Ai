from datetime import datetime, timezone
from pydantic import BaseModel, Field


class Recommendation(BaseModel):
    scheme_id: str
    scheme_name: str
    status: str
    score: int
    matching_reasons: list[str] = Field(default_factory=list)
    missing_information: list[str] = Field(default_factory=list)
    failed_conditions: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
