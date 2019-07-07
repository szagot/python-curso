from modulos import moeda

valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {valor:.2f} é R$ {moeda.metade(valor):.2f}')
print(f'O dobro de R$ {valor:.2f} é R$ {moeda.dobro(valor):.2f}')
print(f'10% de aumento sobre R$ {valor:.2f} é R$ {moeda.aumentar(valor, 10):.2f}')
print(f'15% de desconto sobre R$ {valor:.2f} é R$ {moeda.diminuir(valor, 15):.2f}')
