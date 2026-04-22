from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Caminho base absoluto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CORS (liberado para testes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 SERVIR LOGO (corrigido)
app.mount(
    "/assets",
    StaticFiles(directory=os.path.join(BASE_DIR, "../frontend/assets")),
    name="assets"
)

# LOGIN
@app.post("/login")
async def login(user: dict):
    if user.get("username") == "admin" and user.get("password") == "123":
        return {"status": "ok"}
    return {"status": "erro"}

# FRONTEND
@app.get("/")
def home():
    return FileResponse(os.path.join(BASE_DIR, "../frontend/index.html"))

# DADOS
@app.get("/dados")
def dados():
    return {
        "faturamento": 245750,
        "lucro": 45890,
        "margem": 18.6,
        "caixa": 67890,
        "score": 78
    }