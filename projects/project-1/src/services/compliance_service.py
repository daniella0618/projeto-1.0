from src.core.llm_client import AzureModel
from src.api.schemas import AnalysisRequest, AnalysisResult

def analyze_recommendation(request: AnalysisRequest) -> AnalysisResult:
    try:
        llm = AzureModel()

        prompt = f"""
Analise a recomendação de investimento: {request.text}.
O cliente tem perfil: {request.client_profile}.
Diga se é adequado e explique.
"""

        response = llm.invoke(prompt)
        texto = response.choices[0].message.content

        return AnalysisResult(
            is_compliant="não" not in texto.lower(),
            reason=texto,
            mentioned_products=[]
        )

    except Exception as e:
        return AnalysisResult(
            is_compliant=False,
            reason=f"Erro ao chamar IA: {str(e)}",
            mentioned_products=[]
        )
