# Calcula se um número é primo

num = abs(int(input('Digite um número maior que 0: ')))
ePrimo = True

if num > 2:
    for i in range(2, num):
        if num % i == 0:
            ePrimo = False

print('É primo' if ePrimo else 'NÃO é Primo')
