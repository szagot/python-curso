from blackjack.modulos.Deck import Deck

deck = Deck()
cont = 0
while True:
    carta = deck.get_card()
    cont += 1
    if not carta:
        break

    print(cont)
    print(f'Carta: {carta.get()} | Valor: {deck.get_card_value(carta)}')



