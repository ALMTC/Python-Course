from dataclasses import dataclass  # dataclass é um facilitador de código


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


p1 = Pessoa("Lucas", "Correia", 30)
p2 = Pessoa("Lucas", "Correia", 30)

print(p1)
print(p2)
print(p1 == p2)
