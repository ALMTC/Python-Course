import os
from pathlib import Path

caminho = Path(__file__).parent
lista_arquivos = os.listdir(caminho)


for item in lista_arquivos:
    full_path = os.path.join(caminho, item)
    if not os.path.isdir(full_path):
        print(item)
        continue
    for arch in os.listdir(full_path):
        print(arch)
