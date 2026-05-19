# AI Resume Analyzer

An AI-powered Resume Analyzer built using FastAPI and OpenRouter/OpenAI APIs.

## Features

- Resume PDF Upload
- ATS Score Analysis
- Strengths & Weaknesses Detection
- Skill Extraction
- Resume Improvement Suggestions
- AI-powered Evaluation

## Tech Stack

- Python
- FastAPI
- OpenRouter API
- OpenAI Models
- PyPDF2
- Uvicorn

## Run Locally

```bash
git clone https://github.com/ujjwalavijapurapu96/ai-resume-analyzer.git

cd ai-resume-analyzer

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

## API Endpoint

POST `/upload-resume`

Upload PDF resume and receive AI analysis.

## Future Improvements

- Job Description Matching
- Resume Ranking
- Frontend Dashboard
- Authentication
- Resume Builder
- Downloadable Reports
