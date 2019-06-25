"""
Mudando as cores do terminal com o padrão ANSI

Código ANSI para cores que funciona melhor pro Python: 033

      Estilo ; Texto ; Background
\033[   0    ;  33   ;     44     m

Códigos para Estilo:
0: None     (Padrão se omitido)
1: Bold
4: Underline
7: Negative

Códigos para Texto:
3{cor}

Códigos para Fundo:
4{cor}

Códigos para cores:
0: Branco
1: Vermelho
2: Verde
3: Amarelo
4: Azul
5: Magenta
6: Ciano
7: Cinza    (Padrão se omitido para Texto. Para Fundo, o padrão é preto)

Exemplos:
\033[30;41m   - Texto branco, Fundo Vermelho
\033[4;33;46m - Sublinhado, Texto Amarelo, Fundo ciano
\033[1;35;43m - Negrito, Texto Magenta, Fundo Amarelo
\033[30;42m   - Texto Branco, Fundo Verde
\033[m        - Letra Branca, fundo Preto (Reseta o padrão do terminal)
\033[7;30m    - letra preta, Fundo branco

"""

# Olá mundo em texto azul negrito (O reset no final é para o fundo ficar apenas no texto)
print('\033[1;34mOlá Mundo!\033[m')

# Mostrando valores em cores
a = True
b = False
print('Use \033[1;32m{}\033[m para verdadeiro e \033[1;31m{}\033[m para falso'.format(a, b))

# Outra forma, usando o format
nome = 'Daniel Bispo'
print('Olá {}{}{}!!! Prazer em te conhecer!'.format(
    '\033[7;30m',
    nome,
    '\033[m'
))

# Mais uma forma usando dicionário
cores = {
    'reset': '\033[m',
    'blackWhite': '\033[7;30m',
    'red': '\033[31m',
    'green': '\032[31m'
}
print('Olá {}{}{}!!! Prazer em te conhecer!'.format(
    cores['blackWhite'],
    nome,
    cores['reset']
))
