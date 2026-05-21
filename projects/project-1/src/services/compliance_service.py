from src.core.llm_client import analyze_with_ai
import json

def analyze_text(text: str) -> dict:
    
    ai_response = analyze_with_ai(text)

    try:
        result = json.loads(ai_response)
        return result
    except:
        return {
            "is_compliant": False,
            "reason": "Erro ao interpretar resposta da IA",
            "mentioned_products": []
        }