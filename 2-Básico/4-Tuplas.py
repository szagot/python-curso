"""
Tuplas são o primeiro tipo de variável composta

tupla = ('item 1', 2, True) # Os parênteses são opcionais para tuplas

Aceita as mesmas funções de string, já que uma string é por padrão uma lista (segundo tipo de variável composta)

E assim como as strings, os elementos das tuplas são IMUTÁVEIS: Você pode alterar A VARIÁVEL,
MAS NÃO PODE ALTERAR UM ITEM INDIVIDUAL DELA
"""

# Exemplo de for com tupla
familia = ('Alunos', 'Daniel', 'Alejandro', 'Alini')
for nome in familia:
    print(f'Muito prazer, {nome}!')

# Isso é o mesmo que
for i in range(0, len(familia)):
    print(f'{i} - {familia[i]}')

# Para usar a primeira forma com o índice, use a função enumerate()
for i, nome in enumerate(familia):
    print(f'{i} - {nome}')

# Para ordenar, use sorted()
print(
    sorted(familia)
)

# Para concatenar uma tupla com outra, use +
pais = ('Maria', 'Joalson')
print(
    familia + pais
)

# O método count() conta o número de ocorrências de um elemento dentro de uma tupla, e o index() mostra seu índice
qtAlini = familia.count('Alini')
inAlini = familia.index('Alini')
print(f'Alini aparece {qtAlini} vezes e sua primeira ocorrência é na posição {inAlini}')

# O comando del elimina completamente uma variável da memória
del pais



