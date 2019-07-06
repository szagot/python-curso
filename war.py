"""
Helper para jogo War
--------------------
Digite os nomes dos jogares para definir
quem joga primeiro. Deixe em branco pra avançar
Diga qtos dados serão usados no ataque e na defesa
Deixe em branco para sair
"""


def amend_color(text, color='gray', bg='none', style='none', length=0, space=0, align='left'):
    """
    Devolve um texto formatado usando cores para terminal

    :param str text: Texto a ser formatado
    :param str color: Cor do texto. (none|white|red|green|yellow|blue|pink|cyan|gray)
    :param str bg: Cor do fundo. (none|white|red|green|yellow|blue|pink|cyan|gray)
    :param str style: Estilo do texto. (none|bold|underline|negative)
    :param inr space: Espaços a serem colocados antes e depois do texto
    :param int length: Tamanho do texto formatado
    :param str align: Alinhamento do texto dentro do tamanho informado (left|right|center)

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
    formatted_text += f'm{text:{aligns[align]}{length}}\033[m'

    return formatted_text


from random import shuffle
from random import randint

tela = 40

# Pegando jogadores
jogadores = []
while True:
    jogador = input('Jogador: ').strip().title()
    if not jogador:
        break
    jogadores.append(jogador)

if len(jogadores) < 2:
    print('Não tem gente o suficiente pra jogar War')
    exit()

# Definindo ordem de jogo
shuffle(jogadores)

print('-' * tela)
for i, jogador in enumerate(jogadores):
    print(f'{i + 1}° - {jogador}')

jogador = 0
while True:
    print('-' * tela)
    print(f'{amend_color(jogadores[jogador], color="white", style="negative", length=tela, align="center")}')
    ataque = input('Ataque (1 a 3): ')
    if not ataque.isnumeric():
        break
    defesa = input('Defesa (1 a 3): ')
    if not defesa.isnumeric():
        break

    defesa = int(defesa)
    ataque = int(ataque)

    if defesa > 3:
        defesa = 3
    if defesa < 1:
        defesa = 1
    if ataque > 3:
        ataque = 3
    if ataque < 1:
        ataque = 1

    dados_def = []
    dados_atq = []

    for i in range(0, defesa):
        dados_def.append(randint(1, 6))
    for i in range(0, ataque):
        dados_atq.append(randint(1, 6))

    print('-' * tela)
    print(f'{amend_color("Ataque:", color="red", style="bold")} {sorted(dados_atq, reverse=True)}')
    print(f'{amend_color("Defesa:", color="yellow", style="bold")} {sorted(dados_def, reverse=True)}')
    print('-' * tela)

    opcao = input('Outro ataque [s/n]? ').strip()
    if not opcao:
        break
    if opcao in 'Nn':
        jogador += 1
        if jogador >= len(jogadores):
            jogador = 0

print('-' * tela)
print(amend_color('Fim de Jogo!', color='green', style='bold'))
