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
    return {"mensagem": "API funcionando!"}

@app.get("/projetos")
def projetos():
    return [
        "Calculadora de IMC (HTML, CSS, JS)",
        "Sistema de elevador em Python",
        "API com FastAPI",
        "Site pessoal"
    ]