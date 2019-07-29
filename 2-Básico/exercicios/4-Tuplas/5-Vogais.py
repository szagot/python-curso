palavras = ('Alunos', 'Alejandro', 'Daniel', 'Alini')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais', end=' ')
    for i in range(0, len(palavra)):
        if palavra[i].lower() in 'aeiou':
            print(palavra[i].upper(), end=' ')
    print('')

