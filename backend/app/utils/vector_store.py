from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# 🚀 Setup vector store (Chroma or FAISS)

VECTOR_STORE_PATH = "vector_store"  # Folder to persist the vector DB

def get_vector_store():
    print(f"[DEBUG] Loading vector store from: {VECTOR_STORE_PATH}")

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_store = Chroma(
        persist_directory=VECTOR_STORE_PATH,
        embedding_function=embedding_model
    )
    return vector_store