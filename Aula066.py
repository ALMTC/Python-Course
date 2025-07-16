while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    operacao = input("Digite a operação (+, -, *, /): ")
    float_numero_1 = None
    float_numero_2 = None
    try:
        float_numero_1 = float(numero_1)
        float_numero_2 = float(numero_2)
    except:
        print("Por favor, insira números válidos.")

    if float_numero_1 is not None or float_numero_2 is not None:
        continue
    
    if operacao in ['+', '-', '*', '/']:
        if operacao == '+':
            print(f"Resultado: {float_numero_1 + float_numero_2:.2f}")
        elif operacao == '-':
            print(f"Resultado: {float_numero_1 - float_numero_2:.2f}")
        elif operacao == '*':
            print(f"Resultado: {float_numero_1 * float_numero_2:.2f}")
        else:
            if float_numero_2 != 0:
                print(f"Resultado: {float_numero_1 / float_numero_2:.2f}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
        continue

    sair = input("Deseja sair? (s/n): ").lower().startswith('s')

    if sair:
        print("Saindo da calculadora.")
        break