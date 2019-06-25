# Condicionais em Python
tempo = int(input('Quantos anos tem seu carro? '))

# Em python, a indentação é que define o bloco do if/else
if tempo > 4:
    print('Tá velhinho, hein?')
else:
    print('Carro com cheirinho de novo!')

print('FIM!!!')

# Mesmo exemplo, de forma simplificada (o mais próximo possível de uma condição ternária):
tempo = int(input('Quantos anos tem seu carro? '))

# String se condição for verdadeira, condição, string se for falsa
print('Tá velhinho, hein?' if tempo > 4 else 'Carro com cheirinho de novo!')

print('FIM!!!')

