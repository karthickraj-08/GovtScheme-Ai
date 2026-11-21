# SchemeFinder AI

A Streamlit MVP for discovering Indian government scheme information and performing transparent, deterministic initial eligibility assessments.

## Features

- Responsive government-service-inspired interface
- Beneficiary profile form with category-specific fields
- Optional Gemini profile extraction and structured Pydantic validation
- Deterministic rule-based matching; AI never decides eligibility
- Scheme explorer, details, saved schemes, and document checklist
- MongoDB Atlas support with a clearly identified demo mode
- Curated demonstration scheme records with official portal links

## Setup

```powershell
cd "C:\VS CODE PROJECTS\Govt AI"
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

Add values to `.env`:

```text
GEMINI_API_KEY=your_google_ai_api_key
MONGODB_URI=mongodb+srv://username:password@cluster/database
MONGODB_DB=schemefinder_ai
```

For Streamlit Community Cloud, add these values under **App settings > Secrets** instead of committing them.

## MongoDB

The application works without MongoDB using demo scheme records stored in `services/scheme_data_service.py`. Profile and recommendation writes are skipped with an explicit demo-session message when `MONGODB_URI` is absent or unreachable.

## Gemini

The Gemini integration uses the official `google-genai` SDK and `gemini-2.0-flash`. It is optional. Gemini handles text extraction only; eligibility decisions come exclusively from `services/eligibility_engine.py`.

## Data accuracy

Demo records are not exhaustive verified scheme database entries. They include official portal links and must be checked against current official instructions before use or application.
