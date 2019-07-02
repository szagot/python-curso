# Evitando duplicidades
valores = []
opcao = 'S'
while opcao != 'N':
    valor = abs(int(input('Digite um valor a ser adicionado: ')))
    if valor in valores:
        print(f'O valor {valor} já foi adicionado anteriormente...')
    else:
        valores.append(valor)
        print(f'O valor {valor} foi adicionado com sucesso!')
    opcao = input('Deseja continuar (S/N)? ').strip()
    if len(opcao) > 0:
        opcao = opcao.upper()[0]

print('-=' * 30 + '-')
print(f'Você digitou os valores {valores}')
