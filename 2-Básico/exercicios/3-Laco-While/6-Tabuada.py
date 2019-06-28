# Tabuada - repete até que se digite um número negativo
while True:
    print('-' * 20)
    num = int(input('Digite um número (-1 para cancelar): '))
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num:0>2} x {i:0>2} = {(num * i):0>2}')
