# Testando os tipos de conversão

texto = input('Digite algo: ')

input('Você digitou "{}"'.format(texto))
input('É alfabético? {}'.format(texto.isalpha()))
input('É alfanumerico? {}'.format(texto.isalnum()))
input('É decimal? {}'.format(texto.isdecimal()))
input('É numérico? {}'.format(texto.isnumeric()))
input('É dígito? {}'.format(texto.isdigit()))
input('É identificador? {}'.format(texto.isidentifier()))
input('É apenas minúsculo? {}'.format(texto.islower()))
input('É apenas maiúsculo? {}'.format(texto.isupper()))
input('É imprimível? {}'.format(texto.isprintable()))
input('É somente de espaços? {}'.format(texto.isspace()))
input('É um título? {}'.format(texto.istitle()))
