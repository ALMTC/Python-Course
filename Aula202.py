class Carro:

    def __init__(self, modelo, ano, aceleracao, velocidade_maxima) -> None:
        self.modelo = modelo
        self.ano = ano
        self.aceleracao = aceleracao
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self):
        if self.velocidade_atual < self.velocidade_maxima:
            if self.velocidade_atual >= self.velocidade_maxima - self.aceleracao:
                self.velocidade_atual = self.velocidade_maxima
            else:
                self.velocidade_atual += self.aceleracao
        print(f"O {self.modelo} está acelerando. Sua velocidade atual é {self.velocidade_atual} Sua velocidade máxima é {self.velocidade_maxima}")
    
    def frear(self):
        self.velocidade_atual = 0
        print(f"O {self.modelo} freou, sua velocidade atual é {self.velocidade_atual}")
    
    def buzinar(self):
        print('BiBiiiiii')

fusca = Carro('Fusca', '1980', 10, 180)
uno = Carro('Uno', '1996', 15, 200)

fusca.acelerar()
uno.acelerar()
fusca.acelerar()
uno.acelerar()
fusca.acelerar()
uno.acelerar()
fusca.buzinar()
uno.acelerar()
fusca.frear()
uno.frear()
