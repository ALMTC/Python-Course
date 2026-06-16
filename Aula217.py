class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class Ferramenta:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    
escritor = Escritor('João')
caneta = Ferramenta('Caneta')   
maquina_escrever = Ferramenta('Maquina de Escrever')

escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())

escritor.ferramenta = maquina_escrever
print(escritor.ferramenta.escrever())