from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import User, table_registry

app= FastAPI(title="API de teste")

engine = create_engine("sqlite:///:memory:", echo=False)

table_registry.metadata.create_all(engine)

with Session(engine) as session:
    usuario_novo = User(
        username="nome_de_usuario", password="senha123", email=" user@email.com"
                         
    )
    session.add(usuario_novo)
    session.commit()
    session.refresh(usuario_novo)

print("DADOS DO USUÁRIO NOVO:", usuario_novo)
print("ID:", usuario_novo.id)
print("Criado em:", usuario_novo.created_at)

