# Progressão aritmética
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termos = 10
qt = 0
while termos > 0:
    qt += termos
    for n in range(a1, a1 + (termos * r), r):
        print(n, end=', ')
    termos = int(input('... Quer ver mais quantos termos? '))
    a1 = n + r
print('Finalizado com {} termos mostrados'.format(qt))
