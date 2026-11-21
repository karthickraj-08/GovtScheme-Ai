from models.profile import UserProfile
from models.recommendation import Recommendation
from services.gemini_service import GeminiService


def _profile_value(profile: UserProfile, field: str):
    aliases = {
        "annual_income": "annual_income",
        "age": "age",
        "state": "state",
        "district": "district",
        "beneficiary_type": "beneficiary_type",
        "education": "education",
        "employment": "employment",
        "occupation": "occupation",
        "residence": "residence",
        "gender": "gender",
        "disability_status": "disability_status",
    }
    return getattr(profile, aliases.get(field, field), None)


def evaluate_profile(profile: UserProfile, schemes: list[dict]) -> list[Recommendation]:
    results = []
    for scheme in schemes:
        failed = []
        missing = []
        reasons = []
        matched = 0

        min_age = scheme.get("min_age")
        max_age = scheme.get("max_age")
        if min_age is not None:
            if profile.age is None:
                missing.append("Age")
            elif profile.age < min_age:
                failed.append(f"Minimum age is {min_age}; profile age is {profile.age}.")
            else:
                reasons.append(f"Age {profile.age} meets the stated minimum.")
                matched += 1
        if max_age is not None:
            if profile.age is None:
                missing.append("Age")
            elif profile.age > max_age:
                failed.append(f"Maximum age is {max_age}; profile age is {profile.age}.")
            else:
                reasons.append(f"Age {profile.age} meets the stated maximum.")
                matched += 1

        income_limit = scheme.get("income_limit")
        if income_limit is not None:
            if profile.annual_income is None:
                missing.append("Annual family income")
            elif profile.annual_income > income_limit:
                failed.append(f"Annual income exceeds the stated limit of ₹{income_limit:,}.")
            else:
                reasons.append("Annual income is within the stated limit.")
                matched += 1

        for rule in scheme.get("mandatory_rules", []) or []:
            field = rule.get("field")
            operator = rule.get("operator", "equals")
            value = rule.get("value")
            actual = _profile_value(profile, field)
            if actual is None or (isinstance(actual, str) and not actual.strip()):
                missing.append(field.replace("_", " ").title())
                continue
            passes = (
                str(actual).lower() == str(value).lower()
                if operator == "equals"
                else True
            )
            if passes:
                reasons.append(f"{field.replace('_', ' ').title()} is consistent: {actual}.")
                matched += 1
            else:
                failed.append(f"{field.replace('_', ' ').title()} is {actual}; required value is {value}.")

        states = scheme.get("eligible_states") or []
        if states:
            if not profile.state:
                missing.append("State")
            elif profile.state not in states:
                failed.append(f"The profile state is {profile.state}; this entry lists {', '.join(states)}.")
            else:
                reasons.append(f"State is listed: {profile.state}.")
                matched += 1

        if failed:
            status = "Not Matching"
        elif missing:
            status = "Needs More Information"
        else:
            status = "Potentially Eligible"

        total = max(1, len(scheme.get("mandatory_rules", []) or []) + len(states) + (1 if min_age is not None or max_age is not None else 0) + (1 if income_limit is not None else 0))
        score = 100 if status == "Potentially Eligible" else (55 if status == "Needs More Information" else max(10, int(matched / total * 70)))

        profile_terms = [
            profile.beneficiary_type, profile.occupation, profile.education,
            profile.employment, profile.state, profile.district,
            profile.additional_information,
            *profile.ai_keywords,
        ]
        profile_terms = [str(term).lower().strip() for term in profile_terms if term]
        scheme_terms = " ".join([
            scheme.get("scheme_name", ""),
            scheme.get("description", ""),
            scheme.get("category", ""),
            " ".join(scheme.get("beneficiaries", []) or []),
            " ".join(scheme.get("benefits", []) or []),
        ]).lower()
        keyword_hits = sum(1 for term in profile_terms if len(term) >= 3 and term in scheme_terms)
        if not failed:
            score = min(100, max(score, 60 + keyword_hits * 8))
        elif keyword_hits:
            score = min(69, max(score, 35 + keyword_hits * 6))
        results.append(Recommendation(
            scheme_id=scheme["scheme_id"],
            scheme_name=scheme["scheme_name"],
            status=status,
            score=score,
            matching_reasons=reasons,
            missing_information=sorted(set(missing)),
            failed_conditions=failed,
        ))

    return sorted(results, key=lambda r: (-r.score, r.scheme_name))
