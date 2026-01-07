import requests
from pymongo import MongoClient
import os

# Configurações
TMDB_API_KEY = "c6d86324a69d5052046357e055a61df"
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["movies_db"]
coll = db["movies"]

def buscar_filme(titulo: str):
    """
    Busca informações de um filme pelo título.
    Primeiro tenta encontrar no cache (MongoDB).
    Se não encontrar, consulta a API do TMDb e salva no banco.
    """
    # tenta cache
    filme = coll.find_one({"title": titulo})
    if filme:
        return filme

    # consulta TMDb
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": titulo,
        "language": "pt-BR"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Erro ao consultar TMDb:", response.text)
        return None

    data = response.json()
    if not data.get("results"):
        return None

    first = data["results"][0]
    filme = {
        "title": first.get("title", titulo),
        "year": first.get("release_date", "")[:4],
        # simplificado: plataformas fixas (não é real)
        "platforms": ["Netflix", "Prime Video"]
    }
    coll.insert_one(filme)
    return filme

def main():
    titulo = input("Digite o nome do filme: ").strip()
    if not titulo:
        print("Título inválido.")
        return

    filme = buscar_filme(titulo)
    if not filme:
        print("Filme não encontrado.")
        return

    print(f"\n{filme['title']} ({filme['year']})")
    print("Disponível em:")
    for plataforma in filme["platforms"]:
        print(f"- {plataforma}")

if __name__ == "__main__":
    main()
