import json
from pathlib import Path

NOME_ARQUIVO = "Aula293.json"
CAMINHO_ARQUIVO = Path(__file__).parent / NOME_ARQUIVO

print(CAMINHO_ARQUIVO)

filme = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None,
}

with open(CAMINHO_ARQUIVO, "w+", encoding="utf8") as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ARQUIVO, "r", encoding="utf8") as arquivo:
    filme2 = json.load(arquivo)

    print(filme2)
