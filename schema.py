from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from http import HTTPStatus

class ReceitaCreate(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

app = FastAPI()
receitas: List[Receita] = []

@app.get("/receitas", response_model=List[Receita], status_code=HTTPStatus.OK)
def get_todas_receitas():
    return receitas

@app.post("/receitas", response_model=Receita, status_code=HTTPStatus.CREATED)
def criar_receita(dados: ReceitaCreate):
    for receita in receitas:
        if receita.nome.lower() == dados.nome.lower():
            raise HTTPException(status_code=400, detail="Já existe uma receita com esse nome.")
    novo_id = receitas[-1].id + 1 if receitas else 1
    nova_receita = Receita(id=novo_id, **dados.dict())
    receitas.append(nova_receita)
    return nova_receita

@app.put("/receitas/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def update_receita(id: int, dados: ReceitaCreate):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo
            )
            receitas[i] = receita_atualizada
            return receita_atualizada
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

@app.delete("/receitas/{id}", status_code=HTTPStatus.OK)
def deletar_receita(id: int):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receitas.pop(i)
            return {"mensagem": "Receita deletada"}
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

def receita_existe(nome: str):
    for receita in receitas:
        if receita.nome == nome:
            return True
    return False








