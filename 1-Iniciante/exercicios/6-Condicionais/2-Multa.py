# Determine a multa a ser paga se houver excesso de velocidade

reaisPorKm = 7
radar = int(input('Qual a velocidade registrada? '))
if radar > 80:
    multa = reaisPorKm * (radar - 80)
    print('Emitir multa no valor de R$ {:.2f}'.format(multa))
