from blackjack.modulos.Card import Card
from random import shuffle


class Deck:
    deck = []
    garbage = []

    def __init__(self):
        # Montando Deck
        for symbol in Card.symbols:
            for number in Card.numbers:
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
        if self.qt() == 0:
            return False

        card = self.deck[0]
        self.garbage.append(card)
        self.deck.pop(0)
        return card

    def qt(self):
        """
        Quantidade de cartas ainda no Deck

        :rtype: int
        """
        return len(self.deck)

    def qt_garbage(self):
        """
        Quantidade de cartas na lixeira

        :rtype: int
        """
        return len(self.garbage)

    def __len__(self):
        return self.qt()
