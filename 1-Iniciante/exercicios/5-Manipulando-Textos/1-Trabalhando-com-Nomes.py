nome = input('Digite um nome: ')

print("""
Nome em maiúsculas:                 {}
Nome em minúsculas:                 {}
Total de letras (sem espaços):      {}
Total de letras (primeiro nome):    {}
""".format(
    nome.upper(),
    nome.lower(),
    len(nome.replace(' ', '')),
    nome.find(' ')
))
