from modulos.Card import Card


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

    def free(self):
        """
        Zera a mão
        """
        self.cards = []
        return self

    def count(self, second_card_is_hidden=False):
        """
        Conta os valores das cartas na mão

        :param second_card_is_hidden: Indica se a secunda carta do Dealer ainda está oculta
        :type second_card_is_hidden: bool

        :rtype: int
        """
        if len(self.cards) == 0:
            return 0

        # Verifica se tem uma carta de valor 10 na mão, caso o a segunda carta não estava oculta
        ace = False
        if not second_card_is_hidden:
            for card in self.cards:
                try:
                    if card.get_value() == 10:
                        ace = True
                        break
                except:
                    continue

        # Soma os valores
        val = 0
        for i, card in enumerate(self.cards):
            # Se a segunda carta ainda estiver oculta, não soma o valor
            if len(self.cards) == 2 and i == 1 and second_card_is_hidden:
                continue
            val += card.get_value(ace)

        return val

    def get(self):
        """
        Devolve as cartas da mão

        :rtype: list
        """
        return self.cards
