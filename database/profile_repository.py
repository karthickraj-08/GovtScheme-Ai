from database.connection import get_database


class ProfileRepository:
    def __init__(self):
        self.db = get_database()

    def save_profile(self, profile):
        if self.db is None:
            return False
        try:
            data = profile.model_dump() if hasattr(profile, "model_dump") else dict(profile)
            self.db.profiles.update_one(
                {"session_profile": True},
                {"$set": data},
                upsert=True,
            )
            return True
        except Exception:
            return False
