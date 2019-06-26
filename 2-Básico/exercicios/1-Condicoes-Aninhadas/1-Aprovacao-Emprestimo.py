# Verifica se a pessoa tem condições de pagar

valorCasa = float(input('Digite o valor da casa a ser comprada: '))
salario = float(input('Digite o valor do seu salário: '))
qtAnos = int(input('Digite a quantidade de anos que você pretende pagar: '))
maxParcela = salario * 30 / 100
parcelas = qtAnos * 12
valorParcela = valorCasa / qtAnos

if valorParcela > maxParcela:
    print('Seu empréstimo foi negado. ')
else:
    print('Empréstimo aprovado!')

print('-' * 20)
print('Quantidade Parcela: {}'.format(parcelas))
print('Valor Parcela.....: {:.2f}'.format(valorParcela))
