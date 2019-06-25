# Tentar acertar  número que o PC "Pensou"
from random import randint

pc = randint(0, 5)
user = int(input('De 0 a 5, tente adivinhar que número estou pensando: '))
print('Acertou, Mizerávi!' if pc == user else 'Tente novamente, porque o número que eu pensei foi {}'.format(pc))
