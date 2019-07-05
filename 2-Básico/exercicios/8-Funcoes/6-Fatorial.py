# Fatorial com opcionais


def fatorial(n, show=False):
    """
    Retorna o fatorial de um número inteiro

    :param int n: Valor a ter o fatorial calculado
    :param bool show: Deve mostrar o cálculo?
    :return int: Fatorial
    """
    f = 1
    if n <= 0:
        return 0

    retorno = ''
    for i in range(n, 0, -1):
        f *= i
        if show:
            retorno += str(i) if retorno == '' else f' x {i}'

    if show:
        retorno += ' = '

    return retorno + str(f)


# Fatorial de 5
print(fatorial(5, True))
