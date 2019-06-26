# Definindo qual número é maior

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

if num1 > num2:
    print('O primeiro número é maior')
elif num2 > num1:
    print('O segundo número é maior')
else:
    print('Não existe número maior, ambos são iguais')
