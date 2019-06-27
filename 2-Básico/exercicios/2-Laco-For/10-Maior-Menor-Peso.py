# Verifica quem tem o menor peso e quem tem o maior peso

menor = 0
maior = 0

for i in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i + 1)))
    if menor == 0 or peso < menor:
        menor = peso
    if maior == 0 or peso > maior:
        maior = peso

print('O menor peso digitado foi: {:.2f}'.format(menor))
print('O maior peso digitado foi: {:.2f}'.format(maior))
