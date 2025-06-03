# backend/app/agents/question_rewriter_agent.py

import ollama
from app.config import MODEL_NAME

def rewrite_question(question: str, model_name=MODEL_NAME) -> str:
    print(f"[DEBUG] Rewriting question: {question}")

    # 🚀 Improved rewriter prompt
    prompt = f"""
You are a helpful assistant refining user questions for a RAG-based document QA system.

Guidelines:
- Rewrite for clarity and focus.
- DO NOT change names, dates, or entities in the question.
- DO NOT add example answers.
- DO NOT add additional assumptions.
- Keep the intent of the original question.
- Output only the rewritten question.
- while rewriting question, mostly make changes regarding grammatical, spelling mistakes only 
if there are any while entering question, otherwise keep the question as it is no need of rewriting.

User question:
{question}

Rewritten question:
"""

    response = ollama.chat(model=model_name, messages=[
        {"role": "user", "content": prompt}
    ])

    rewritten_question = response["message"]["content"].strip()

    print(f"[DEBUG] Rewritten question: {rewritten_question}")
    return rewritten_question