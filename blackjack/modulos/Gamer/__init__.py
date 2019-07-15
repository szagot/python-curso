from modulos.Hand import Hand


class Gamer:
    amount: float = 100
    bet: float = 0
    insurance: float = 0
    hand: Hand

    def __init__(self):
        self.hand = Hand()

    def betting(self, value):
        """
        Adiciona uma aposta

        :type value: float
        :rtype: bool
        """
        if value > self.amount:
            return False

        self.bet += value
        self.amount -= value

        return True

    def double(self):
        """
        Dobra a aposta
        """
        if 0 < self.bet <= self.amount:
            self.bet *= 2

    def bet_wins(self):
        """
        Aposta ganha!
        """
        self.amount = self.bet * 2
        self.bet = 0
        self.insurance = 0

    def bet_lost(self):
        """
        Aposta Perdida!
        """
        if self.insurance > 0:
            self.amount += self.bet

        self.bet = 0
        self.insurance = 0

    def game_tie(self):
        """
        Empate
        """
        self.amount += self.bet
        self.bet = 0
        self.insurance = 0

    def add_insurance(self):
        """
        Adiciona seguro
        """
        if self.bet > 0:
            self.insurance = self.bet / 2
            self.amount -= self.insurance

    def split_verify(self):
        """
        Verifica se é possível splitar
        :rtype: bool
        """
        return \
            len(self.hand.cards) == 2 and \
            self.hand.cards[0].get_number() == self.hand.cards[1].get_number() and \
            self.amount >= self.bet
