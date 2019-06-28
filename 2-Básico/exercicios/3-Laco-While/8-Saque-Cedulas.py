# Informe quantas cédulas serão entregues

print('=' * 50)
print(f'{"BANCO FILIPES":^50}')
print('=' * 50)

valor = int(input('Digite o valor a ser sacado: R$ '))
saque = 0
c50 = c20 = c10 = c1 = 0

print('=' * 50)
while saque < valor:
    faltando = valor - saque
    if faltando >= 50:
        c50 += 1
        saque += 50
    elif faltando >= 20:
        c20 += 1
        saque += 20
    elif faltando >= 10:
        c10 += 1
        saque += 10
    else:
        c1 += 1
        saque += 1

if c50 > 0:
    print(f'- {c50:>5} notas de R$ 50,00')
if c20 > 0:
    print(f'- {c20:>5} notas de R$ 20,00')
if c10 > 0:
    print(f'- {c10:>5} notas de R$ 10,00')
if c1 > 0:
    print(f'- {c1:>5} notas de R$ 1,00')

print('=' * 50)
