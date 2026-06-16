import json

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome = "", idade = 0, genero = "", endereco = ""):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = self.ano_atual = self.idade
        self.genero = genero
        self.endereco = endereco

    def salvar(self):
        with open('aula208.json', 'w+',encoding="utf-8") as arquivo:
            json.dump(self.__dict__, arquivo, ensure_ascii=False, indent=2)

    def carregar(self, caminho):
        try:
            with open(caminho, 'r', encoding="utf-8") as arquivo:
                self.__dict__ = json.load(arquivo)
            
        except FileNotFoundError:
            print("Nenhum arquivo de tarefas encontrado")

pessoa =  Pessoa("Luiz", 25, "masculino", "Rua 10")

pessoa.salvar()

pessoa_copia = Pessoa()

pessoa_copia.carregar('aula208.json')

print(f'Dados pessoa = {pessoa.__dict__}')
print(f'Dados pessoa_copia = {pessoa_copia.__dict__}')