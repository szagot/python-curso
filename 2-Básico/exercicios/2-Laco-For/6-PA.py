# Progressão aritmética

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for n in range(a1, a1 + (10 * r), r):
    print(n, end=', ')
print('...')
