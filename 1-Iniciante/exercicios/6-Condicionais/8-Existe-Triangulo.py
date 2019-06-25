# Calcular se 3 medidas formam um triangulo

print('-=' * 20 + '-')
print('{:^41}'.format('Analisador de Triângulos'))
print('-=' * 20 + '-')

a = float(input('Digite a medida 1: '))
b = float(input('Digite a medida 2: '))
c = float(input('Digite a medida 3: '))

if a + b > c and a + c > b and b + c > a:
    print('O triangulo pode ser formado')
else:
    print('Não tem possibilidade de se formar um triangulo')
