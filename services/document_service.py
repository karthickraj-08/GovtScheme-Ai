from pathlib import Path
import pymupdf as fitz
from PIL import Image
from config.settings import settings
from services.gemini_service import GeminiService


def extract_document_text(uploaded_file):
    name = uploaded_file.name.lower()
    data = uploaded_file.getvalue()
    if len(data) > settings.max_upload_mb * 1024 * 1024:
        return None, f"File exceeds the {settings.max_upload_mb} MB limit."
    suffix = Path(name).suffix.lower().lstrip(".")
    if suffix not in settings.allowed_upload_types:
        return None, "Unsupported file type."
    try:
        if suffix == "pdf":
            text_parts = []
            doc = fitz.open(stream=data, filetype="pdf")
            for page in doc:
                text_parts.append(page.get_text())
            doc.close()
            return "\n".join(text_parts).strip(), None
        with Image.open(uploaded_file) as image:
            image.verify()
        return "[Image uploaded: visual text extraction is unavailable]", None
    except Exception as exc:
        return None, f"Document could not be read: {exc}"


def normalize_document_text(text: str):
    gemini = GeminiService()
    if not text:
        return None, "No document text was extracted."
    data, error = gemini.generate_json(
        "Extract only clearly stated profile facts from this document consented for processing. "
        "Return JSON with fields annual_income, state, education, disability_status, caste_category, landholding_size_acres, "
        "and missing_fields. Do not verify authenticity. Document text:\n" + text[:12000]
    )
    return data, error
