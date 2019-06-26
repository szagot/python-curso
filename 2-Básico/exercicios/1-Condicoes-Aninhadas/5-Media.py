# Define a situação de um aluno
from coresTerminal import cores

n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
media = (n1 + n2) / 2

if media < 5:
    print(cores['red'], 'Aluno Reprovado', cores['reset'])
elif media >= 7:
    print(cores['green'], 'Aluno Aprovado', cores['reset'])
else:
    print(cores['yellow'], 'Aluno em Recuperação', cores['reset'])
