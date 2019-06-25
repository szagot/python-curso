from random import choice

aluno = [
    input('Nome do aluno 1: '),
    input('Nome do aluno 2: '),
    input('Nome do aluno 3: '),
    input('Nome do aluno 4: ')
]

# Escolhe um item da lista
escolhido = choice(aluno)

print('O escolhido foi o {}'.format(escolhido))
