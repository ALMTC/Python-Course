# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import os
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

def copia_profundamente(lista):
    return copy.deepcopy(lista)

def exibir_produtos(lista):
    for item in lista:
        print(item)

print("A lista de produtos é:")
exibir_produtos(produtos)
print('Escolha o que fazer:\n')

while True:

    option = input('Digite 1 para aumentar os preços em 10%\nDigite 2 para ordenar por nome decrescente\nDigite 3 para ordenar por preço crescente\nDigite 4 para sair\n')
    if option == '1':
        lista10 = [{**p,'preco': round(p['preco']*1.1,2)} for p in copia_profundamente(produtos)]

    elif option == '2':
        lista_nome_decrescente = copia_profundamente(produtos)
        lista_nome_decrescente.sort(key=lambda item: item['nome'], reverse=True)
        exibir_produtos(lista_nome_decrescente)

    elif option == '3':
        lista_preco_crescente = copia_profundamente(produtos)
        lista_preco_crescente.sort(key=lambda item: item['preco'])
        exibir_produtos(lista_preco_crescente)

    elif option == '4':
        break
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Opção inválida, tente novamente\n\n')