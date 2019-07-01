from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Lista gerada: {numeros}')

maior = 0
menor = 0
for numero in numeros:
    if maior == 0 or numero > maior:
        maior = numero
    if menor == 0 or numero < menor:
        menor = numero

print(f'O menor número foi o {menor} e o maior foi o {maior}')
