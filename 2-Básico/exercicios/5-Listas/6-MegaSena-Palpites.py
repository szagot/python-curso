# Gerando palpites para Mega Sena
from random import shuffle
from time import sleep

qt = int(input('Quantos palpites você quer? '))
print('-=' * 30 + '-')
palpites = []
if qt > 0:
    for i in range(0, qt):
        lista = list(range(1, 61))
        shuffle(lista)
        palpites.append(lista[:6])
        lista.clear()

    for i, palpite in enumerate(palpites):
        sleep(.5)
        print(f'Jogo {i+1}: {palpite}')

print('-=' * 30 + '-')
print('Volte Sempre!')
