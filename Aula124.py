perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for i, opcao in enumerate(pergunta['Opções'], start=1):
        print(f"{i}) {opcao}")
    resposta = input("Digite a opção correta: ")

    if resposta == pergunta['Resposta']:
        print("Resposta correta!")
        acertos += 1
    else:
        print(f"Resposta errada! A resposta correta é: {pergunta['Resposta']}")
    print()

print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")