# Aumento de salário conforme taxa

limite = 1250
taxMin = 15
taxMax = 10

salario = float(input('Digite o salário do funcionário: '))

if salario > limite:
    novoSalario = salario + (salario * taxMax / 100)
else:
    novoSalario = salario + (salario * taxMin / 100)

print('Seu novo salário é R$ {:.2f}'.format(novoSalario))
