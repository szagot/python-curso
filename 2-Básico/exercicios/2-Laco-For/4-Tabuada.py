# Tabuada
num = int(input('Digite um número: '))
for i in range(1, 11):
    print('{:0>2} x {:0>2} = {:0>2}'.format(num, i, num * i))
