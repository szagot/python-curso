exp = input('Digite uma expressão matemática: ').strip()

# Versão com menos laços: método de pilha
pilha = []
for char in exp:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

print('Expressão Inválida!' if len(pilha) > 0 else 'Expressão Válida!')

"""
# Versão com mais laços 
fechamentos = []
expError = False
for i, char in enumerate(exp):
    # Se encontrou um fechamento sem abertura, fecha
    if char == ')' and i not in fechamentos:
        expError = True
        break

    # Se encontrou uma abertura, localiza seu fechamento
    if char == '(':
        encontrou = False
        for c, fec in enumerate(exp):
            # Achou um fechamento e ele ainda não foi contabilizado
            if fec == ')' and c not in fechamentos:
                fechamentos.append(c)
                encontrou = True
                break
        # Se apos procurar, não encontrou
        if not encontrou:
            expError = True

print('Expressão Inválida!' if expError else 'Expressão Válida!')
"""
