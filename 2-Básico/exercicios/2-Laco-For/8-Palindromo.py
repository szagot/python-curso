# É um palíndromo?
import re

# Usando REGEX
regex = re.compile('[^a-z]', re.IGNORECASE)
frase = regex.sub('', input('Digite uma frase: ').replace(' ', '').lower())

fraseInversa = ''
for i in range(len(frase) - 1, -1, -1):
    fraseInversa += frase[i]

print('Isso é um palíndromo' if frase == fraseInversa else 'Essa é uma frase normal')
