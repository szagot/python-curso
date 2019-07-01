# Listagem do CBF 2019

times = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético', 'Goiás', 'Botafogo', 'Bahia', 'São Paulo',
         'Corinthians', 'Grêmio', 'Atlético', 'Ceará', 'Fortaleza', 'Vasco', 'Fluminense', 'Chapecoense', 'Cruzeiro')

print('Os 5 primeiros colocados na CBR são:')
for i, time in enumerate(times[:5]):
    print(f'{i + 1} - {time}')

print('-' * 20)
print('Os últimos 4 colocados na CBR são:')
for i, time in enumerate(times[:-5:-1]):
    print(f'{len(times)-i} - {time}')

print('-' * 20)
print(f'Lista com os times em ordem alfabética: {sorted(times)}')

print('-' * 20)
print(f'O time Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
