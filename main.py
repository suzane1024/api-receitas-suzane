from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title='API da Suzane')

class ReceitaCreate(BaseModel):
    nome: str
    ingredientes: List[str]   # corrigido: antes estava "ingredients"
    modo_de_preparo: str

class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

receitas: List[Receita] = []

@app.get("/")
def hello():
    return {"title": "api-receitas-suzane"}

@app.get("/receitas/")
def get_todas_receitas():
    return receitas

@app.post("/receitas")
def criar_receita(dados: ReceitaCreate):
    for receita in receitas:
        if receita.nome.lower() == dados.nome.lower():
            raise HTTPException(status_code=400, detail="Já existe uma receita com esse nome.")
    novo_id = receitas[-1].id + 1 if receitas else 1
    nova_receita = Receita(id=novo_id, **dados.dict())
    receitas.append(nova_receita)
    return nova_receita

@app.get("/receitas/{nome_receita}")
def get_receita_por_nome(nome_receita: str):
    for receita in receitas:
        if receita.nome.lower() == nome_receita.lower():
            return receita
    raise HTTPException(status_code=404, detail="Receita não encontrada")

@app.get("/receita/id/{id}", response_model=Receita)
def get_receita_por_id(id: int):
    for receita in receitas:
        if receita.id == id:
            return receita
    raise HTTPException(status_code=404, detail="Receita não encontrada")

@app.put("/receita/{id}")
def update_receita(id: int, dados: ReceitaCreate):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,   # corrigido: antes estava "dados.ingredients"
                modo_de_preparo=dados.modo_de_preparo
            )
            receitas[i] = receita_atualizada
            return receita_atualizada
    raise HTTPException(status_code=404, detail="Receita não encontrada")

@app.delete("/receitas/{id}")
def deletar_receita(id: int):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receitas.pop(i)
            return {"mensagem": "Receita deletada"}
    raise HTTPException(status_code=404, detail="Receita não encontrada")
