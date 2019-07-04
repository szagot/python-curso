# Verifica qual é o número maior


def maior(*valores):
    retorno = 0
    for valor in valores:
        if retorno == 0 or valor > retorno:
            retorno = valor

    return retorno


print(maior(1, 10, 15, 20, 30, 99, 4))
