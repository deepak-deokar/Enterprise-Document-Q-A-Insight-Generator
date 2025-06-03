# backend/app/agents/post_edit_agent.py

import ollama
from app.config import MODEL_NAME

# 🚀 Post-Edit Agent → polishes generated answer

def post_edit_answer(answer: str) -> str:
    print(f"[DEBUG] Post-editing answer...")

    prompt = f"""
Polish the following AI-generated answer for clarity and professionalism. 
Format them as a numbered list. Make those AI generated answers in human language.
Do not add any new information.

Answer:
{answer}

Polished Answer:
"""

    response = ollama.chat(model=MODEL_NAME, messages=[
        {"role": "user", "content": prompt}
    ])

    polished = response['message']['content'].strip()
    print(f"[DEBUG] Polished answer: {polished}")
    return polished