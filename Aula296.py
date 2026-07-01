import csv
from pathlib import Path

NOME_ARQUIVO = "Aula296.csv"
CAMINHO_ARQUIVO = Path(__file__).parent / NOME_ARQUIVO

with open(CAMINHO_ARQUIVO, "r", encoding="utf8") as arquivo:
    arquivo_csv = csv.reader(arquivo)

    for linha in arquivo_csv:
        print(linha[0], linha[1], linha[2])

with open(CAMINHO_ARQUIVO, "r", encoding="utf8") as arquivo:
    arquivo_csv = csv.DictReader(arquivo)

    for linha in arquivo_csv:
        print(linha)
