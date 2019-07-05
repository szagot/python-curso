def voto(ano):
    """
    Indica se a pessoa tem voto obrigatório ou não de acordo com a idade
    :param int ano: ano de nascimento da pessoa
    :return str:
    """
    from datetime import date

    idade = date.today().year - ano
    if idade <= 0:
        return 'Essa pessoa nem nasceu!'
    elif idade < 16:
        return f'Com {idade} ano(s): Não Vota.'
    elif 18 > idade > 65:
        return f'Com {idade} ano(s): Voto Opcional'
    return f'Com {idade} ano(s): Voto Obrigatório'


ano = int(input('Em que ano você nasceu? '))
print(f'{voto(ano)}')
