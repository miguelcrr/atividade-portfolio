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

@app.get("/dados")
def dados():
    return {
        "nome": "Miguel Correa Serraglio",
        "titulo": "Estudante de Engenharia de Computação",
        "sobre": "Sou estudante de engenharia de computação na Fastech e estou aprendendo desenvolvimento web com HTML, CSS, Python, JavaScript ",
        "escolaridade": "Ensino superior em andamento",
        "contato": "miguelcorreaserraglio@gmail.com",
        "foto": "foto.jpg",
        "projetos": ["IMC", "Elevador", "API", "Portfólio"]
    }