# Jogo de dados para 4
from random import randint
from time import sleep

jogadores = []
jogador = {}
for i in range(0, 4):
    jogador['nome'] = input(f'Digite o nome do {i+1}º jogador: ')
    jogador['resultado'] = randint(1, 6)
    print(f'{jogador["nome"]} tirou {jogador["resultado"]} no dado.')
    # Se for o primeiro item ou o último colocado for maior que o atual, adiciona fo final
    if len(jogadores) == 0 or jogadores[-1]['resultado'] > jogador['resultado']:
        jogadores.append(jogador.copy())
    else:
        # Localiza um resultado menor ou igual que o atual
        for pos, j in enumerate(jogadores):
            if j['resultado'] <= jogador['resultado']:
                jogadores.insert(pos, jogador.copy())
                break

# Imprimindo resultados
print('-' * 30)
print('== RANKING DOS JOGADORES ==')
for i, jogador in enumerate(jogadores):
    sleep(0.5)
    print(f'{i+1}º Lugar: {jogador["nome"]} com {jogador["resultado"]}')
