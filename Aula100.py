"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf_cru = "746.824.890-70"
cpf = ""
verificacao_digito_1 = 0
verificacao_digito_2 = 0


for digito in cpf_cru:
    if digito.isdigit():
        cpf += digito

if len(cpf) != 11:
    print("CPF inválido. Deve conter 11 dígitos.")

for i in range(9):
    digito = cpf[i]
    verificacao_digito_1 += int(digito) * (10 - i)

verificacao_digito_1 *= 10
verificacao_digito_1 %= 11

digito_1 = 0 if verificacao_digito_1 >= 10 else verificacao_digito_1

for i in range(10):
    digito = cpf[i]
    verificacao_digito_2 += int(digito) * (11 - i)

verificacao_digito_2 *= 10
verificacao_digito_2 %= 11

digito_2 = 0 if verificacao_digito_2 >= 10 else verificacao_digito_2

if digito_1 == int(cpf[9]) and digito_2 == int(cpf[10]):
    print(f"O CPF {cpf_cru} é válido")
else:
    print(f"O CPF {cpf_cru} é inválido")