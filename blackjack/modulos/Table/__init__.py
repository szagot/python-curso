from modulos.Hand import Hand
from modulos.Gamer import Gamer
from modulos.Deck import Deck
from modulos import Helpers
import os


class Table:
    dealer: Hand
    gamer: Gamer
    deck: Deck
    screen = 50
    second_card_is_hidden = True

    def __init__(self):
        self.dealer = Hand()
        self.gamer = Gamer()
        self.deck = Deck()
        self.start()

    def start(self):
        """
        Inicia o Jogo
        """
        # Libera a mão
        self.dealer.free()
        self.gamer.hand.free()

        # Dá as cartas do Dealer
        self.dealer.add(self.deck.get_card())
        self.dealer.add(self.deck.get_card())

        # Dá as cartas do Jogador
        self.gamer.hand.add(self.deck.get_card())
        self.gamer.hand.add(self.deck.get_card())

        # Imprime a tela
        self.print_table()

    def verify_deck(self):
        """
        Retorna se o deck ainda tem cartas
        :rtype: bool
        """
        return self.deck.qt() > 0

    def print_table(self):
        """
        Impressão de tela
        """
        os.system('cls' if os.name == 'nt' else 'clear') or None
        tela = self.screen
        Helpers.title('BlackJack', tam=tela, espaco=0)

        # Lixo e Deck
        print(f'{"┌────┐":<{int(tela / 2)}}{"┌────┐":>{int(tela / 2)}}')
        print(f'{f"│ {self.deck.qt_garbage():0>2} │ Lixo":<{int(tela / 2)}}', end='')
        print(f'{f"Deck │ {self.deck.qt():0>2} │":>{int(tela / 2)}}')
        print(f'{"└────┘":<{int(tela / 2)}}{"└────┘":>{int(tela / 2)}}')

        # Dealer
        Helpers.print_color(
            f'Dealer: {self.dealer.count(self.second_card_is_hidden)}',
            color='cyan',
            align='center',
            style='bold',
            length=tela
        )
        cards_dealer = ''
        cards_dealer_before = ''
        cards_dealer_after = ''
        for i, card in enumerate(self.dealer.get()):
            cards_dealer_before += ' ┌─────┐ '
            cards_dealer_after += ' └─────┘ '
            cards_dealer += f' │ {card if i != 1 or not self.second_card_is_hidden else " ? "} │ '
        Helpers.print_color(cards_dealer_before, color='blue', style='bold', align='center', length=tela)
        Helpers.print_color(cards_dealer, color='blue', style='bold', align='center', length=tela)
        Helpers.print_color(cards_dealer_after, color='blue', style='bold', align='center', length=tela)
