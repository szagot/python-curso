"""
if condicao:
    bloco de comandos
elif condicao:
    bloco de comandos
else:
    bloco de comandos
"""

from coresTerminal import cores

nome = input('Qual o seu nome? ')

if nome == 'Daniel':
    print('Amei o seu nome!')
elif nome == 'Alini':
    print('Mesmo nome da minha esposa!')
elif nome in 'Alunos Alejandro':
    print('Mesmo nome dos meus filhos!')
else:
    print('Que nome diferente!')

print('Muito prazer em te conhecer, {}{}{}'.format(cores['green'], nome, cores['reset']))
