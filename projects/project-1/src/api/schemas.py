from pydantic import BaseModel
from typing import List

class AnalysisRequest(BaseModel):
    text: str
    client_profile: str

class AnalysisResult(BaseModel):
    is_compliant: bool
    reason: str
    mentioned_products: List[str]