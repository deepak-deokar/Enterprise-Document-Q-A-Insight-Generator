# backend/app/agents/evaluation_agent.py

from rouge_score import rouge_scorer

# 🚀 Evaluation Agent → ROUGE-based evaluation

def evaluate_summary(predicted_summary: str, reference_summary: str) -> dict:
    print(f"[DEBUG] Evaluating summary with ROUGE.")

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_summary, predicted_summary)

    result = {
        "rouge1_f": scores["rouge1"].fmeasure,
        "rouge2_f": scores["rouge2"].fmeasure,
        "rougeL_f": scores["rougeL"].fmeasure,
    }

    print(f"[DEBUG] Evaluation scores: {result}")
    return result