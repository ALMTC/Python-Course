primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor == segundo_valor:
    print(f"{primeiro_valor=} é igual a {segundo_valor=}")
elif primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior que {segundo_valor=}")
else:
    print(f"{segundo_valor=} é maior que {primeiro_valor=}")