nome = input('Digite seu nome completo: ').strip()
lista = nome.split()

print("""
Primeiro Nome: {}
Último Nome..: {}
""".format(
    lista[0],
    lista[-1]
))
