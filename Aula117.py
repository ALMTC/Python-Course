def criar_multiplicação(multiplicador):
    def multiplicar(multiplicando):
        return f'{multiplicando} x {multiplicador} = {multiplicando * multiplicador}'
    return multiplicar

duplica = criar_multiplicação(2)
triplica = criar_multiplicação(3)
quadruplica = criar_multiplicação(4)
quitruplica = criar_multiplicação(5)

valor = int(input("Digite um número: "))

print(duplica(valor))
print(triplica(valor))
print(quadruplica(valor))
print(quitruplica(valor))