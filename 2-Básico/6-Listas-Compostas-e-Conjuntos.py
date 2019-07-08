"""
pessoa1 = ['Filipe', 8]
pessoa2 = ['Alejandro', 6]

dados = []
dados.append(pessoa1[:])
dados.append(pessoa2[:])

print(dados)
#-> Resultado: [ ['Filipe', 8], ['Alejandro', 6] ]

print(dados[0][0])
#-> Resultado: 'Filipe'


Outro tipo de dados são os conjuntos (set). São como as listas, porém só permitem valores únicos
exemplo = set()
exemplo2 = set(pessoa1)
"""

# Pegando os dados e salvando em uma lista composta
pessoas = []
dados = []
for i in range(0, 3):
    # Pede o nome e a idade
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    # Adiciona uma cópia dos dados em pessoas
    pessoas.append(dados[:])
    # Limpa os dados
    dados.clear()

# Mostrando os dados de uma lista composta
for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

# Criando um conjunto
conjunto = set()

# Adicionando dados. O exemplo abaixo retornará {1,2} por que ele não repete valores já adicionados
conjunto.add(1)
conjunto.add(2)
conjunto.add(1)

# Lendo conjunto
for item in conjunto:
    print(item)

# É possível criar um conjunto a partir de uma lista. O conjunto resultante ficará ordenado e sem as repetições
lista = [1,22,33,1,'Daniel',22]
conjunto = set(lista)
# -> Resultado {1, 22, 33, 'Daniel'}
