"""
São semelhantes ao formato JSON

Declaração:
    dados = dict()
ou
    dados = {}
ou
    dados = {
        'nome': 'Pedro,
        'idade': 25
    }

print(dados['nome]')
"""

dados = {
    'nome': 'Daniel Bispo',
    'idade': 37
}

# Removendo um item
del dados['idade']

# Adicionando um novo item
dados['sexo'] = 'M'

# Mostrando Chaves
for key in dados.keys():
    print(key)

# Mostrando apenas valores
for value in dados.values():
    print(value)

# Mostrando items
for key, value in dados.items():
    print(f'O {key} é {value}')

# Para ordenar um dicionário, é preciso importar o itemgetter de operator a fim de determinar a chave de indice
from operator import itemgetter

jogadores = {
    'jogador1': 10,
    'jogador2': 5,
    'jogador3': 8,
    'jogador4': 3
}
# Ordena em forma decrescente pelo valor. Se fosse pela chave, seria itemgetter(0)
ordenado = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))
print(ordenado)

# Para criar uma cópia sem vínculos, use o método copy()
brasil = list()
estado = dict()
for i in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ').strip().title()
    estado['sigla'] = input('Sigla do Estado: ').strip().upper()
    # Isso irá adicionar uma cópia à lista brasil, sem vínculos
    brasil.append(estado.copy())

# Mostrando formatado:
for estado in brasil:
    print('-' * 20)
    for key, value in estado.items():
        print(f'{key}: {value}')
print('-' * 20)
