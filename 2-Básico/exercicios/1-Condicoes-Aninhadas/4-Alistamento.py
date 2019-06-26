# Verifica se está na hora de se alistar

from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento
diff = abs(idade - 18)

if (idade - 18) < 0:
    print('Faltam {} ano(s) para você se alistar'.format(diff))
elif (idade - 18) > 0:
    print('Já passou(ram) {} ano(s) da data do seu alistamento'.format(diff))
else:
    print('Você deve se alistar esse ano!')
