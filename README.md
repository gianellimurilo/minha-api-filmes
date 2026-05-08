# 🎬 API de Filmes

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/Licença-MIT-green?style=for-the-badge)

API REST para gerenciamento de um catálogo de filmes, construída com **FastAPI** e **Python**. Permite listar, buscar, adicionar e remover filmes.

---

## 📌 Sobre o Projeto

Este projeto é uma API RESTful simples e funcional que realiza operações **CRUD** (Create, Read, Delete) em um catálogo de filmes. Foi desenvolvido com o framework **FastAPI**, que oferece alta performance e documentação interativa automática via Swagger UI.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| [Python 3.14](https://www.python.org/) | Linguagem de programação |
| [FastAPI](https://fastapi.tiangolo.com/) | Framework web de alta performance |
| [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI para rodar a API |

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.8+ instalado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/gianellimurilo/minha-api-filmes.git

# 2. Acesse a pasta do projeto
cd minha-api-filmes

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente virtual
# Windows (PowerShell):
venv\Scripts\Activate
# Linux/Mac:
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Rode a API
uvicorn main:app --reload
```

A API estará disponível em: **http://127.0.0.1:8000**

📄 Documentação interativa (Swagger): **http://127.0.0.1:8000/docs**

---

## 📡 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/filmes` | Lista todos os filmes |
| `GET` | `/filmes/{filme_id}` | Busca um filme pelo ID |
| `POST` | `/filmes` | Adiciona um novo filme |
| `DELETE` | `/filmes/{filme_id}` | Remove um filme pelo ID |

---

## 📦 Exemplo de Resposta

### `GET /filmes`

```json
[
    {
        "id": 1,
        "titulo": "Interestelar",
        "nota": 9.5
    },
    {
        "id": 2,
        "titulo": "Matrix",
        "nota": 9.0
    },
    {
        "id": 3,
        "titulo": "Senhor dos Anéis",
        "nota": 9.8
    }
]
```

### `GET /filmes/1`

```json
{
    "id": 1,
    "titulo": "Interestelar",
    "nota": 9.5
}
```

### `POST /filmes?titulo=Oppenheimer&nota=9.2`

```json
{
    "id": 4,
    "titulo": "Oppenheimer",
    "nota": 9.2
}
```

### `DELETE /filmes/1`

```json
{
    "mensagem": "Filme removido com sucesso"
}
```

---

## 🛣️ Melhorias Futuras

- [ ] Adicionar rota `PUT` para atualizar filmes
- [ ] Conectar a um banco de dados (SQLite / PostgreSQL)
- [ ] Adicionar autenticação com JWT
- [ ] Deploy online (Render / Railway)
- [ ] Testes automatizados com Pytest

---

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

Feito por **Murilo Gianelli** — [GitHub](https://github.com/gianellimurilo)
