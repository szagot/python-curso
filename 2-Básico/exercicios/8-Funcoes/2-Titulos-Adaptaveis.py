def titulo(tit, tam=0, espaco=2, character='-'):
    """
    Imprimindo um título
    :param str tit: Título a Ser impresso
    :param int tam: Tamanho mínimo do título
    :param int espaco: Quantidade de espaços entre os títulos
    :param str character: Caracter do título
    """
    # Verifica se o tamanho é maior que o tamanho do titulo
    if tam < len(tit):
        tam = len(tit)
    # Adiciona um espaço ao tamanho
    tam += espaco
    # Linha
    print(character * tam)
    # Titulo centralizado dentro do tamanho
    print(f'{tit.upper():^{tam}}')
    # Linha
    print(character * tam)


titulo('Teste')
titulo('Teste Diferente', character='#')
titulo('Completo', 50, 0, '/')
