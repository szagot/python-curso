# Variáveis criadas no corpos do programa são globais por padrão.
# As criadas dentro de uma função, são locais
# Se for criada em uma função uma variável já existente no escopo global,
# ela não irá afetar a variável global, a menos que antes se use, dentro da função, o comando:
# ->  global variavel
#
# Os tipos de possíveis de escopo são
#   Local               - variáveis/funções criadas localmente (dentro de funções, por exemplo)
#                         e que só funcionam naquele escopo
#   Enclosing Functions - funções criadas dentro de funções encapsuladas
#   Global              - variáveis/funções atribuídas no inicio do arquivo,
#                         ou que são declaradas como global dentro de uma função
#   Bult-in             - variáveis/funções do Python
#
# A ordem que o Python irá usar para verificar uma variável ou função é o LEGB (ordem acima)
# Exemplo:
x = 0
def exemplo():
    # Essa tem prioridade, e não afeta o "x" de fora, a menos que se use antes "global x"
    x = 50
    # Esse gunção nunca seria chamada, pois a variável local "x" tem prioridade na chamada
    def x():
        return 30
    x += 10
    return x

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
