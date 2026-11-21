from database.connection import get_database


class RecommendationRepository:
    def __init__(self):
        self.db = get_database()

    def save(self, profile, recommendations):
        if self.db is None:
            return False
        try:
            self.db.recommendations.insert_one({
                "profile": profile.model_dump() if hasattr(profile, "model_dump") else dict(profile),
                "recommendations": [r.model_dump() if hasattr(r, "model_dump") else r for r in recommendations],
            })
            return True
        except Exception:
            return False
