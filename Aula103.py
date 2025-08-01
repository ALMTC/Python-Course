from random import randint

numero_bese = ""
digito_verificador_1 = 0
digito_verificador_2 = 0

for i in range(9):
    numero_bese += str(randint(0, 9))

print(f"Número base gerado: {numero_bese}")

for i in range(9):
    digito = numero_bese[i]
    digito_verificador_1 += int(digito) * (10 - i)

digito_verificador_1 *= 10
digito_verificador_1 %= 11

numero_bese += str(0 if digito_verificador_1 >= 10 else digito_verificador_1)

for i in range(10):
    digito = numero_bese[i]
    digito_verificador_2 += int(digito) * (11 - i)

digito_verificador_2 *= 10
digito_verificador_2 %= 11

numero_bese += str(0 if digito_verificador_2 >= 10 else digito_verificador_2)

print(f"CPF gerado: {numero_bese}")