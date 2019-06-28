# Jogo de adivinha
from random import randint

pc = randint(0, 10)
user = -1
palpites = 0
acertou = False
while not acertou:
    user = int(input('Que número estou pensando (de 0 a 10)? '))
    palpites += 1
    if pc == user:
        acertou = True
    else:
        print('É menos...' if pc < user else 'É mais...', 'Tente mais uma vez')

print('Acertou com {} tentativa(s)! Parabéns!'.format(palpites))
