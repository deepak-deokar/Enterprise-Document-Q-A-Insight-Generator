# backend/app/langgraph_pipeline.py

from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda

# Import agents
from app.agents.retriever_agent import retrieve_context
from app.agents.question_rewriter_agent import rewrite_question
from app.agents.answer_generator_agent import generate_answer
from app.agents.source_attribution_agent import attribute_sources
from app.agents.post_edit_agent import post_edit_answer
from app.agents.summarizer_agent import summarize_document
from app.agents.insight_agent import extract_insights
from app.agents.evaluation_agent import evaluate_summary

from app.config import ENABLE_POST_EDIT, TOP_K_RETRIEVAL

# 🚀 State schema (can be flexible — we'll use a simple dict)
class QAPipelineState(dict):
    question: str
    rewritten_question: str
    context: str
    sources: list[str]
    answer: str
    final_answer: str

# 🚀 Define LangGraph nodes

# 1️⃣ Question Rewriter Node
rewrite_node = RunnableLambda(lambda state: {
    "rewritten_question": rewrite_question(state["question"])
})

# 2️⃣ Retriever Node
retriever_node = RunnableLambda(lambda state: retrieve_context(
    question=state["rewritten_question"],
    top_k=TOP_K_RETRIEVAL
))

# 3️⃣ Answer Generator Node
answer_node = RunnableLambda(lambda state: {
    "answer": generate_answer(state["rewritten_question"], state["context"])
})

# 4️⃣ Source Attribution Node
source_attr_node = RunnableLambda(lambda state: {
    "sources": state["sources"],
    "source_text": attribute_sources(state["sources"])
})

# 5️⃣ Post-Edit Node
post_edit_node = RunnableLambda(lambda state: {
    "final_answer": post_edit_answer(state["answer"]) if ENABLE_POST_EDIT else state["answer"]
})

# 🚀 Assemble LangGraph pipeline
def build_qa_graph():
    graph = StateGraph(QAPipelineState)

    # Add nodes
    graph.add_node("rewrite_question", rewrite_node)
    graph.add_node("retrieve_context", retriever_node)
    graph.add_node("generate_answer", answer_node)
    graph.add_node("attribute_sources", source_attr_node)
    graph.add_node("post_edit_answer", post_edit_node)

    # Set entry point
    graph.set_entry_point("rewrite_question")

    # Define edges
    graph.add_edge("rewrite_question", "retrieve_context")
    graph.add_edge("retrieve_context", "generate_answer")
    graph.add_edge("generate_answer", "attribute_sources")
    graph.add_edge("attribute_sources", "post_edit_answer")
    graph.add_edge("post_edit_answer", END)

    return graph.compile()

# 🚀 Pipeline runner
qa_graph = build_qa_graph()

def run_qa_pipeline(question: str):
    print(f"[DEBUG] Running LangGraph QA pipeline for question: {question}")

    initial_state = {
        "question": question
    }

    final_state = qa_graph.invoke(initial_state)

    print(f"[DEBUG] Final state: {final_state}")

    return {
        "answer": final_state.get("final_answer", ""),
        "sources": final_state.get("sources", []),
        "source_text": final_state.get("source_text", "")
    }

# 🚀 Summarizer pipeline (simple direct call)
def run_summarizer_pipeline(doc_name: str):
    return summarize_document(doc_name)

# 🚀 Insight extraction pipeline (simple direct call)
def run_insight_pipeline(text: str):
    return extract_insights(text)

# 🚀 Evaluation pipeline (simple direct call)
def run_evaluation_pipeline(predicted: str, reference: str):
    return evaluate_summary(predicted, reference)