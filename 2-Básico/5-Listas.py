"""
As regras para as listas são as mesmas de tuplas, mas tuplas são imutáveis, já as listas são mutáveis

lista = ['Item 1', 2, True]
lista[2] = False # Com listas isso é possível

Outro jeito de iniciar uma lista é
    lista = list()
ou
    lista = []

Ao fazer lista1 = lista2 será criada uma ligação (cópia vinculada) e não um clone da lista
Ao fazer lista1 = lista2[:] será criado um clone: a lista1 irá receber os itens da lista2
"""

nomes = ['Alejandro', 'Alunos', 'Alini', 'Daniel', 'Daniel']

# Método insert(posicao, valor): Adiciona um item na posição escolhida, "empurrando" os demais itens para a frente
nomes.insert(0, 'Maria')  # Isso adiciona um item na posição 0, de modo que os índices de todos os outros mudam

# Método append(): Adiciona um item ao final da lista
nomes.append('Joalson')

# Método pop(posicao): Apaga um item da lista
nomes.pop(2)  # Apaga o nome que esta na posição 2
del nomes[2]  # Mesmo que nomes.pop(2)
nomes.pop()  # Isso elimina o último elemento

# Método remove(valor): Apaga a primeira ocorrência do valor
if 'Daniel' in nomes:
    nomes.remove('Daniel')

# Criando uma lista ordenada usando range
valores = list(range(4, 10))  # Uma lista contendo os valores de 4 a 10

# Método sort(): ordena uma lista, alterando o seus indices de acordo com os seus valores ordenados
nomes.sort()
nomes.sort(reverse=True)  # Ordena de trás pra frente

lista1 = [1, 3, 5]
lista2 = lista1
# Isso irá mudar o item da posição 1 em ambas as listas, pois elas estão vinculadas!
lista2[1] = 2

# Para clonar, sem ter vinculos, faça
lista2 = lista1[:]  # Dessa forma, a lista2 vai receber os itens da lista1, e não uma cópia vinculada da mesma
