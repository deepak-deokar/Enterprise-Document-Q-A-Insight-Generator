from sentence_transformers import SentenceTransformer

# 🚀 Load embedding model once

_EMBEDDING_MODEL = None

def get_embedding_model():
    global _EMBEDDING_MODEL
    if _EMBEDDING_MODEL is None:
        print("[DEBUG] Loading embedding model: all-MiniLM-L6-v2")
        _EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return _EMBEDDING_MODEL