nome = input("Digite seu primero nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 1:
    print("Desculpe, você não digitou um nome válido.")
elif tamanho_nome <= 4:
    print(f"{nome} é um nome curto.")
elif tamanho_nome <= 6:
    print(f"{nome} é um nome normal.")
else:
    print(f"{nome} é um nome grande.")