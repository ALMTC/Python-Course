nome = input("Digite seu nome: ")
nome_tamanho = len(nome)
contador = 0
novo_nome = ""

while contador < nome_tamanho:
    novo_nome += f"*{nome[contador]}*"
    contador += 1

print(f"Seu nome com asteriscos: {novo_nome}")