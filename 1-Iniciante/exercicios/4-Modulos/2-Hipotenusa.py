from math import hypot

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))

print('O valor da hipotenusa é {}'.format(hypot(oposto, adjacente)))
