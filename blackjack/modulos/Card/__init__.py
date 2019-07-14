class Card:
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number

    def get(self):
        return f'{self.symbol}{self.number:>2}'

    def get_symbol(self):
        return self.symbol

    def get_number(self):
        return self.number

    def __str__(self):
        return self.get()
