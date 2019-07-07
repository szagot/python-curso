def aumentar(valor, percent):
    """
    Aumenta em x% o valor informado
    :param float valor: Valor
    :param float percent: Quantidade em % a ser aumentado
    :return float: valor com aumento
    """
    return valor + (valor * percent / 100)


def diminuir(valor, percent):
    """
    Diminui em x% o valor informado
    :param float valor: Valor
    :param float percent: Quantidade em % a ser aumentado
    :return float: valor com aumento
    """
    return valor - (valor * percent / 100)


def dobro(valor):
    """
    Devolve o dobro do valor
    :param float valor:
    :return float:
    """
    return valor * 2


def metade(valor):
    """
    Devolve a metade do valor
    :param float valor:
    :return float:
    """
    return valor / 2
