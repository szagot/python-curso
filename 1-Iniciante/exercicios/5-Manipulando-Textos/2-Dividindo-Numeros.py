num = int(input('Digite um número de 0 a 9999: '))

# Fórmula: divisão inteira do numero por 1, 10, 100 ou 1000, pegando o módulo do resultado

# Pegando a unidade
unidade = num // 1 % 10
# Pegando a dezena
dezena = num // 10 % 10
# Pegando a centena
centena = num // 100 % 10
# Pegando o milhar
milhar = num // 1000 % 10

print("""
unidade: {}
dezena:  {}
centena: {}
milhar:  {}
""".format(
    unidade,
    dezena,
    centena,
    milhar
))
