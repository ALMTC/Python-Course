import os

palavra = "espaguete"
palavra_adivinhada = "*" * len(palavra)
tentativas = 0

while "*" in palavra_adivinhada:
    letra = input("Digite uma letra: ").lower()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, insira apenas uma letra.")
        continue

    tentativas += 1

    if letra in palavra:
        nova_palavra_adivinhada = ""
        for i in range(len(palavra)):
            if palavra[i] == letra:
                nova_palavra_adivinhada += letra
            else:
                nova_palavra_adivinhada += palavra_adivinhada[i]
        palavra_adivinhada = nova_palavra_adivinhada
    print(f"Palavra atual: {palavra_adivinhada}")

os.system('cls' if os.name == 'nt' else 'clear')
print(f"Parabéns! Você adivinhou a palavra '{palavra}' em {tentativas} tentativas.")