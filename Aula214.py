class Caneta:

    def __init__(self, cor):
        self._cor = cor #_cor o _ antes do atributo é uma conveção, significa que aquela não é uma propriedade a ser utilizada livremente, apenas pela funcão cor. É o equivalente ao private e protect em outras linguagens
        #self.cor = cor # também pode ser feito apenas assim
        self._cor_tampa = self.cor

    @property #funciona como um getter, só que do python
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor
        self.cor_tampa = self.cor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, cor_tampa):
        self._cor_tampa = cor_tampa

caneta_azul = Caneta('azul')

print(caneta_azul.cor)
print(caneta_azul.cor_tampa)
caneta_azul.cor = 'preto'
print(caneta_azul.cor)
print(caneta_azul.cor_tampa)