from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title='API da Suzane')

'''
receitas = [

{'nome': 'Brownie',
 'ingredientes': ['3 ovos', '6 colheres de açucar', '1 xicara de cacau em pó', '1 pitada de sal', '1 colher (chá) de essência de baunilha (opcional)', '1 xícara de farinha de trigo', '1 xícara de manteiga derretida'],
 'utensilios': ['Tigela grande', 'Colher ou fouet', 'Forma retangular untada,', 'Forno pré-aquecido'],
 'modo de preparo': 'Misture manteiga e açúcar, Acrescente os ovos, mexendo bem., Junte o chocolate, a farinha e o sal., Coloque a baunilha,, se quiser. Despeje na forma e asse em forno a 180 °C por cerca de 30 minutos.'
},

{'nome': 'Brigadeiro',
 'ingredientes': ['1 lata de leite condensado', '4 colheres de sopa de chocolate em pó', '1 colher de sopa de manteiga', 'Chocolate granulado para decorar'],
 'utensilio': ['Panela pequena', 'Colher de pau', 'Prato untado'],
 'modo de preparo': 'Em uma panela, misture o leite condensado, o chocolate em pó e a manteiga., Leve ao fogo baixo, mexendo sem parar para não grudar no fundo., Quando a mistura começar a desgrudar do fundo da panela, está no ponto., Despeje em um prato untado com manteiga e deixe esfriar., Quando estiver frio, enrole pequenas bolinhas e passe no chocolate granulado.'
},

{'nome': 'Bolo de Cenoura com Cobertura de Chocolate',
 'ingredientes': ['3 cenouras médias', '4 ovos', '1/2 xícara de óleo', '2 xícaras de açúcar', '2 xícaras de farinha de trigo', '1 colher de sopa de fermento em pó', '1 xícara de chocolate em pó', '1/2 xícara de leite', '1 colher de sopa de manteiga'],
 'utensilio': ['Liquidificador', 'Tigela', 'Forma', 'Panela'],
 'modo de preparo': 'No liquidificador, bata a cenoura, os ovos e o óleo até ficar um creme homogêneo., Em uma tigela, misture o açúcar e a farinha de trigo., Adicione a mistura do liquidificador aos ingredientes secos e misture bem., Acrescente o fermento e misture delicadamente., Despeje a massa em uma forma untada e asse em forno pré-aquecido a 180°C por cerca de 40 minutos., Para a cobertura, misture o chocolate em pó, o leite e a manteiga em uma panela e leve ao fogo até engrossar., Cubra o bolo com a calda de chocolate.'
},

{'nome': 'Salada de Frutas',
 'ingredientes': ['2 bananas', '2 maçãs', '2 laranjas', '1 mamão pequeno', '1/2 melão pequeno', '10 morangos', '1 lata de creme de leite (opcional)'],
 'utensilio': ['Tigela grande', 'Faca', 'Colher'],
 'modo de preparo': 'Descasque e pique todas as frutas em cubos pequenos., Coloque as frutas picadas em uma tigela grande., Esprema as laranjas e jogue o suco sobre as frutas., Misture bem todos os ingredientes., Se desejar, adicione o creme de leite por cima na hora de servir.'
},

{'nome': 'Feijoada',
 'ingredientes': ['1kg de feijão preto', '250g de carne seca dessalgada', '200g de costelinha de porco salgada', '150g de paio', '150g de linguiça defumada', '1 cebola grande picada', '4 dentes de alho picados', 'Folhas de louro', 'Sal e pimenta a gosto'],
 'utensilio': ['Panela de pressão', 'Panela grande', 'Colher'],
 'modo de preparo': 'Deixe a carne seca e a costelinha de molho por pelo menos 12 horas, trocando a água., Em uma panela de pressão, cozinhe o feijão com água e as folhas de louro., Em outra panela, refogue a cebola e o alho em um pouco de óleo., Adicione as carnes dessalgadas e as linguiças e frite-as., Junte o feijão cozido com o refogado de carnes e cozinhe por mais 30 minutos em fogo baixo., Ajuste o sal e a pimenta a gosto e sirva bem quente.'
},

{'nome': 'Pão de Queijo',
 'ingredientes': ['2 copos de polvilho doce', '1 copo de leite', '1/2 copo de óleo', '1 colher de chá de sal', '2 ovos', '250g de queijo minas ralado'],
 'utensilio': ['Tigela grande', 'Colher', 'Forma'],
 'modo de preparo': 'Em uma panela, ferva o leite, o óleo e o sal., Adicione essa mistura quente ao polvilho e misture bem., Deixe esfriar um pouco e adicione os ovos um de cada vez, mexendo até incorporar., Por último, adicione o queijo ralado e misture bem com as mãos até formar uma massa homogênea., Faça bolinhas e coloque em uma forma untada., Leve ao forno pré-aquecido a 180°C por cerca de 30 minutos ou até dourarem.'
}

]
'''

class ReceitaCreate(BaseModel):
    nome: str
    ingredientes: List[str]   
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