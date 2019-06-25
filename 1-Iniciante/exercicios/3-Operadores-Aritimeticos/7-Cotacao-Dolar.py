# Mostra quantos dólares a pessoa pode comparar com o que tem na carteira em reais

cotacao = 3.27
reais = float(input('Digite quanto você tem em R$: '))

print('Com isso dá para você comprar U$ {:.2f}'.format(reais / cotacao))
