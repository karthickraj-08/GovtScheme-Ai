from models.profile import UserProfile
from services.eligibility_engine import evaluate_profile


def test_farmer_matches():
    profile = UserProfile(beneficiary_type="Farmer", age=40, state="Tamil Nadu")
    schemes = [{
        "scheme_id": "test",
        "scheme_name": "Test Farmer Scheme",
        "mandatory_rules": [{"field": "beneficiary_type", "operator": "equals", "value": "Farmer"}],
        "eligible_states": [],
    }]
    result = evaluate_profile(profile, schemes)[0]
    assert result.status == "Potentially Eligible"


def test_failed_mandatory_rule_is_not_hidden():
    profile = UserProfile(beneficiary_type="Student", age=21)
    schemes = [{
        "scheme_id": "test",
        "scheme_name": "Farmer Only",
        "mandatory_rules": [{"field": "beneficiary_type", "operator": "equals", "value": "Farmer"}],
    }]
    result = evaluate_profile(profile, schemes)[0]
    assert result.status == "Not Matching"
    assert result.failed_conditions


def test_missing_income_requires_information():
    profile = UserProfile(beneficiary_type="General Public")
    schemes = [{
        "scheme_id": "test",
        "scheme_name": "Income Scheme",
        "income_limit": 250000,
    }]
    result = evaluate_profile(profile, schemes)[0]
    assert result.status == "Needs More Information"
    assert "Annual family income" in result.missing_information


def test_keyword_relevance_increases_score():
    profile = UserProfile(
        beneficiary_type="Student",
        education="Undergraduate",
        ai_keywords=["scholarship", "undergraduate"],
    )
    schemes = [{
        "scheme_id":"scholarship",
        "scheme_name":"Student Scholarship Scheme",
        "description":"Scholarship and undergraduate student assistance",
        "category":"Education",
        "beneficiaries":["Student"],
        "benefits":["Financial assistance"],
        "mandatory_rules": [],
    }]
    result = evaluate_profile(profile, schemes)[0]
    assert result.status == "Potentially Eligible"
    assert result.score >= 60
