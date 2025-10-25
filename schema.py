from pydantic import BaseModel
from typing import List 

class ReceitaCreate(BaseModel):
    nome: str
    ingredientes: List[str]   
    modo_de_preparo: str

class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

response_model = (List[Receita], status_code=HTTPStatus.OK)
