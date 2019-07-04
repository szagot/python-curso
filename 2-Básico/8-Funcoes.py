"""
Para declarar uma função, use
    def nomeFuncao():
        comandos
"""


def titulo(tit, tam=0, espaco=2):
    """
    Imprimindo um título
    :param str tit: Título a Ser impresso
    :param int tam: Tamanho mínimo do título
    :param int espaco: Quantidade de espaços entre os títulos
    """
    # Verifica se o tamanho é maior que o tamanho do titulo
    if tam < len(tit):
        tam = len(tit)
    # Adiciona um espaço ao tamanho
    tam += espaco
    # Linha
    print('-' * tam)
    # Titulo centralizado dentro do tamanho
    print(f'{tit.upper():^{tam}}')
    # Linha
    print('-' * tam)


# O asterisco indica um empacotamento. Ele irá pegar todos os valores passados e jogar em uma tupla
def soma(*valores, digits=2):
    """
    Somando valores
    :param float valores: Valores a serem somados
    :param int digits: Número de dígitos para arredondamento
    :return float:
    """
    resultado = 0
    for valor in valores:
        resultado += float(valor)

    return round(resultado, digits)


# Se o parametro for uma lista, é possível trabalhar com a ideia de global (vinculo)
def dobra(lista):
    """
    Dobra os valores de uma lista
    :param list lista: Lista com valores inteiros
    """
    for i in range(0, len(lista)):
        lista[i] *= 2


# Exemplos de funções
titulo('Teste Simples')
titulo('Teste com título maior', 50)
titulo('Teste com informativo de parametro', espaco=10)

# Exemplo de empacotamento
print(soma(2.55, 3.457, 5.123, digits=1))

# Exemplo de valores vinculados
lista = [2, 4, 6, 8]
dobra(lista)
print(lista)
