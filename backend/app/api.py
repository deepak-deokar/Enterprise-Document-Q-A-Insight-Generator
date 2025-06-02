# backend/app/api.py

from fastapi import APIRouter, UploadFile, File, Form, Body
from typing import List
from pydantic import BaseModel
from app.utils.doc_loader import ingest_document
import shutil
import os
from app.langgraph_pipeline import (
    run_qa_pipeline,
    run_summarizer_pipeline,
    run_insight_pipeline,
    run_evaluation_pipeline
)

router = APIRouter()

# 🚀 Health check
@router.get("/health")
def health_check():
    return {"status": "ok"}

# 🚀 QARequest model (for JSON input)
class QARequest(BaseModel):
    question: str

# 🚀 QA endpoint → now accepts JSON 🚀
@router.post("/qa")
def qa_endpoint(request: QARequest):
    question = request.question
    result = run_qa_pipeline(question)
    return result

# 🚀 Summarization endpoint
@router.post("/summarize")
def summarize_endpoint(doc_name: str = Form(...)):
    summary = run_summarizer_pipeline(doc_name)
    return {"summary": summary}

# 🚀 Insights endpoint
@router.post("/insights")
def insights_endpoint(text: str = Form(...)):
    insights = run_insight_pipeline(text)
    return {"insights": insights}

# 🚀 Evaluation endpoint
@router.post("/evaluate")
def evaluate_endpoint(predicted_summary: str = Form(...), reference_summary: str = Form(...)):
    scores = run_evaluation_pipeline(predicted_summary, reference_summary)
    return {"scores": scores}

# 🚀 Upload endpoint
@router.post("/upload")
def upload_endpoint(file: UploadFile = File(...)):
    print(f"[DEBUG] Received file upload: {file.filename}")

    # Save uploaded file to temp folder
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Ingest document into vector store
    ingest_document(file_path)

    return {"status": "success", "filename": file.filename}