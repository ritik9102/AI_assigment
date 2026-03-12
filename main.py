from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Resilient Decision Workflow System")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Workflow Decision System Running"}
