# backend/app/config.py

import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

MODEL_NAME = config.get("model_name", "phi4-mini")
EMBEDDING_MODEL_NAME = config.get("embedding_model", "sentence-transformers/all-MiniLM-L6-v2")
CHUNK_SIZE = config.get("chunk_size", 800)
CHUNK_OVERLAP = config.get("chunk_overlap", 100)
TOP_K_RETRIEVAL = config.get("top_k_retrieval", 5)
RAG_THRESHOLD = config.get("rag_threshold", 1000)
ENABLE_POST_EDIT = config.get("enable_post_edit", True)
EVALUATION_METRICS = config.get("evaluation_metrics", ["rouge1", "rouge2", "rougeL"])