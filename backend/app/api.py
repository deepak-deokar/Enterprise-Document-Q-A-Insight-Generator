# backend/app/api.py

from fastapi import APIRouter, UploadFile, File, Form, Body
from typing import List
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

# 🚀 QA endpoint
@router.post("/qa")
def qa_endpoint(question: str = Form(...)):
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