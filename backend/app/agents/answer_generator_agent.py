# backend/app/agents/answer_generator_agent.py

import ollama
from app.config import MODEL_NAME

# 🚀 Answer Generator Agent → uses retrieved context to generate answer

def generate_answer(question: str, context: str) -> str:
    print(f"[DEBUG] Generating answer for question: {question}")

    prompt = f"""
You are an expert AI assistant. Answer the following question using ONLY the provided context.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(model=MODEL_NAME, messages=[
        {"role": "user", "content": prompt}
    ])

    answer = response['message']['content'].strip()
    print(f"[DEBUG] Generated answer: {answer}")
    return answer