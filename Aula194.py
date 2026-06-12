import os
import copy

def exibir_lista(lista_de_tarefas):
    os.system("cls")
    print("Tarefas:\n")
    for tarefa in lista_de_tarefas:
        print(tarefa)
    print("\n")


def adicionar_tarefa(tarefa, lista_de_tarefas, lista_de_tarefas_maxima):
    if len(tarefa) > 0:
        lista_de_tarefas.append(tarefa)
        lista_de_tarefas_maxima = copy.deepcopy(lista_de_tarefas)
    exibir_lista(lista_de_tarefas)
    exibir_lista(lista_de_tarefas_maxima)

def desfazer(lista_de_tarefas):
    if len(lista_de_tarefas) > 0:
        lista_de_tarefas.pop()
    exibir_lista(lista_de_tarefas)

def refazer(lista_de_tarefas, lista_de_tarefas_maxima):
    tamanho_lista_de_tarefas = len(lista_de_tarefas)
    if tamanho_lista_de_tarefas < len(lista_de_tarefas_maxima):
    
        lista_de_tarefas.append(lista_de_tarefas_maxima[tamanho_lista_de_tarefas])
    exibir_lista(lista_de_tarefas)


verifica = True

lista_de_tarefas = []
lista_de_tarefas_maxima = []

while verifica:
    print("Comandos: listar, desfazer, refazer, sair")
    comando = input("Digite um comando: ").lower()

    if comando == "listar":
        exibir_lista(lista_de_tarefas)

    elif comando == "desfazer":
        desfazer(lista_de_tarefas)

    elif comando == "refazer":
        refazer(lista_de_tarefas, lista_de_tarefas_maxima)

    elif comando == "sair":
        verifica = False

    elif comando == "limpar":
        os.system("cls")

    else:
        adicionar_tarefa(comando, lista_de_tarefas, lista_de_tarefas_maxima)