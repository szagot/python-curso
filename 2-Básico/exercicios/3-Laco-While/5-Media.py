# Media entre números
opcao = 'S'
soma = 0
qtd = 0
maior = 0
menor = 0
while opcao == 'S':
    valor = int(input('Digite um valor: '))
    opcao = input('Deseja continuar (S/N)? ').strip().upper()
    qtd += 1
    soma += valor
    if maior == 0 or valor > maior:
        maior = valor
    if menor == 0 or valor < menor:
        menor = valor

print('A média dos valores digitados é {:.2f}'.format(soma / qtd))
print('O menor número digitado foi {} e o maior foi {}'.format(menor, maior))

