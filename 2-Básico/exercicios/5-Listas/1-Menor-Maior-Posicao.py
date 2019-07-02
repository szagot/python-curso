valores = []
maior = menor = 0
for i in range(0, 5):
    valores.append(abs(int(input(f'Digite o {i + 1}º valor: '))))
    if maior < valores[i] or maior == 0:
        maior = valores[i]
    if menor > valores[i] or menor == 0:
        menor = valores[i]

posMaior = posMenor = ''
for i, valor in enumerate(valores):
    if valor == menor:
        posMenor += f'{i}... '
    if valor == maior:
        posMaior += f'{i}... '

print(f'Você digitou os valores {valores}')
print(f'O menor valor digitado foi {menor} na(s) posição(ões) {posMenor}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) {posMaior}')
