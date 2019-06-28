"""
Estrutura:

    while {condição}:
        comandos
        # opcional para interrupção
        if condicao
            break

"""

# Exemplo equivalente a 'for c in range(1,10:'
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

# Exemplo com limite desconhecido
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Deseja continuar (S/N)? ').strip().upper()
print('Fim')
