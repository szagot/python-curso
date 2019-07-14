from blackjack.modulos.Deck import Deck
from blackjack.modulos.Hand import Hand

deck = Deck()
gamer = Hand()
dealer = Hand()

valor = 0
while valor < 17:
    gamer.add(deck.get_card())
    valor = gamer.count()

for card in gamer.get():
    print(card, end=' | ')
print(valor)

exit()
cont = 0
print(f'Cartas no Deck: {deck.qt()}')
print(f'Cartas na Lixeira: {deck.qt_garbage()}')
print('-' * 20)
while True:
    carta = deck.get_card()
    cont += 1
    if not carta:
        break

    print(cont)
    print(f'Carta: {carta.get()} | Valor: {carta.get_value()}')

print('-' * 20)
print(f'Cartas no Deck: {deck.qt()}')
print(f'Cartas na Lixeira: {deck.qt_garbage()}')
