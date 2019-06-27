# Sequencia de Fibonacci

n = int(input('Digite quantos termos da sequencia de Fibonacci vc quer ver (digite um número maior que 1): '))
cont = 2
t1 = 0
t2 = 1
print('0 → 1 → ', end='')
while cont < n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' → ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
