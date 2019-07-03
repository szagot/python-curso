# Montando uma Matriz 3x3,
#   somando os valores pares e os valores da 3ª coluna,
#   e verificando qual o maior valor da 2ª linha

space = 0
matriz = []
somaPares = somaCol = maiorLin = 0

for i in range(0, 3):
    line = []
    for c in range(0, 3):
        valor = input(f'Digite um valor para [{i},{c}]: ').strip()
        # Evita que um valor nulo seja digitado
        if not valor.isnumeric():
            valor = '0'
        # Verifica qual o número com a maior qtd de caracteres
        if space == 0 or len(valor) > space:
            space = len(valor)
        # Convertendo para inteiro
        valor = int(valor)
        # Adiciona o valor à linha
        line.append(valor)
        # Somando valores pares
        if valor % 2 == 0:
            somaPares += valor
        # Somando valores da terceira coluna
        if c == 2:
            somaCol += valor
        # Verificando maior da segunda linha
        if i == 1 and (maiorLin == 0 or valor > maiorLin):
            maiorLin = valor
    # Adiciona a linha a matriz
    matriz.append(line[:])
    line.clear()

space += 2

# Mostrando a matriz
maxCar = (space + 4) * 3
print('-' * maxCar)
for line in matriz:
    for val in line:
        print(f' [{val:^{space}}] ', end='')
    print()
print('-' * maxCar)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da 3ª colunas é {somaCol}')
print(f'O maior valor da segunda linha é {maiorLin}')
