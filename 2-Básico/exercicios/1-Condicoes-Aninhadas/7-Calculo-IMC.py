# Calcula o IMC da pessoa

altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso (kg): '))
imc = peso / (altura ** 2)

print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc < 25:
    print('Seu peso é o ideal.')
elif imc < 30:
    print('Você está um pouco acima do peso ideal.')
elif imc < 40:
    print('Você desenvolveu obesidade. Procure se cuidar!!!')
else:
    print('Sua obesidade é do tipo mórbida. Alto risco de morte!!!')
