"""
Laço de repetição for com variavel de controle

# Repita o laço de 0 a 9. A cada repetição, variavel conterá o numero referente ao range em que o ponteiro estiver
for variavel in range(0,9):
    comandos
comandos_fora_do_laço

O último índice do range será o índice de quebra, e, portanto, será ignorado
"""

# Imprimindo OI 6 vezes
for i in range(0, 6):
    print('{} - Oi, mané'.format(i))
print('Fim!')

# Imprimindo Oi 6 vezes com indice de trás pra frente
for i in range(6, 0, -1):
    print('{} - Oi Mané'.format(i))
print('Fim de trás pra frente!')

# Imprimindo Oi 3 vezes com indice pulando de 2 em 2
for i in range(0, 6, 2):
    print('{} - Oi Mané'.format(i))
print('Fim com pulinhos!')

# Imprimindo o indice conforme interação de usuário
num = int(input('Digite um número: '))
for i in range(0, num + 1):
    print(i)
print('Fim com interação!')
