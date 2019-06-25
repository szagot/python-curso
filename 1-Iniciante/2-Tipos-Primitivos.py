"""
Tipos Primitivos
================

int()
Tipos inteiros.
Exemplo: 1, 5, -10, 0

float()
Tipos de ponto flutuante.
Exemplo: 1.5, 0.5, -15.25

bool()
Booleano. Pode ser True ou False (em Camelcase)

str()
String. As aspas podem ser duplas ou simples, mas a comunidade prefere simples.
"""

# Exemplo para mostrar tipo da variável
s = 5
print('A variável "s" é do tipo', type(s))

# Exemplo de conversão entre string e inteiro
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma de {} e {} é {}'.format(n1, n2, soma))
