# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

def zipper(lista1, lista2):
    menor_lista = min(len(lista1), len(lista2))
    # zippered = []

    # for i in range(menor_lista):
    #     zippered.append((lista1[i], lista2[i]))
    # return zippered

    return [(lista1[i], lista2[i]) for i  in range(menor_lista)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

lista_zipper = zipper(l1, l2)
print(lista_zipper)

print(list(zip(l1, l2)))  # Função nativa do Python que faz a mesma coisa
print(list(zip_longest(l1, l2, fillvalue="Sem cidade"))) # Função que une listas considerando a maior lista