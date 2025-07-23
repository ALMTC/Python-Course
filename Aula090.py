import os
lista_de_compras = []

while True:
    print("Lista de compras")
    print ('Escolha uma opção:')
    print ('1 - Adicionar Item')
    print ('2 - Remover Item')
    print ('3 - Listar Itens')
    print ('4 - Sair')
    opcao = input('Opção: ')

    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == '1':
        item = input('Digite o item a ser adicionado: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_de_compras.append(item)
        print(f'Item "{item}" adicionado com sucesso!')

    elif opcao == '2':
        item = input('Digite o número do item a ser removido: ')
        try:
            item = int(item)
            removed_item = lista_de_compras.pop(item)
            print(f'Item "{removed_item}" removido com sucesso!')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
        except IndexError:
            print('Número inválido. Tente novamente.')
        
        """
        if lista_de_compras != []:
            item = input('Digite o número do item a ser removido: ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if item.isdigit():
                item = int(item)
                if 0 <= item < len(lista_de_compras):
                    removed_item = lista_de_compras.pop(item)
                    print(f'Item "{removed_item}" removido com sucesso!')
                else:
                    print('Número inválido. Tente novamente.')
            else:
                print('Entrada inválida. Por favor, digite um número.')
        else:
            print('A lista de compras está vazia. Não há itens para remover.')
        """
    elif opcao == '3':
        if lista_de_compras:
            print('Itens na lista de compras:')
            for i, item in enumerate(lista_de_compras):
                print(f'{i}: {item}')
        else:
            print('A lista de compras está vazia.')
    elif opcao == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
    print()