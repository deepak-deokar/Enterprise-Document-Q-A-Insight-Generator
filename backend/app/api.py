# backend/app/api.py

from fastapi import APIRouter, UploadFile, File, Form
from typing import List
from app.langgraph_pipeline import run_qa_pipeline, run_summarizer_pipeline

router = APIRouter()

# Health check
@router.get("/health")
def health_check():
    return {"status": "ok"}

# Q&A endpoint
@router.post("/qa")
def qa_endpoint(question: str = Form(...)):
    result = run_qa_pipeline(question)
    return result

# Summarization endpoint
@router.post("/summarize")
def summarize_endpoint(doc_name: str = Form(...)):
    summary = run_summarizer_pipeline(doc_name)
    return {"summary": summary}