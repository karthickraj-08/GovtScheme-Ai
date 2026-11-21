import os
from config.settings import settings


def get_database():
    if not settings.mongodb_uri:
        return None
    try:
        from pymongo import MongoClient
        client = MongoClient(settings.mongodb_uri, serverSelectionTimeoutMS=3000)
        client.admin.command("ping")
        return client[settings.mongodb_db]
    except Exception:
        return None
