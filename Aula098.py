"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_cru = "746.824.890-70"
cpf = ""
verificacao_digito_1 = 0


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

if digito_1 == int(cpf[9]):
    print(f"O primeiro dígito do CPF {cpf_cru} é válido")
else:
    print(f"O primeiro dígito do CPF {cpf_cru} é inválido")