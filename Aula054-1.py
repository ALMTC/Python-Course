numero = input("Digite um número inteiro: ")

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
except:
    print("Desculpe, você não digitou um número inteiro.")
