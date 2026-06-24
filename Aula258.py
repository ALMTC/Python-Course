"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
--Criar classe Cliente que herda da classe Pessoa (Herança)
    --Pessoa tem nome e idade (com getters)
    --Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
--Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    --ContaCorrente deve ter um limite extra
    --Contas têm agência, número da conta e saldo
    --Contas devem ter método para depósito
    --Conta (super classe) deve ter o método sacar abstrato (Abstração e
    --polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta: Conta | None = None) -> None:  # noqa: F821
        super().__init__(nome, idade)
        self.conta = conta

    def depositar(self, valor, banco: Banco):  # noqa: F821
        if banco.verifica_conta_user(self):
            self.conta.depositar(valor, banco)  # type: ignore
            return

        print(f"Usuário ou conta não pertencem ao banco {banco.nome}")

    def sacar(self, valor, banco: Banco):  # noqa: F821
        if banco.verifica_conta_user(self):
            self.conta.sacar(valor, banco)  # type: ignore
            return

        print(f"Usuário ou conta não pertencem ao banco {banco.nome}")


class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo=0) -> None:
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    def depositar(self, valor: int | float, banco: Banco):  # noqa: F821
        self.saldo += valor
        print(f"Saldo depositado com sucesso. Novo saldo R${self.saldo}")

    @abstractmethod
    def sacar(valor): ...


class Banco:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.clientes = []
        self.contas = []
        self.agencias = []

    def adiciona_agencia(self, numero):
        self.agencias.append(numero)
        print(f"A agencia {numero} foi adicionada com sucesso")

    def criar_conta(
        self, cliente: Cliente, tipo, agencia, num_conta, saldo=0, limite=100
    ):
        conta = None
        if tipo in ["Corrente", "corrente"]:
            conta = ContaCorrente(agencia, num_conta, saldo, limite)
        elif tipo in ["Poupanca", "poupanca", "Poupança", "poupança"]:
            conta = ContaPoupanca(agencia, num_conta, saldo)
        else:
            print("Tipo de conta inesistente")
            return

        self.clientes.append(cliente)
        self.contas.append(conta)
        return conta

    def verifica_conta_user(self, cliente: Cliente) -> bool:
        if (cliente.conta in self.contas) and (cliente in self.clientes):
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, agencia, num_conta, saldo=0, limite=0) -> None:
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor: int | float, banco: Banco):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print(
                f"Você sacou R${valor}\nSeu novo saldo é R${self.saldo}\nSeu limite negativo é R${self.limite}"
            )
            return self.saldo
        print(
            f"Saldo insuficiente para sacar R${valor}\nSeu saldo é R${self.saldo}\nSeu limite negativo é R${self.limite}\nVocê pode sacar apenas R${self.limite + self.saldo}"
        )
        return self.saldo


class ContaPoupanca(Conta):
    def __init__(self, agencia, num_conta, saldo=0):
        super().__init__(agencia, num_conta, saldo)

    def sacar(self, valor: int | float, banco: Banco):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Você sacou R${valor}\nSeu novo saldo é R${self.saldo}")
            return self.saldo
        print(f"Saldo insuficiente para sacar R${valor}\nSeu saldo é R${self.saldo}")
        return self.saldo


c1 = Cliente("Lucas", 30)
c2 = Cliente("João", 25)

caixa = Banco("Caixa")
inter = Banco("Inter")

caixa.adiciona_agencia(1000)
caixa.adiciona_agencia(1001)
inter.adiciona_agencia(2000)
inter.adiciona_agencia(2001)

c1.conta = caixa.criar_conta(c1, "poupança", 100, "0001", 2000)
c1.conta = caixa.criar_conta(c1, "poupança", 1001, "0001", 2000)
c2.conta = inter.criar_conta(c2, "corrente", 2000, 1010, 100, 1000)

c1.depositar(100, inter)
c1.depositar(100, caixa)
c2.depositar(200, inter)

c1.sacar(2000, inter)
c1.sacar(2000, caixa)
c1.sacar(300, caixa)
c2.sacar(400, inter)
c2.sacar(1000, inter)
