"""
Estrutura:

    while {condição}:
        comandos
        # opcional para interrupção
        if condicao
            break

É possível usar usar "else", que será executado uma vez

"""

# Exemplo equivalente a 'for c in range(1,10), porém irá printar tb o 10 por causa do "else":'
c = 1
while c < 10:
    print(c)
    c += 1
else:
    print(c)
print('Fim')

# Exemplo com limite desconhecido
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Deseja continuar (S/N)? ').strip().upper()
print('Fim')
