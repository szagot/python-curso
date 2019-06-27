# Soma todos os números ímpares multiplos de 3 entre 1 e 500

soma = 0
for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        soma += i

print('O resultado da soma dos números ímpares multiplos de 3 entre 1 e 500 é {}'.format(soma))
