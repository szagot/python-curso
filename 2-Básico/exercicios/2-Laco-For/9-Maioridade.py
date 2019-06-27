# De 7, Quantos atingiram a maioridade e quantos não

from datetime import date

anoAtual = date.today().year
maiores = 0
menores = 0

for i in range(0, 7):
    ano = int(input('Digite o ano de nasc. da {}ª pessoa: '.format(i + 1)))
    if (anoAtual - ano) >= 18:
        maiores += 1
    else:
        menores += 1

print('Dos 7, {} atingiram a idade adulta e {} são menores de idade'.format(maiores, menores))
