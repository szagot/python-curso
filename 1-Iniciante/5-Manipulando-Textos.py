"""
Cadeia de caracteres

Exemplo:
    frase = C  u  r  s  o     d  e     P  y  t  h  o  n
            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
"""

frase = 'Curso de Python'

# Pega o caractere 6
frase[6]
# 'd'

# Vai do caractere 0 até 4 caracteres, contando do 0
frase[0:4]
# 'Curs'

# Vai do caractere da posição 9 até 15 caracteres a partir do 0
frase[9:15]
# 'Python'

# Vai do caractere da posição 9 até 15 caracteres a partir do 0, pulando de 2 em 2
frase[9:15:2]
# 'Pto'

# Vai do inicio até 5 caracteres
frase[:5]
# 'Curso'

# Vai do caractere 9 até o final
frase[9:]
# 'Python'

# Vai do 6º caractere a contar da direita (do final) até o fim da string
frase[-6:]
# 'Python'

# Vai do 6 ao final, pulando de 3 em 3
frase[6::3]
# 'dPh'


# -> Análise:

# Mostra o tamanho da string
len(frase)
# 15

# Conta quantos caracteres 'o' tem na variavel
frase.count('o')
# 2

# Conta quantos caracteres 'o' tem, começando do  9 até o final
frase.count('o', 9, len(frase))
# 1

# Localiza o primeiro range de caracteres 'rso' dentro da string, retornando o inicio
frase.find('rso')
# 2

# Se a string procurada não existir, o retorno será -1
frase.find('Android')
# -1

# Verificador booleano
teste = 'Curso' in frase
# True


# -> Transformação

# Substituir 'Python' por 'Android'
frase = frase.replace('Python', 'Android')
# 'Curso de Android'

# Maiúscula
frase.upper()
# 'CURSO DE ANDROID'

# Minúscula
frase.lower()
# 'curso de android'

# Irá jogar todos para minúsculos, e só o primeiro caractere será maiuscula
frase.captalize()
# 'Curso de android'

# Deixa o primeiro caractere de cada palavra em maiúscula
frase.title()
# 'Curso De Android'

# Elimina espaços em branco do início e do final, se houverem
frase.strip()

# Elimina espaços em brancos do final da string
frase.rstrip()

# Elimina espaços em brancos do início da string
frase.lstrip()

# -> Divisão

# Transforma uma string em uma lista. Se nenhum parâmetro for informado, a quebra será feita nos espaços
lista = frase.split()
# ['Curso', 'de', 'Android']

# Transforma uma lista em uma string, usando o caractere de separação informado
novaFrase = '-'.join(lista)
# 'Curso-de-Android'

# Imprimindo um texto grande usando apenas um print (semelhante ao <pre>)
print("""
    Isso é um exemplo de texto grande.
    Note que ele respeita as tabulações e espaços, bem como
as quebras de linha.  
""")
