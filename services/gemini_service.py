import json
from pydantic import BaseModel
from config.settings import settings


class GeminiService:
    MODEL_CANDIDATES = (
        "gemini-3.8-flash",
        "gemini-2.5-flash",
        "gemini-flash-latest",
    )

    def __init__(self):
        self.enabled = bool(settings.gemini_api_key)
        self.client = None
        if self.enabled:
            try:
                from google import genai
                self.client = genai.Client(api_key=settings.gemini_api_key)
            except Exception:
                self.enabled = False

    @property
    def status(self):
        if not settings.gemini_api_key:
            return "Gemini API key is missing."
        if not self.enabled:
            return "Gemini SDK could not be initialized."
        return "Gemini is configured."

    def generate_json(self, prompt: str):
        if not self.enabled:
            return None, "Gemini is not configured."
        last_error = ""
        for model in self.MODEL_CANDIDATES:
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config={"response_mime_type": "application/json"},
                )
                text = getattr(response, "text", "") or ""
                if not text.strip():
                    raise ValueError("Gemini returned an empty response.")
                return json.loads(text), None
            except Exception as exc:
                last_error = str(exc)
        return None, f"Gemini request failed: {last_error}"

    def explain(self, prompt: str):
        if not self.enabled:
            return None
        for model in self.MODEL_CANDIDATES:
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                return getattr(response, "text", None)
            except Exception:
                continue
        return None
