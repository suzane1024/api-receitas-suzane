from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title='API da Suzane')

class Receita(BaseModel):
    nome: str
    ingredients: List[str]
    modo_de_preparo: str

receitas: List[Receita] = []

@app.get("/")
def hello():
    return {"title": "api-receitas-suzane"}

@app.get("/receitas/")
def get_todas_receitas():
    return receitas

@app.post("/receitas", response_model=Receita, status_code=201)
def criar_receita(dados: Receita):
    receitas.append(dados)
    return dados

@app.get("/receitas/{nome_receita}")
def get_receita_por_nome(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return receita
    return {"erro": "receita não encontrada"}