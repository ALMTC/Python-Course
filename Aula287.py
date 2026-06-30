import os
from pathlib import Path

caminho = Path(__file__).parent

for root, dirs, files in os.walk(caminho):
    print(f"Caminho: {root}")

    for dir_ in dirs:
        print(f"    Dir: {dir_}")

    for file_ in files:
        print(f"        File: {file_}")
