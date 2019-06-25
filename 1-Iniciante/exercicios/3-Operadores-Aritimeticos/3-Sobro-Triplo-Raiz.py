# Mostra o dobro, o triplo e a raiz quadrada (com 2 pontos flutuantes) de um número

n = int(input('Digite um número inteiro: '))

print('O dobro do número {} é {}, o triplo é {} e sua raiz quadrada é {:.2f}'.format(n, n * 2, n * 3, n ** (1 / 2)))
