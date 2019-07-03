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
