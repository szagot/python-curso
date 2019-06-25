# Calcula quanta tinta é necessária para pintar uma parede, sabendo que 1l de tinta pinta 2m²

litrosPorMetroQuadrado = 0.5
altura = float(input('Digite a altura da sua parede: '))
comprimento = float(input('Digite o comprimento da sua parede: '))
area = altura * comprimento

print('Você vai precisar de {} litros de tinta para pintar essa parede'.format(area * litrosPorMetroQuadrado))
