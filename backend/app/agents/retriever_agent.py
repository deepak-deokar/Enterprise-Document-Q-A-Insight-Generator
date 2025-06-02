# backend/app/agents/retriever_agent.py

from app.utils.vector_store import get_vector_store
from app.utils.embedding_model import get_embedding_model

# 🚀 Retriever Agent → pulls relevant chunks for given question

def retrieve_context(question: str, top_k: int = 5):
    print(f"[DEBUG] Retriever agent running for question: {question}")

    # Load embedding model & vector store
    embedding_model = get_embedding_model()
    vector_store = get_vector_store()

    # Embed question
    question_embedding = embedding_model.encode([question])[0]

    # Search vector DB
    results = vector_store.similarity_search_by_vector(question_embedding, top_k=top_k)

    # Extract retrieved texts + metadata
    retrieved_texts = [doc.page_content for doc in results]
    sources = [doc.metadata.get("source", "unknown") for doc in results]

    print(f"[DEBUG] Retrieved {len(retrieved_texts)} chunks")
    return {
        "context": "\n\n".join(retrieved_texts),
        "sources": list(set(sources))  # unique sources
    }