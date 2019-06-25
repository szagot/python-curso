# Valor com 5% de desconto

desconto = 5
valor = float(input('Digite o valor do produto: '))

print('Esse produto com desconto de {}% custará R$ {:.2f}'.format(desconto, valor - (valor * desconto / 100)))
