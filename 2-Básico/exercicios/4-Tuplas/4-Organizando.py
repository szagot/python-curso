produtos = ('Caderno', 11.5, 'Borracha', 0.56, 'Régua', 5.99, 'Lápis', 1.5, 'Adesivo', 99.5)

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for i, produto in enumerate(produtos):
    if i % 2 == 0:
        print(f'{produto:.<20}:', end=' ')
    else:
        print(f'R$ {produto:>5.2f}')

print('-' * 30)