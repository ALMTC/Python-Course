class Carro:
    def __init__(self, nome, fabricante = None, motor = None):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome

    def exibe_dados(self):
        print(f'O carro {self.nome} é fabricado pela {self.fabricante.nome} e possui o motor {self.motor.nome}')

class Motor:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

fabrica1 = Fabricante('F1')
fabrica2 = Fabricante('F2')

motor1 = Motor('Motor Forte')
motor2 = Motor('Motor Fraco')

c1 = Carro('Gol', fabrica1, motor2)
c2 = Carro('Uno')
c3 = Carro('Fusca', fabrica2, motor1)

c2.motor = motor1
c2.fabricante = fabrica2

c1.exibe_dados()
c2.exibe_dados()
c3.exibe_dados()