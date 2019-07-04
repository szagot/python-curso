# Área do terreno


def area(l, c):
    """
    Calcula a área do terreno
    :param float l: Largura do terreno
    :param float c: Altura do terreno
    :return float: área do terreno
    """

    return c * l


print('Controle de Terreno')
print('-' * 20)

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

print(f'A área de um terreno de {largura:.1f}x{comprimento:.1f} é de {area(largura, comprimento):.1f}m²')
