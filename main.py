from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .schema import ReceitaCreate, Receita, Usuario, BaseUsuario, UsuarioPublic

app = FastAPI(title='API da Suzane')

_next_id = 1

usuarios: List[Usuario] = []

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
                ingredientes=dados.ingredientes,   
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

@app.post("/usuarios", status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_usuario(dados: BaseUsuario):
    for usuarios in usuarios:
        if usuarios == usuarios:
            raise HTTPException(status_code=400, detail="Já existe um usuario com esse nome.")
    novo_id = receitas[-1].id + 1 if receitas else 1
    novos_usuarios = Receita(id=novo_id, **dados.dict())
    usuarios.append(novos_usuarios)
    return novos_usuarios


@app.get("/usuarios/{Usuario}")
def todos_os_usuarios(nome_usuario: str):
    for usuarios in usuarios:
        if todos_os_usuarios() == todos_os_usuarios():
            return usuarios

@app.get("/usuarios/nome_usuario/{nome_usuario}", response_model=Usuario)
def get_usuario_por_nome(nome_usuario: str):
    for get_usuario_por_nome in get_usuario_por_nome:
        if nome_usuario == nome_usuario:
            return usuarios 
    raise HTTPException(status_code=404, detail="Receita não encontrada")

@app.get("/usuarios/id/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_id(id: int):
    for get_usuario_por_id in get_usuario_por_id:
        if get_usuario_por_id == get_usuario_por_id:
            return usuarios
        
@app.put("/usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def update_usuario(id: int, dados: BaseUsuario):
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
    raise HTTPException(status_code=404, detail="Receita não encontrada")
