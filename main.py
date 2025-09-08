from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title='API da Suzane')

class Receita(BaseModel):
    nome: str
    ingredients: List [str]
    modo_de_preparo: str

receitas: List[Receita] = []
    
@app.get("/")
def hello():
    return {"title": "api-receitas-suzane"}

@app.get("/receitas/{receita}")
def get_receita():
    return {"message": "Livro de Receitas!"}

@app.get("/receitas/")
def get_todas_receitas():
    return receitas 

@app.post("/receitas", response_model=Receita, status_code=201)
def criar_receita(dados: Receita): 
    nova_receita = dados

    receitas.append(nova_receita)

    return nova_receita

@app.get("/receitas/{nome_receita}")
def get_receita_por_nome(nome_receita: str ):
    for receitas in receitas:
        if receitas.nome == nome_receita:
            return receita
        
    return {"receita não encontrada"}

@app.post("/receitas")
def create_receita(dados: Receita):
    nova_receitas = dados 

    receitas.append(nova_receita)

    return nova_receita