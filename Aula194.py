import json
import os
import copy

lista_de_tarefas = []
lista_de_tarefas_maxima = []

def exibir_lista(lista_de_tarefas):
    #limpar_tela()
    print("Tarefas:\n")
    for tarefa in lista_de_tarefas:
        print(tarefa)
    print("\n")


def adicionar_tarefa(tarefa):
    if len(tarefa) > 0:
        lista_de_tarefas.append(tarefa)
        global lista_de_tarefas_maxima
        lista_de_tarefas_maxima = copy.deepcopy(lista_de_tarefas)
    exibir_lista(lista_de_tarefas)

def desfazer():
    if len(lista_de_tarefas) > 0:
        lista_de_tarefas.pop()
    exibir_lista(lista_de_tarefas)

def refazer():
    tamanho_lista_de_tarefas = len(lista_de_tarefas)
    if tamanho_lista_de_tarefas < len(lista_de_tarefas_maxima):
    
        lista_de_tarefas.append(lista_de_tarefas_maxima[tamanho_lista_de_tarefas])
    exibir_lista(lista_de_tarefas)

def limpar_tela():
    os.system("cls")

def salvar(lista_de_tarefas):
    with open('aula194.json', 'w+',encoding="utf-8") as arquivo:
        json.dump(lista_de_tarefas, arquivo, ensure_ascii=False, indent=2)

def carregar():
    global lista_de_tarefas
    try:
        with open('aula194.json', 'r', encoding="utf-8") as arquivo:
            lista_de_tarefas = json.load(arquivo)
        exibir_lista(lista_de_tarefas)
    except FileNotFoundError:
        print("Nenhum arquivo de tarefas encontrado")
        with open('aula194.json', 'w+',encoding="utf-8") as arquivo:
            json.dump(lista_de_tarefas, arquivo, ensure_ascii=False, indent=2)

verifica = True

while verifica:
    print("Comandos: listar, desfazer, refazer, salvar, sair")
    comando = input("Digite um comando: ").lower()

    if comando == "listar":
        exibir_lista(lista_de_tarefas)

    elif comando == "desfazer":
        desfazer()

    elif comando == "refazer":
        refazer()

    elif comando == "sair":
        verifica = False

    elif comando == "limpar":
        os.system("cls")

    elif comando == "salvar":
        salvar(lista_de_tarefas)

    elif comando == "carregar":
        carregar()
        
    else:
        adicionar_tarefa(comando)