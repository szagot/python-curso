# Contagem
from time import sleep


def contagem(start, end, step=1):
    """
    Imprime uma contagem
    :param int start:
    :param int end:
    :param int step:
    """
    step = abs(step)
    # Verifica se o step não é 0
    if step == 0:
        step = 1

    # final para o range deve ser 1 a mais do que o informado (ou 1 a menos, em caso regressivo)
    end_range = end
    if start > end:
        # Step em caso regressivo deve ser negativo
        step *= -1
        end_range -= 1
    else:
        end_range += 1

    print(f'Contagem de {start} até {end} de {step} em {step}')
    for i in range(start, end_range, step):
        # O flush indica se deve descarregar a impressão direto em tela, sem armazenar buffer.
        # True: Não armazena buffer e imprime direto. False: Armazena o buffer, imprimindo apenas no final
        print(i, end=' ', flush=True)
        sleep(.4)

    print('Fim!')


print('-' * 50)
contagem(1, 10)
print('-' * 50)
contagem(10, 1, 2)
print('-' * 50)
print('Personalize sua contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passos = int(input('Passos: '))
print('-' * 50)
contagem(ini, fim, passos)
