from fastapi import FastAPI
from src.api.schemas import AnalysisRequest
from src.services.compliance_service import analyze_recommendation

app = FastAPI()

@app.post("/analyze")
def analyze(request: AnalysisRequest):
    return analyze_recommendation(request)