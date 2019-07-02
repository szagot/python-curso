# Solicitando e já ordenando os valores

valores = []
for i in range(0, 5):
    valor = abs(int(input(f'Digite o {i + 1}º valor: ')))
    # O valor é o primeiro a ser digitado ou é maior que o último?
    if i == 0 or valor > valores[-1]:
        # Adiciona oa final da lista
        valores.append(valor)
        print('Adicionado ao final da lista')
    else:
        # Localiza o maior valor que ele
        for pos, val in enumerate(valores):
            if valor <= val:
                # Ao encontrar o valor que seja maior ou igual que o digitado, adiciona ele na posição
                valores.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista.')
                break

print('-=' * 30 + '-')
print(f'Você digitou os valores {valores}')
