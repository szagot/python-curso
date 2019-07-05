# Variáveis criadas no corpos do programa são globais por padrão.
# As criadas dentro de uma função, são locais
# Se for criada em uma função uma variável já existente no escopo global,
# ela não irá afetar a variável global, a menos que antes se use, dentro da função, o comando:
# ->  global variavel

# -> Interactive help
# No prompt use help(). Ele irá acessar o help do python,
# digite o comando para o qual precisa de ajuda. Para sair, quit.
# Outro modo é help(comando)
help(print)

# Você pode imprimir o documento de uma função com o parametro __doc__
print(print.__doc__)


# -> Criando uma docstring
def exemplo(param1, param2):
    """
    Exemplo de DOC String. Para chamar essa documentação use:
        help(exemplo)
    ou:
        print(exemplo.__doc__)

    :param int param1: Valor 1
    :param int param2: Valor 2
    :return int: Retorna a multiplicação dos valores
    """
    return param1 * param2


help(exemplo)
