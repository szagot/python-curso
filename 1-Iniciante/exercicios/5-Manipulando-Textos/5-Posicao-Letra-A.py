frase = input('Digite uma frase: ').strip().upper()

print("""
A letra A aparece {} vezes
A primeira vez na posição {}
A última vez na posição {}
""".format(
    frase.count('A'),
    frase.find('A') + 1,
    frase.rfind('A') + 1
))
