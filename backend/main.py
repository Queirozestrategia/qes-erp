from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API online"}

@app.get("/dashboard/")
def dashboard():
    return {
        "receitas": 10000,
        "despesas": 3000,
        "lucro": 7000
    }
