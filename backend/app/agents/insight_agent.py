# backend/app/agents/insight_agent.py

import ollama
from app.config import MODEL_NAME

# 🚀 Insight Agent → extracts actionable insights

def extract_insights(text: str) -> str:
    print(f"[DEBUG] Extracting insights...")

    prompt = f"""
Extract 3 to 5 actionable insights or key takeaways from the following content.
Format them as a numbered list.

Content:
{text}

Insights:
"""

    response = ollama.chat(model=MODEL_NAME, messages=[
        {"role": "user", "content": prompt}
    ])

    insights = response['message']['content'].strip()
    print(f"[DEBUG] Extracted insights.")
    return insights