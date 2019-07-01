numeros = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais número: ')),
    int(input('Digite só mais um número: '))
)

print(f'Você digitou os valores {numeros}')

# 9 apareceu?
print(f'O número 9 apareceu {numeros.count(9)} vezes')

# Posição do 3
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado nenhuma vez')

# Pares
pares = ''
for i, numero in enumerate(numeros):
    if numero % 2 == 0:
        pares += str(numero) + ' '
print(f'Os valores pares digitados foram {pares}')
