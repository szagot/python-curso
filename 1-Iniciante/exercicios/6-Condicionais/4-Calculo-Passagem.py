# Cálculo de passagem com valores diferenciados
limiteKm = 200
km = float(input('Digite q quilometragem de sua viagem: '))
# Taxa Viagens curtas
taxMin = .5 * km
# Taxa viagens longas
taxMax = .45 * km

print('O valor de sua passagem será R$ {:.2f}'.format(taxMin if km <= 200 else taxMax))
