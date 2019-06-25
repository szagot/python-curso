from random import shuffle

aluno = [
    input('Nome do aluno 1: '),
    input('Nome do aluno 2: '),
    input('Nome do aluno 3: '),
    input('Nome do aluno 4: ')
]

# Embaralha a lista
shuffle(aluno)

print('A ordem de apresentação será {}'.format(aluno))
