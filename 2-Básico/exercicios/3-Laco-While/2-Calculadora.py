# Calcule dois números

opcao = 4
while opcao != 5:
    if opcao == 4:
        print('-' * 20)
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))

    print('-' * 20)
    opcao = int(input("""O que você deseja fazer com ós números {} e {}?
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair
    : """.format(num1, num2)))

    if opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    if opcao == 2:
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
    if opcao == 3:
        print(
            'Entre {} e {}, o maior é {}'.format(num1, num2, num1 if num1 > num2 else num2 if num2 > num1 else 'Ambos'))
    if opcao > 5 or opcao < 1:
        print('Opção inválida!')

print('-' * 20)
