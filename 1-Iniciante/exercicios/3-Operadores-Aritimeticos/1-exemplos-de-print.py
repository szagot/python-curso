n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))

som = n1 + n2
sub = n1 - n2
div = n1 / n2
mul = n1 * n2
exp = n1 ** n2
diI = n1 // n2
mod = n1 % n2

# Repete 30 vezes o caracter =
print('=' * 50)
# Centraliza o texto entre caracteres =
print('{:=^50}'.format(' Cálculos básicos '))
# Repete 30 vezes o caracter = e quebra a linha 2 vezes no final
print('=' * 50)

# Títulos com 20 caracteres alinhados à esquerda e
# Resultados com 30 caracteres alinhados à direita, com 2 pontos flutuantes
print(
    '{:<20}{:>30.2f}\n{:<20}{:>30.2f}\n{:<20}{:>30.2f}\n{:<20}{:>30.2f}\n{:<20}{:>30.2f}'.format(
        'Soma:', som,
        'Subtração:', sub,
        'Divisão:', div,
        'Multiplicação:', mul,
        'Exponenciação:', exp
    ), end='\n' + '=' * 50 + '\n'
)

# Títulos com 20 caracteres alinhados à esquerda e
# Resultados com 30 caracteres alinhados à direita, com nenhuma casa decimal
print(
    '{:<20}{:>30.0f}\n{:<20}{:>30.0f}'.format(
        'Divisão Inteira:', diI,
        'Sobra da Divisão:', mod
    )
)

# Fim
print('=' * 50)
