nome_arquivo = "Aula188.txt"
caminho_arquivo = "D:\\Python Course\\"
caminho_arquivo_completo = caminho_arquivo + nome_arquivo

# print(caminho_arquivo_completo)

#Versão sem with
# arquivo = open(caminho_arquivo_completo, "w")
# print("Escrevendo no arquivo...")
# arquivo.close()

#Versão com with
with open(caminho_arquivo_completo, "w+") as arquivo:
    arquivo.write("Hello, World!\n")
    arquivo.write("Segunda Linha\n")
    #arquivo.seek(0,0) 
    arquivo.writelines(["Terceira Linha\n", "Quarta Linha\n"])
    arquivo.seek(0,0)

    print("#" * 20)

    arquivo.seek(0,0)
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print("#" * 20)
    
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

with open(caminho_arquivo_completo, "r") as arquivo:
    print(arquivo.read())