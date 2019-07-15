# Tic Tac Toe Game
#   by Szag-Ot
#   2019-07-12
#   V1


def title(tit='', tam=0, espaco=2, character='-'):
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

    if len(tit) == 0:
        return

    # Titulo centralizado dentro do tamanho
    print(f'{tit.upper():^{tam}}')
    # Linha
    print(character * tam)


def print_board():
    """
    Imprime o tabuleiro do jogo
    """
    import os
    # Limpando a Tela
    os.system('cls' if os.name == 'nt' else 'clear') or None
    title('TIC TAC TOE', tam=screen, character='~')
    print('        \033[1;34mA\033[m   \033[1;34mB\033[m   \033[1;34mC\033[m')
    print('      ┌───┬───┬───┐')
    print(f'    \033[1;34m0\033[m │ {board["a"][0]} │ {board["b"][0]} │ {board["c"][0]} │')
    print('      ├───┼───┼───┤')
    print(f'    \033[1;34m1\033[m │ {board["a"][1]} │ {board["b"][1]} │ {board["c"][1]} │')
    print('      ├───┼───┼───┤')
    print(f'    \033[1;34m2\033[m │ {board["a"][2]} │ {board["b"][2]} │ {board["c"][2]} │')
    print('      ──┴───┴───┘')
    title(tam=screen, character='~')


def verify_game():
    """
    Verifica se houve um campeão, ou se deu velha
    :return bool|str: Retorna se houve um campeão/empate ou retorna False
    """
    # Coluna A
    if board['a'][0] == board['a'][1] == board['a'][2] != ' ':
        return f'{board["a"][0]} ganhou!'
    # Coluna B
    elif board['b'][0] == board['b'][1] == board['b'][2] != ' ':
        return f'{board["b"][0]} ganhou!'
    # Coluna C
    elif board['c'][0] == board['c'][1] == board['c'][2] != ' ':
        return f'{board["c"][0]} ganhou!'
    # Linha 0
    elif board['a'][0] == board['b'][0] == board['c'][0] != ' ':
        return f'{board["a"][0]} ganhou!'
    # Linha 1
    elif board['a'][1] == board['b'][1] == board['c'][1] != ' ':
        return f'{board["a"][1]} ganhou!'
    # Linha 2
    elif board['a'][2] == board['b'][2] == board['c'][2] != ' ':
        return f'{board["a"][2]} ganhou!'
    # Diagonal A0 -> C2
    elif board['a'][0] == board['b'][1] == board['c'][2] != ' ':
        return f'{board["a"][0]} ganhou!'
    # Diagonal C0 -> A2
    elif board['a'][2] == board['b'][1] == board['c'][0] != ' ':
        return f'{board["a"][2]} ganhou!'
    # Velha
    else:
        is_old = True
        for col in board.values():
            for lin in col:
                # Se tiver uma celula vazia, não acabou ainda
                if lin == ' ':
                    is_old = False
                    break
            # Se encontrou uma celula vazia, já finaliza o laço
            if not is_old:
                break
        if is_old:
            return 'Deu \033[1;34mVelha\033[m!'

    # Se não houve fim de jogo
    return False


def require_game():
    global gamer
    while True:
        player = str(input(f' {gamer} Digite sua Jogada: ')).lower().strip()
        if len(player) == 2 and player[0] in 'abc' and player[1] in '012' and board[player[0]][int(player[1])] == ' ':
            break
        print(' \033[31mJogada inválida!\033[m')
        title(tam=screen, character='.')

    # Adiciona jogada
    board[player[0]][int(player[1])] = gamer
    # Muda o jogador atual
    gamer = o if gamer == x else x


# Tabuleiro
board = {
    'a': [' ', ' ', ' '],
    'b': [' ', ' ', ' '],
    'c': [' ', ' ', ' ']
}

# Peças
o = '\033[1;32mO\033[m'
x = '\033[1;31mX\033[m'

# Jogador Atual
gamer = o

# Tela
screen = 23

# Inicia o game
while True:
    print_board()
    require_game()
    vg = verify_game()
    if vg:
        break

title(tam=screen, character='~')
print(f'\n {vg}\n')
title(tam=screen, character='~')
