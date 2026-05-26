from fastapi import FastAPI
from src.api.routes.analysis import router as analysis_router

app = FastAPI()

app.include_router(analysis_router)