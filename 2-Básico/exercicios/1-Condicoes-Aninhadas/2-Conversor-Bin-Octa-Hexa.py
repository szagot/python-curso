# Converte um decimal para Binario, Octadecimal ou Hexadecimal

base = int(input('Digite a base de conversão - (1) Binário | (2) Octal | (3) Hexadecimal: '))
num = int(input('Digite o número a ser convertido: '))

if base == 1:
    print('Binário: {}'.format(bin(num)[2:]))
elif base == 2:
    print('Octal: {}'.format(oct(num)[2:]))
elif base == 3:
    print('Hexadecimal: {}'.format(hex(num)[2:]))
else:
    print('Opção inválida')
