from models.profile import UserProfile
from services.recommendation_service import recommendations_for


def test_recommendation_sort_and_classification():
    profile = UserProfile(beneficiary_type="Farmer", age=40, annual_income=100000)
    schemes = [
        {"scheme_id":"a","scheme_name":"Farmer A","mandatory_rules":[{"field":"beneficiary_type","operator":"equals","value":"Farmer"}]},
        {"scheme_id":"b","scheme_name":"Student B","mandatory_rules":[{"field":"beneficiary_type","operator":"equals","value":"Student"}]},
    ]
    results = recommendations_for(profile, schemes)
    assert {r.status for r in results} == {"Potentially Eligible","Not Matching"}
