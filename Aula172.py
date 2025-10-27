"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

from itertools import zip_longest

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def somar_listas(lista1,lista2):
    menor = min(len(lista1), len(lista2))
    return [lista1[i] + lista2[i] for i in range(menor)]

lista_somav1 = somar_listas(lista_a, lista_b)
lista_somav2 = [x + y for x, y in zip(lista_a, lista_b)]
lista_somav3 = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]

print(lista_somav1)
print(lista_somav2)
print(lista_somav3)
