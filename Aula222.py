class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

class Cliente(Pessoa):

    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

    def apresentar(self):
        super().apresentar()
        print(f'Minha conta é {self.conta}.')

class Aulo(Pessoa):
    def __init__(self, nome, idade, classe):
        super().__init__(nome, idade)
        self.classe = classe

    def apresentar(self):
        super().apresentar()
        print(f'Estou na classe {self.classe}.')

cliente1 = Cliente('João', 30, '12345')
aluno1 = Aulo('Maria', 20, 'A')

cliente1.apresentar()
aluno1.apresentar()