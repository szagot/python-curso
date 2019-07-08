def amend_color(text, color='gray', bg='none', style='none', length=0, space=0, align='left', close_after=True):
    """
    Devolve um texto formatado usando cores para terminal

    :param str text: Texto a ser formatado
    :param str color: Cor do texto. (none|white|red|green|yellow|blue|pink|cyan|gray)
    :param str bg: Cor do fundo. (none|white|red|green|yellow|blue|pink|cyan|gray)
    :param str style: Estilo do texto. (none|bold|underline|negative)
    :param inr space: Espaços a serem colocados antes e depois do texto
    :param int length: Tamanho do texto formatado
    :param str align: Alinhamento do texto dentro do tamanho informado (left|right|center)
    :param bool close_after: É pra fechar a cor ao finalizar?

    :return str: Texto formatado

    Criado por Szag-Ot, 2019-07-06
    v1.0
    """

    colors = ('white', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'gray')
    styles = ('none', 'bold', False, False, 'underline', False, False, 'negative')
    aligns = {'left': '<', 'right': '>', 'center': '^'}

    color = color.strip().lower()
    bg = bg.strip().lower()
    style = style.strip().lower()
    align = align.strip().lower()

    # Verifica se a cor informada é válida
    if color not in colors or color == 'none':
        color = colors[7]
    # Verifica se o estilo informado é válido
    if style not in styles:
        style = styles[0]
    # Verifica alinhamento
    if align not in aligns.keys():
        align = 'left'

    # Montando as cores
    formatted_text = f'\033[{styles.index(style)};3{colors.index(color)}'
    if bg in colors:
        formatted_text += f';4{colors.index(bg)}'
    # Adiciona tamanho se o informado for inferior ao tamanho do texto
    if length < len(text):
        length = len(text)
    # Adiciona espaçamento
    if space > 0:
        text = f'{" ":<{space}}{text}{" ":<{space}}'
    formatted_text += f'm{text:{aligns[align]}{length}}'
    if close_after:
        formatted_text += '\033[m'

    return formatted_text


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
