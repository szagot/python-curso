# Salário com 15% de aumento

aumento = 15
salario = float(input('Digite seu salário atual: '))

print('Seu salário, corrigido em {}%, será de R$ {:.2f}'.format(aumento, salario + (salario * aumento / 100)))
