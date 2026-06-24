# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): #define o que vai ser exibido quando o objeto for printado (mais voltado para programadores, para mostrar o que eu quero da construção do objeto)
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'
    
    def __add__(self, other):
        x_soma = self.x + other.x
        y_soma = self.y + other.y
        return Ponto(x_soma, y_soma)
        
    def __gt__(self, other):
        self_tamanho = (self.x**2 + self.y**2)**0.5
        other_tamanho = (other.x**2 + other.y**2)**0.5
        if self_tamanho > other_tamanho:
            return True
        return False
    
    def __lt__(self, other):
        self_tamanho = (self.x**2 + self.y**2)**0.5
        other_tamanho = (other.x**2 + other.y**2)**0.5
        if self_tamanho < other_tamanho:
            return True
        return False

p1 = Ponto(1,2)
p2 = Ponto(46,98)
p3 = p1 + p2

print(p1)
print(repr(p2))
print(f'{p2!r}')
print(p3)
print('P1 é maior que p2?', p1 > p2)
print('P1 é menpr que p2?', p1 < p2)