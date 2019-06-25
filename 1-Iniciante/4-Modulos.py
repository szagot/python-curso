"""
Para adicionar módulos ao Python, é necessário importar suas bibliotecas

isso é feito com o comando import. Exemplos:
    import math                     # isso irá importar todas os módulos matematicos do Python
    from math import sqrt           # isso irá importar apenas o módulo sqrt da biblioteca math
    from math import ceil, floor    # isso irá importar os módulos ceil e floor da biblioteca math


Para verificar todas as bibliotecas, vá em https://docs.python.org/3/library/index.html

"""

# Exemplo 1
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é {}'.format(num, math.ceil(raiz)))

# Exemplo 2 (Procure usar as importações sempre no inicio do arquivo)
from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)  # Não precisa mais referenciar o módulo

print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))

# Exemplo 3: números randômicos
import random
print('Randômico entre 0 e 1: {}\nRandômico entre 1 e 10: {}'.format(random.random(), random.randint(1, 10)))

# Exemplo 4: Importando bibliotecas de 3ºs - https://pypi.org/
import emoji
print(emoji.emojize('Olá :earth_americas:!', use_aliases=True))
