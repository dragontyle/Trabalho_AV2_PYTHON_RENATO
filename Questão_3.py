def horario(h, m):
    if 0 <= h <= 12:
        h = h + 12
        if h == 24:
            h = 0
        print(f"são {h}:{m} P.M")
    elif 12 <= h < 24:
        h = h - 12
        print(f"são {h}:{m} A.M")


def saida():
    from time import sleep
    while True:
        hora = int(input("Digite a hora: "))
        if hora < 0:
            break
        minutos = int(input("Digite os minutos: "))
        print('-'* 34)
        print("REALIZANDO A CONVERSÃO DO HORÁRIO")
        print('-' * 34)
        sleep(1.5)
        horario(hora, minutos)


saida()
