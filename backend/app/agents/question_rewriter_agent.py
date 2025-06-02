import ollama
from app.config import MODEL_NAME

# 🚀 Question Rewriter Agent → improves clarity of question
def rewrite_question(question: str) -> str:
    print(f"[DEBUG] Rewriting question: {question}")

    prompt = f"""
Rewrite the following question to be as clear and specific as possible for an AI system:

Question: {question}
"""
    response = ollama.chat(model=MODEL_NAME, messages=[
        {"role": "user", "content": prompt}
    ])

    rewritten = response['message']['content'].strip()
    print(f"[DEBUG] Rewritten question: {rewritten}")
    return rewritten