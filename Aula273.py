from collections import namedtuple
from typing import NamedTuple


class Carta2(NamedTuple):
    valor: str = "VALOR"
    naipe: str = "NAIPE"


Carta = namedtuple("Carta", ["valor", "naipe"])


lista_naipe_1 = []
lista_naipe_2 = []

as_espadas = Carta("A", "♠️")
as_copas = Carta("A", "♥️")
as_ouros = Carta("A", "♦️")
as_paus = Carta("A", "♣️")

lista_naipe_1.extend([as_espadas, as_copas, as_ouros, as_paus])

as_espadas2 = Carta("A", "♠️")
as_copas2 = Carta("A", "♥️")
as_ouros2 = Carta("A", "♦️")
as_paus2 = Carta("A", "♣️")

lista_naipe_2.extend([as_espadas2, as_copas2, as_ouros2, as_paus2])

for carta in lista_naipe_1:
    print(carta)

for carta in lista_naipe_2:
    print(carta)
