class Card:
    symbols = ('♥', '♦', '♣', '♠')
    numbers = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number

    def get(self):
        return f'{self.symbol}{self.number:>2}'

    def get_symbol(self):
        return self.symbol

    def get_number(self):
        return self.number

    def get_value(self, ace: bool = False):
        """
        Verifica o valor da carta

        :param ace: Está em conjunto com um 10?
        :type ace: bool

        :return: Valor da Carta
        :rtype: int
        """
        number = self.get_number()

        # Card é válido?
        if self.get_symbol() not in self.symbols or number not in self.numbers:
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

    def __str__(self):
        return self.get()
