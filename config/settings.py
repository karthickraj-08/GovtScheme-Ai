from dataclasses import dataclass
import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def _get_setting(name: str, default: str = "") -> str:
    value = os.getenv(name, "").strip()
    if value:
        return value
    try:
        secrets = st.secrets
        if name in secrets:
            return str(secrets[name]).strip()
    except Exception:
        pass
    return default


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str = _get_setting("GEMINI_API_KEY")
    mongodb_uri: str = _get_setting("MONGODB_URI")
    mongodb_db: str = _get_setting("MONGODB_DB", "schemefinder_ai")
    max_upload_mb: int = 5
    allowed_upload_types: tuple[str, ...] = ("pdf", "jpg", "jpeg", "png")


settings = Settings()
