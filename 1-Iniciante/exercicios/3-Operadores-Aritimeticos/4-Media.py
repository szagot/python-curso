# Mostra a média de duas notas (com 1 casa decimal)

n1 = int(input('Digite a nota 1: '))
n2 = int(input('Digite a nota 2: '))

print('A média das notas {} e {} é {:.1f}'.format(n1, n2, (n1+n2)/2))
