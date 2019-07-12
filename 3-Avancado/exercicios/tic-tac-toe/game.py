# Tic Tac Toe Game
def print_board():
    """
    Imprime o tabuleiro do jogo
    """
    global board
    print('\n' * 100)
    print('     \033[1;34mA\033[m   \033[1;34mB\033[m   \033[1;34mC\033[m')
    print('   ┌───┬───┬───┐')
    print(f'\033[1;34m0\033[m  │ {board["a"][0]} │ {board["b"][0]} │ {board["c"][0]} │')
    print('   ├───┼───┼───┤')
    print(f'\033[1;34m1\033[m  │ {board["a"][1]} │ {board["b"][1]} │ {board["c"][1]} │')
    print('   ├───┼───┼───┤')
    print(f'\033[1;34m2\033[m  │ {board["a"][2]} │ {board["b"][2]} │ {board["c"][2]} │')
    print('   └───┴───┴───┘')


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


# Tabuleiro
board = {
    'a': [' ', ' ', ' '],
    'b': [' ', ' ', ' '],
    'c': [' ', ' ', ' ']
}

# Peças
o = '\033[1;32mO\033[m'
x = '\033[1;31mX\033[m'

board['a'][0] = x
board['a'][1] = o
board['a'][2] = x
board['b'][0] = o
board['b'][1] = o
board['b'][2] = x
board['c'][0] = x
board['c'][1] = x
board['c'][2] = o
print_board()

print(verify_game())
