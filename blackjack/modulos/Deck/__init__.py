from blackjack.modulos.Card import Card
from random import shuffle


class Deck:
    symbols = ('♥', '♦', '♣', '♠')
    numbers = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    deck = []
    garbage = []

    def __init__(self):
        # Montando Deck
        for symbol in self.symbols:
            for number in self.numbers:
                self.deck.append(Card(symbol, number))
        self.shuffle()

    def shuffle(self):
        """
        Embaralha o deck
        :rtype: self
        """
        shuffle(self.deck)
        return self

    def get_card(self):
        """
        Pega uma carta do deck, jogando para a lixeira

        :return: Próxima carta do deck
        :rtype: Card
        """
        if len(self.deck) == 0:
            return False

        card = self.deck[0]
        self.garbage.append(card)
        self.deck.pop(0)
        return card

    def get_card_value(self, card: Card, ace: bool = False):
        """
        Verifica o valor da carta

        :param card: Carta
        :type card: Card

        :param ace: Está em conjunto com um 10?
        :type ace: bool

        :return: Valor da Carta
        :rtype: int
        """
        number = card.get_number()

        # Card é válido?
        if card.get_symbol() not in self.symbols or number not in self.numbers:
            return 0
        # É um Ais?
        if number == 'A':
            return 11 if ace else 1
        # É uma carta especial?
        if number in 'JQK':
            return 10
        if number.isnumeric():
            return int(number)

        return 0
