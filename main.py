from fastapi import FastAPI

app = FastAPI(title='API da Suzane')

@app.get("/")
def hello():
    return {"title": "api-receitas-suzane"}

@app.get("/receitas/{receita}")
def get_receita():
    return {"message": "Livro de Receitas!"}