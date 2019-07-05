"""
Helper para jogo War
--------------------
Digite os nomes dos jogares para definir
quem joga primeiro. Deixe em branco pra avançar
Diga qtos dados serão usados no ataque e na defesa
Deixe em branco para sair
"""

# Pegando jogadores
from random import shuffle
from random import randint

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

print('-'*30)
for i, jogador in enumerate(jogadores):
    print(f'{i+1}° - {jogador}')

jogador = 0
while True:
    print('-'*30)
    print(f'\033[1;34m{jogadores[jogador]}\033[m jogando...')
    ataque = input('Ataque (1 a 3): ')
    if not ataque.isnumeric():
        break
    defesa = input('Defesa (1 a 3): ')
    if not defesa.isnumeric():
        break
    
    defesa = int(defesa)
    ataque = int(ataque)
    
    if defesa > 3: defesa = 3
    if defesa < 1: defesa = 1
    if ataque > 3: ataque = 3
    if ataque < 1: ataque = 1
    
    dados_def = []
    dados_atq = []
    
    for i in range(0,defesa):
        dados_def.append(randint(1,6))
    for i in range(0,ataque):
        dados_atq.append(randint(1,6))
   
    print('-'*30)
    print(f'\033[1;31mAtaque\033[m: {sorted(dados_atq, reverse=True)}')
    print(f'\033[1;33mDefesa\033[m: {sorted(dados_def, reverse=True)}')
    print('-'*30)
    
    opcao = input('Outro ataque [s/n]? ').strip()
    if not opcao:
        break
    if opcao in 'Nn':
        jogador += 1
        if jogador >= len(jogadores):
            jogador = 0

print('-'*30)
print('\033[1;32mFim de Jogo!\033[m')
