import json
from src.core.llm_client import AzureModel
from src.api.schemas import AnalysisRequest, AnalysisResult


def analyze_recommendation(request: AnalysisRequest) -> AnalysisResult:
    try:
        llm = AzureModel()

        prompt = f"""
Você é um especialista em compliance financeiro.

Regras:
- Clientes conservadores NÃO podem receber produtos de alto risco
- Identifique produtos como ações, criptomoedas, fundos, derivativos

Analise a recomendação:
"{request.text}"

Perfil do cliente:
"{request.client_profile}"

RESPONDA APENAS EM JSON no formato:
{{
  "is_compliant": true ou false,
  "reason": "explicação clara",
  "mentioned_products": ["produto1", "produto2"]
}}
"""

        response = llm.invoke(prompt)
        texto = response.choices[0].message.content

        # 🔥 CONVERTE JSON
        data = json.loads(texto)

        return AnalysisResult(**data)

    except Exception as e:
        return AnalysisResult(
            is_compliant=False,
            reason=f"Erro ao processar resposta da IA: {str(e)}",
            mentioned_products=[]
        )