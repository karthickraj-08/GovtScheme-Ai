from models.profile import UserProfile
from services.eligibility_engine import evaluate_profile


def recommendations_for(profile: UserProfile, schemes: list[dict]):
    return evaluate_profile(profile, schemes)
