from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="TaskFlow API", version="1.0.0")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to TaskFlow API VRX"}