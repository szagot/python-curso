# Estatísticas

nomeMaisVelho = ''
idadeMaisVelho = 0
mediaIdade = 0
somaIdade = 0
mulheresMenores = 0

print('-' * 20)
for i in range(0, 4):
    print('{}ª pessoa'.format(i + 1))
    nome = input('Nome: ').strip().title()
    sexo = input('Sexo (M ou F): ').strip().upper()
    idade = int(input('Idade: '))
    print('-' * 20)

    somaIdade += idade

    if sexo == 'M' and (idadeMaisVelho == 0 or idade > idadeMaisVelho):
        idadeMaisVelho = idade
        nomeMaisVelho = nome

    if idade < 21 and sexo == 'F':
        mulheresMenores += 1

print('A média de idade do grupo é {:.2f}'.format(somaIdade / 4))

if nomeMaisVelho != '':
    print('O homem mais velho é o {}'.format(nomeMaisVelho))
else:
    print('Não há nenhum homem na lista')

if mulheresMenores > 0:
    print('{} mulher(es) tem menos de 21 anos'.format(mulheresMenores))
else:
    print('Não há nenhuma mulher na lista com menos de 21 anos')

print('-' * 20)