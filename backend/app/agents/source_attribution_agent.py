# 🚀 Source Attribution Agent → formats list of sources nicely

def attribute_sources(sources: list[str]) -> str:
    print(f"[DEBUG] Attributing sources: {sources}")

    if not sources:
        return "No sources found."

    formatted_sources = "\n".join([f"- {src}" for src in sources])
    return f"Sources:\n{formatted_sources}"