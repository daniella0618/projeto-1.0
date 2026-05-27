from pydantic import BaseModel, Field
from typing import List


class AnalysisRequest(BaseModel):
    text_to_analyze: str = Field(
        ...,
        min_length=10,
        description="Texto da recomendação a ser analisada."
    )


class Source(BaseModel):
    document: str
    chunk_id: str


class AnalysisResponse(BaseModel):
    is_compliant: bool = Field(
        ...,
        description="Indica se a recomendação está em conformidade."
    )
    reason: str = Field(
        ...,
        description="Justificativa detalhada da análise."
    )
    mentioned_products: List[str] = Field(
        default_factory=list,
        description="Lista de produtos mencionados."
    )
    sources: List[Source] = Field(
        default_factory=list,
        description="Fontes utilizadas na análise"
    )