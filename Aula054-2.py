hora = input("Digite a hora: ")
hora_int = None
try:
    hora_int = int(hora)
    if hora_int is not None and 0 <= hora_int < 24:
        if 0 <= hora_int < 11:
            print("Bom dia!")
        elif 11 <= hora_int < 17:
            print("Boa tarde!")
        elif 17 <= hora_int < 24:
            print("Boa noite!")
        else:
            print("Desculpe, você não digitou uma hora válida.")
except:
    print("Desculpe, você não digitou uma hora válida.")