# Determina se um ano é bissexto
from datetime import date

ano = int(input('Digite um ano para saber se ele é bissexto ou não (digite 0 para pegar o ano atual): '))
if ano == 0:
    ano = date.today().year

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} NÃO é um ano bissexto.'.format(ano))
