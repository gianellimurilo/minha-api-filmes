from fastapi import FastAPI

app = FastAPI()

# Lista simples como "banco de dados"
filmes = [
    {"id": 1, "titulo": "Interestelar", "nota": 9.5},
    {"id": 2, "titulo": "Matrix", "nota": 9.0},
    {"id": 3, "titulo": "Senhor dos Anéis", "nota": 9.8},
]


# GET - Listar todos os filmes
@app.get("/filmes")
def listar_filmes():
    return filmes


# GET - Buscar filme por ID
@app.get("/filmes/{filme_id}")
def buscar_filme(filme_id: int):
    for filme in filmes:
        if filme["id"] == filme_id:
            return filme
    return {"erro": "Filme não encontrado"}


# POST - Adicionar um filme
@app.post("/filmes")
def adicionar_filme(titulo: str, nota: float):
    novo_filme = {
        "id": len(filmes) + 1,
        "titulo": titulo,
        "nota": nota,
    }
    filmes.append(novo_filme)
    return novo_filme


# DELETE - Remover um filme
@app.delete("/filmes/{filme_id}")
def deletar_filme(filme_id: int):
    for filme in filmes:
        if filme["id"] == filme_id:
            filmes.remove(filme)
            return {"mensagem": "Filme removido com sucesso"}
    return {"erro": "Filme não encontrado"}