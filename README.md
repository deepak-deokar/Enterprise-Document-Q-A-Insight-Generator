# 🚀 Enterprise Document Q&A & Insight Generator

A modern **AI-powered Document Q&A System** using **LangGraph**, **RAG**, and **LLM post-editing**.  
Built with a sleek **React + FastAPI** architecture & fully Dockerized 🐳.

---

## ✨ Features

✅ Upload enterprise documents (PDF, DOCX, TXT)  
✅ Automatically splits & ingests into vector store (Chroma)  
✅ LangGraph pipeline with multi-step RAG → Rewriter → Retriever → Answer Generator → Post-editor  
✅ Source attribution  
✅ Evaluate generated answers vs reference (ROUGE)  
✅ Modern React UI  
✅ 🚀 Fully Dockerized for 1-command deploy  

---

## ⚙️ Installation (Local Dev)

```bash
# Clone the repo
git clone https://github.com/deepak-deokar/Enterprise-Document-Q-A-Insight-Generator.git
cd Enterprise-Document-Q-A-Insight-Generator

# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Run backend
cd ../backend
uvicorn app.main:app --reload --port 8000

# In new terminal → run frontend
cd frontend
npm run dev
```
## 🐳 Run with Docker
```bash
# From project root
docker-compose up --build

• Frontend → http://localhost:3000
• Backend → http://localhost:8000/docs
```

## 🚀 Usage
	1️⃣ Go to Upload tab → Upload your document.
	2️⃣ Ask questions → get answers with sources.
	3️⃣ Summarize document.
	4️⃣ Extract insights.
	5️⃣ Evaluate predictions vs reference summary.

## 🏗️ Architecture
```markdown
[User Question]
      ↓
[LangGraph Pipeline]
  → Question Rewriter
  → Context Retriever (Vector DB - Chroma)
  → Answer Generator (LLM)
  → Source Attribution
  → Post-editor
      ↓
[Final Answer + Sources]

+ Evaluation Agent → ROUGE scoring
```

## 🧰 Key Technologies
	•	LangGraph (multi-agent orchestration)
	•	LangChain Core
	•	Sentence Transformers (Embeddings)
	•	Chroma (Vector DB)
	•	phi4-mini / Ollama LLMs
	•	ROUGE Score (Evaluation)
	•	FastAPI (Backend API)
	•	React + Bootstrap (Frontend UI)
	•	Docker + Docker Compose

## 🧭 Possible Improvements
	✅ Add User Auth & Multi-tenant support.
	✅ Fine-tuning pipeline (LoRA / PEFT).
	✅ Hybrid RAG (Structured + Unstructured).
	✅ Multi-modal support (images, tables).
	✅ Advanced source highlighting.
	✅ UI polish & dark mode.

## 💬 Example Questions
	•	“What skills does this candidate have?”
	•	“Summarize this policy document.”
	•	“What is the company’s refund policy?”
	•	“Extract key insights from this market report.”
	•	“How does the Responsible AI toolkit improve fairness?”