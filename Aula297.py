import csv
from pathlib import Path

NOME_ARQUIVO = "Aula297.csv"
CAMINHO_ARQUIVO = Path(__file__).parent / NOME_ARQUIVO


lista_clientes = [
    {"Nome": "Luiz Otávio", "Endereço": "Av 1, 22"},
    {"Nome": "João Silva", "Endereço": 'R. 2, "1"'},
    {"Nome": "Maria Sol", "Endereço": "Av B, 3A"},
]

with open(CAMINHO_ARQUIVO, "w", encoding="utf8") as arquivo:
    nome_colunas = lista_clientes[0].keys()
    writer = csv.writer(arquivo)
    writer.writerow(nome_colunas)
    for item in lista_clientes:
        writer.writerow(item.values())


with open(CAMINHO_ARQUIVO, "w", encoding="utf8") as arquivo:
    nome_colunas = lista_clientes[0].keys()
    writer = csv.DictWriter(arquivo, fieldnames=nome_colunas)
    writer.writeheader()

    for item in lista_clientes:
        writer.writerow(item)
