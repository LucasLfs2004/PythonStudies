status = True

while status:
    notas = 0
    for i in range(2):
        continua = True
        while continua:
            nota = float(input())
            if nota >= 0 and nota <= 10:
                notas += nota
                break
            else:
                print('nota invalida')
    media = notas/2
    print(f"media: {media:.2f}")

    novo_calculo = 0
    while novo_calculo != 1 or novo_calculo != 2:
        novo_calculo = int(input('novo calculo (1-sim 2-nao)'))
        if novo_calculo == 1:
            break
        elif novo_calculo == 2:
            status = False
            break
        else:
            continue
