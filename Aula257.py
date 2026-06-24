import enum

Direcoes = enum.Enum('Direcoes', ['ESQUERDA','DIREITA', 'CIMA', 'BAIXO'])

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para {direcao.name.lower()}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)