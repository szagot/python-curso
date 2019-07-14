from blackjack.modulos.Card import Card


class Hand:
    cards = []

    def add(self, card: Card):
        """
        Adiciona uma carta na mão do jogador ou do dealer

        :type card: Card
        :rtype: self
        """
        self.cards.append(card)

        return self

    def count(self):
        """
        Conta os valores das cartas na mão

        :rtype: int
        """
        if len(self.cards) == 0:
            return 0

        # Verifica se tem uma carta de valor 10 na mão
        ace = False
        for card in self.cards:
            if card.get_value() == 10:
                ace = True
                break

        # Soma os valores
        val = 0
        for card in self.cards:
            val += card.get_value(ace)

        return val

    def get(self):
        """
        Devolve as cartas da mão

        :rtype: list
        """
        return self.cards
