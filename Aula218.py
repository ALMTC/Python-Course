class Carrinho:

    def __init__(self):
        self._produtos = []

    def inserir_produto(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco


p1 = Produto('Caderno', 15.50)
p2 = Produto('Caneta', 1)
carrinho = Carrinho()

carrinho.inserir_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
