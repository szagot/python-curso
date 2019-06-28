# Jogo de par ou ímpar
from random import randint

vitorias = 0
print('=' * 30)
print(f'{"PAR ou ÍMPAR" :^30}')

while True:
    print('=' * 30)
    pc = randint(0, 10)
    user = int(input('Digite um valor de 0 a 10: '))
    tipo = input('Você quer [P]ar ou [I]mpar? ').strip().upper()[0]
    soma = pc + user
    ePar = soma % 2 == 0
    print(f'Você jogou {user} e o computador {pc}. Total: {soma}. Deu', 'PAR!' if ePar else 'ÍMPAR!')
    # Perdeu? Então interrompe
    if (ePar and tipo == 'I') or (not ePar and tipo == 'P'):
        break
    print('Você ganhou! Vamos mais uma...')
    vitorias += 1

print('Você Perdeu, Mané!')
print('=' * 30)
print(f'Você venceu {vitorias} vezes!')
