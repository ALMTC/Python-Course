def multiplicar(*numero):
    resultado = 1
    for n in numero:
        print(f"Multiplicando: {n}")
        resultado *= n
    return resultado

def validar_impar_par(numero):
    if numero % 2 == 0:
        return f"{numero} é par."
    else:
        return f"{numero} é ímpar."

print("Escolha a função que deseja executar:")
escolha = input("1 - Multiplicar\n2 - Validar Impar/Par\n")

if escolha == "1":
    número = (1,5,10,15,20)
    print("Os números são:", número)

    print("O resultado da multiplicação é:", multiplicar(*número))
elif escolha == "2":
    numero = int(input("Digite um número para validar se é par ou ímpar: "))
    print(validar_impar_par(numero))
