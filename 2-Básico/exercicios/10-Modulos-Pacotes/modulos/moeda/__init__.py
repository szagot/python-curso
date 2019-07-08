def aumentar(valor=0, percent=100, formatado=False):
    """
    Aumenta em x% o valor informado
    :param float valor: Valor
    :param float percent: Quantidade em % a ser aumentado
    :param bool formatado: Deve ser formatado como dinheiro?
    :return float: valor com aumento
    """
    retorno = valor + (valor * percent / 100)
    return moeda(retorno) if formatado else retorno


def diminuir(valor=0, percent=100, formatado=False):
    """
    Diminui em x% o valor informado
    :param float valor: Valor
    :param float percent: Quantidade em % a ser aumentado
    :param bool formatado: Deve ser formatado como dinheiro?
    :return float: valor com aumento
    """
    retorno = valor - (valor * percent / 100)
    return moeda(retorno) if formatado else retorno


def dobro(valor=0, formatado=False):
    """
    Devolve o dobro do valor
    :param float valor:
    :param bool formatado: Deve ser formatado como dinheiro?
    :return float:
    """
    retorno = valor * 2
    return moeda(retorno) if formatado else retorno


def metade(valor=0, formatado=False):
    """
    Devolve a metade do valor
    :param float valor:
    :param bool formatado: Deve ser formatado como dinheiro?
    :return float:
    """
    retorno = valor / 2
    return moeda(retorno) if formatado else retorno


def moeda(valor, cifra='R$'):
    """
    Devolve um valor no formato brasileiro, adicionando a cifra da moeda
    :param float valor:
    :param str cifra:
    :return str:
    """
    return f'{cifra} {valor:.2f}'.replace('.', ',')


def resumo(valor=0, reducao=0, aumento=0):
    from modulos import texto

    texto.titulo('RESUMO DO VALOR', 30)
    print(f'{"Preço analisado:":<18}{moeda(valor):>12}')
    print(f'{"Dobro do Preço:":<18}{dobro(valor, True):>12}')
    print(f'{"Metade do Preço:":<18}{metade(valor, True):>12}')
    print(f'{f"{aumento}% de aumento:":<18}{aumentar(valor, aumento, True):>12}')
    print(f'{f"{reducao}% de aumento:":<18}{diminuir(valor, reducao, True):>12}')
    print('-' * 30)
