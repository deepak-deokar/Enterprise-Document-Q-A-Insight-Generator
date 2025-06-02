# backend/app/agents/summarizer_agent.py

import ollama
from app.utils.vector_store import get_vector_store
from app.config import MODEL_NAME

# 🚀 Summarizer Agent → summarizes selected document

def summarize_document(doc_name: str) -> str:
    print(f"[DEBUG] Summarizing document: {doc_name}")

    vector_store = get_vector_store()

    # Simple heuristic: search for all chunks that came from this doc
    results = vector_store.similarity_search("Document summary", k=100)  # pull many chunks

    # Filter by source doc name
    doc_chunks = [
        doc.page_content
        for doc in results
        if doc.metadata.get("source") == doc_name
    ]

    if not doc_chunks:
        return "No content found for this document."

    # Combine chunks
    full_text = "\n\n".join(doc_chunks)

    prompt = f"""
Summarize the following document content in clear, concise language, suitable for business users.

Content:
{full_text}

Summary:
"""

    response = ollama.chat(model=MODEL_NAME, messages=[
        {"role": "user", "content": prompt}
    ])

    summary = response['message']['content'].strip()
    print(f"[DEBUG] Generated summary.")
    return summary