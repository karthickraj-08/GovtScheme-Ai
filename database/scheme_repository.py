from database.connection import get_database
from services.scheme_data_service import demo_schemes


class SchemeRepository:
    def __init__(self):
        self.db = get_database()

    def get_all(self):
        if self.db is not None:
            try:
                rows = list(self.db.schemes.find({}, {"_id": 0}))
                if rows:
                    return rows
            except Exception:
                pass
        return demo_schemes()

    def get_by_id(self, scheme_id):
        for scheme in self.get_all():
            if scheme.get("scheme_id") == scheme_id:
                return scheme
        return None

    def ensure_demo_data(self):
        if self.db is None:
            return False
        try:
            for scheme in demo_schemes():
                self.db.schemes.update_one(
                    {"scheme_id": scheme["scheme_id"]},
                    {"$set": scheme},
                    upsert=True,
                )
            return True
        except Exception:
            return False
