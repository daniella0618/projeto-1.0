from src.core.llm_client import analyze_with_ai
from src.rag.retrieval import retrieve
from src.rag.reranker import rerank


def analyze_text(text: str) -> dict:

    docs = retrieve(text)
    docs = rerank(text, docs)

    context = "\n".join([d["text"] for d in docs])

    prompt = f"""
    Analise o texto com base no contexto abaixo:

    CONTEXTO:
    {context}

    TEXTO:
    {text}

    Explique se está em conformidade.
    """

    ai_response = analyze_with_ai(prompt)

    return {
        "is_compliant": False,
        "reason": ai_response,
        "mentioned_products": [],
        "sources": [
            {
                "document": d["source"],
                "chunk_id": d["chunk_id"]
            }
            for d in docs
        ]
    }