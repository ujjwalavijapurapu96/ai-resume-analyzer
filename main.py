from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pypdf import PdfReader
from dotenv import load_dotenv
import requests
import io
import os

load_dotenv()

app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}


@app.get("/")
async def home():
    return {
        "message": "AI Resume Analyzer Running"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    try:

        contents = await file.read()

        pdf = PdfReader(io.BytesIO(contents))

        resume_text = ""

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                resume_text += text

        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Analyze this resume.

Give:
1. Skills
2. Strengths
3. Weaknesses
4. Improvement suggestions
5. ATS score out of 100

Resume:

{resume_text}
"""
                }
            ]
        }

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

        result = response.json()

        return {
            "analysis": result
        }

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )