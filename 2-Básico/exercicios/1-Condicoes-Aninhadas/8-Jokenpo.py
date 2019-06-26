# Jokenpô

from coresTerminal import cores
from random import choice
from time import sleep
import emoji

print('-=' * 20 + '-')
print('{:^41}'.format('JOKENPO'))
print('-=' * 20 + '-')

user = input('Escolha Pedra, Papel ou Tesoura: ').lower().strip()
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)

if user not in lista:
    print(cores['red'] + 'Opção inválida!', cores['reset'])
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 20 + '-')

if user == pc:
    print((cores['yellow'] + '{:^41}' + cores['reset']).format('Empate!'))
elif (pc == 'pedra' and user == 'tesoura') or (pc == 'tesoura' and user == 'papel') or (
        pc == 'papel' and user == 'pedra'):
    print((cores['red'] + '{:^41}' + cores['reset']).format('Você perdeu!'))
else:
    print((cores['green'] + '{:^41}' + cores['reset']).format('Você ganhou!!!'))

emojis = {
    'pedra': ':facepunch:',
    'papel': ':hand:',
    'tesoura': ':v:'
}

print('-=' * 20 + '-')
print(
    ' ' * 5,
    'Computador', cores['blackWhite'], emoji.emojize(emojis[pc], use_aliases=True), cores['reset'],
    'x', cores['blackWhite'], emoji.emojize(emojis[user], use_aliases=True), cores['reset'], 'Jogador'
)
print('-=' * 20 + '-')
