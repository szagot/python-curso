# Boletim

tela = 40
print('#' * tela)
print(f'#{"Boletim - Entrada de dados":^{tela - 2}}#')
print('#' * tela, end='\n\n')

alunos = []
aluno = {}
opcao = 's'
while opcao not in 'Nn':
    aluno['nome'] = input('Nome: ').strip().title()
    aluno['n1'] = float(input(f'Nota 1: ').strip())
    aluno['n2'] = float(input(f'Nota 2: ').strip())
    alunos.append(aluno.copy())
    opcao = input('Deseja continuar (S/N)? ').strip()[0]
    print('-' * tela)

# Imprimindo
print(f'{"Nº":<3}{"Nome":<{(tela - 10)}}{"Média":>7}')
print('-' * tela)
for n, aluno in enumerate(alunos):
    media = (aluno['n1'] + aluno['n2']) / 2
    print(f'{n:<3}{aluno["nome"]:<{(tela - 10)}}{media:>7.2f}')

# Mostrando notas
while True:
    print('-' * tela)
    qt = len(alunos) - 1
    opcao = input(f'Mostrar notas de qual aluno?\n(0 a {qt} | 999 para interromper) ')
    print('-' * tela)
    opcao = int(opcao) if opcao.isnumeric() else qt + 1
    if opcao == 999:
        break
    elif opcao > qt:
        print('Aluno inexistente! ')
    else:
        print(f'As notas de {alunos[opcao]["nome"]} são [{alunos[opcao]["n1"]}, {alunos[opcao]["n2"]}]')

print('#' * tela)
