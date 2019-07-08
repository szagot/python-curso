def leia_dinheiro(pergunta):
    from modulos import texto
    while True:
        valor = str(input(pergunta)).strip().replace(',', '.')
        if not valor or valor.isalpha():
            print(texto.amend_color(f'Valor "{valor}" é inválido! Tente novamente!', color='red', style='bold'))
        else:
            break

    return float(valor)
