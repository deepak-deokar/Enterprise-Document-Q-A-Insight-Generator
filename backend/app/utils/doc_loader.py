from langchain.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.utils.vector_store import get_vector_store
from app.utils.embedding_model import get_embedding_model
import os

# 🚀 Config
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# Supported extensions
SUPPORTED_EXTS = [".pdf", ".docx", ".txt"]

# 🚀 Main ingestion function
def ingest_document(file_path: str):
    print(f"[DEBUG] Ingesting document: {file_path}")

    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".docx":
        loader = UnstructuredWordDocumentLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    # Load raw docs
    raw_docs = loader.load()
    print(f"[DEBUG] Loaded {len(raw_docs)} raw documents")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    docs = splitter.split_documents(raw_docs)
    print(f"[DEBUG] Split into {len(docs)} chunks")

    # Add metadata (source filename)
    for doc in docs:
        doc.metadata["source"] = os.path.basename(file_path)

    # Embed and store in Vector DB
    vector_store = get_vector_store()
    vector_store.add_documents(docs)
    vector_store.persist()

    print(f"[DEBUG] Document {file_path} ingested and stored in vector DB ✅")