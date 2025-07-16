frase = "lorem ipsum dolor sit amet, consectetur adipiscing elit"

frase.lower()

i = 0
letra_mais_repetida = []
numero_repeticoes = 0

while i < len(frase):
    letra = frase[i]

    repeticoes = frase.count(letra)
    if repeticoes >= numero_repeticoes and letra != ' ':
        letra_mais_repetida = letra
        numero_repeticoes = repeticoes

    i += 1

print(f"A letra mais repetida é '{letra_mais_repetida}' com {numero_repeticoes} repetições.")