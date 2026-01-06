import requests
from pymongo import MongoClient
import os

# Configurações
TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "")  # coloque sua chave TMDb
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["movies_db"]
coll = db["movies"]

def buscar_filme(titulo: str):
    # tenta cache
    filme = coll.find_one({"title": titulo})
    if filme:
        return filme

    # consulta TMDb
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": titulo, "language": "pt-BR"}
    r = requests.get(url, params=params).json()

    if not r.get("results"):
        return None

    first = r["results"][0]
    filme = {
        "title": first["title"],
        "year": first.get("release_date", "")[:4],
        # simplificado: plataformas fixas
        "platforms": ["Netflix", "Prime Video"]
    }
    coll.insert_one(filme)
    return filme

def main():
    titulo = input("Digite o nome do filme: ")
    filme = buscar_filme(titulo)
    if not filme:
        print("Filme não encontrado.")
        return

    print(f"\n{filme['title']} ({filme['year']})")
    print("Disponível em:")
    for p in filme["platforms"]:
        print(f"- {p}")

if __name__ == "__main__":
    main()
