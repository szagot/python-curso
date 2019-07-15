from modulos.Hand import Hand
from modulos.Gamer import Gamer
from modulos.Deck import Deck
from modulos import Helpers
import os


class Table:
    dealer: Hand
    gamer: Gamer
    split: Gamer
    deck: Deck
    screen = 60
    second_card_is_hidden = True
    split_active = False
    dealer_active = False
    plays = {'h': '[H]it', 's': '[S]tand', 'u': 'S[u]rrender', 'e': '[E]xit'}

    def __init__(self):
        self.dealer = Hand()
        self.gamer = Gamer()
        self.split = Gamer()
        self.deck = Deck()
        self.start()

    def start(self):
        """
        Inicia o Jogo
        """
        # Libera a mão
        self.dealer.free()
        self.gamer.hand.free()
        self.split.hand.free()

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

    def hit(self, is_double=False):
        """
        Dá um hit para a mão da vez
        :param is_double: É pra dobrar?
        :rtype: bool
        """
        if not self.verify_deck():
            self.end_game()
            return False

        # Gamer 2 ativo?
        if self.split_active:
            self.split.hand.add(self.deck.get_card())
            if is_double:
                self.split.double()
                self.stand()
        # Dealer ativo?
        elif self.dealer_active:
            self.second_card_is_hidden = False
            while self.dealer.count() < 17:
                self.dealer.add(self.deck.get_card())
            self.dealer_active = False
        # Gamer 1 Ativo?
        else:
            self.gamer.hand.add(self.deck.get_card())
            if is_double:
                self.gamer.double()
                self.stand()

        self.print_table()

        return True

    def stand(self):
        # Split ativo? Passa a vez pro dealer e dá o Hit dele
        if self.split_active:
            self.split_active = False
            self.dealer_active = True
            self.hit()
        # Tem split? Passa a vez pro Gamer 2
        elif self.split.hand.count() > 0:
            self.split_active = True
            self.print_table()
        # Passa a vez pro Dealer e já executa o hit dele
        else:
            self.dealer_active = True
            self.hit()

    def surrender(self):
        pass

    def end_hound(self):
        """
        Faz a contagem e paga ou recolhe as apostas
        """

        split = self.split.hand.count()
        gamer = self.gamer.hand.count()
        dealer = self.dealer.count()

    def end_game(self):
        pass

    def print_table(self, status=''):
        """
        Impressão de tela
        :param status: Situação atual do jogo.
                        '' - Aguardando jogada
                        Outros exemplos:
                            'Dealer Ganha!'
                            'Gamer 1 Ganha, Gamer 2 Perde!'
                            'Gamer 2 Ganha, Gamer 1 Perde!'
                            'Gamer 1 e Gamer 2 Ganham, Dealer Perde!'
                            'Empate!'
        """
        os.system('cls' if os.name == 'nt' else 'clear') or None
        tela = self.screen
        Helpers.title('BlackJack', tam=tela, espaco=0, character='─')

        # Lixo e Deck
        print(f'{"┌────┐":<{int(tela / 2)}}{"┌────┐":>{int(tela / 2)}}')
        print(f'{f"│ {self.deck.qt_garbage():0>2} │ Death":<{int(tela / 2)}}', end='')
        print(f'{f"Deck │ {self.deck.qt():0>2} │":>{int(tela / 2)}}')
        print(f'{"└────┘":<{int(tela / 2)}}{"└────┘":>{int(tela / 2)}}')

        # Dealer
        dealer_count = self.dealer.count(self.second_card_is_hidden)
        bigger = len(self.dealer.get())
        if dealer_count < 21:
            dealer_status = ''
        elif dealer_count == 21 and len(self.dealer.get()) == 2:
            dealer_status = ' (Black Jack!)'
        else:
            dealer_status = ' (Estouro!)'
        Helpers.print_color(f'~ Dealer: {dealer_count:0>2}{dealer_status} ~', color='cyan', align='center',
                            style='bold', length=tela)
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

        Helpers.print_color('─' * bigger * 9, align='center', length=tela, color='pink')
        Helpers.print_color('Dealer must draw to 16 and stand on all 17\'s', align='center', length=tela, color='pink')
        Helpers.print_color('2 to 1 Insurance 2 to 1', align='center', length=tela, color='pink')

        print()
        Helpers.title(tam=tela, espaco=0)
        print()

        # Gamer
        gamer_count = self.gamer.hand.count()
        bigger = len(self.gamer.hand.get())
        if gamer_count < 21:
            gamer_status = ''
        elif gamer_count == 21 and len(self.gamer.hand.get()) == 2:
            gamer_status = ' (Black Jack!)'
        else:
            gamer_status = ' (Estouro!)'
        Helpers.print_color(f'~ Gamer 1: {gamer_count:0>2}{gamer_status} ~', color='yellow', align='center',
                            style='bold',
                            length=tela)
        cards_gamer = ''
        cards_gamer_before = ''
        cards_gamer_after = ''
        for i, card in enumerate(self.gamer.hand.get()):
            cards_gamer_before += ' ┌─────┐ '
            cards_gamer_after += ' └─────┘ '
            cards_gamer += f' │ {card} │ '
        Helpers.print_color(cards_gamer_before, color='green', style='bold', align='center', length=tela)
        Helpers.print_color(cards_gamer, color='green', style='bold', align='center', length=tela)
        Helpers.print_color(cards_gamer_after, color='green', style='bold', align='center', length=tela)

        split_count = self.split.hand.count()
        if split_count > 0:
            if len(self.split.hand.get()) > len(self.gamer.hand.get()):
                bigger = len(self.split.hand.get())
            Helpers.print_color('─' * bigger * 9, align='center', length=tela, color='pink')
            split_count = self.split.hand.count()
            Helpers.print_color(
                f'~ Gamer 2: {split_count:0>2} ~',
                color='yellow',
                align='center',
                style='bold',
                length=tela
            )
            cards_split = ''
            cards_split_before = ''
            cards_split_after = ''
            for i, card in enumerate(self.split.hand.get()):
                cards_split_before += ' ┌─────┐ '
                cards_split_after += ' └─────┘ '
                cards_split += f' │ {card} │ '
            Helpers.print_color(cards_split_before, color='green', style='bold', align='center', length=tela)
            Helpers.print_color(cards_split, color='green', style='bold', align='center', length=tela)
            Helpers.print_color(cards_split_after, color='green', style='bold', align='center', length=tela)

        # Aposta
        Helpers.print_color('─' * bigger * 9, align='center', length=tela, color='pink')
        Helpers.print_color(f'Bet...: ${self.gamer.bet:>7.1f}', align='center', length=tela, color='pink')
        Helpers.print_color(f'Amount: ${self.gamer.amount:>7.1f}', align='center', length=tela, color='pink')

        print()
        Helpers.title(tam=tela, espaco=0)
        print()

        if status != '':
            Helpers.print_color(status, color='red', style='bold', align='center', length=tela)
            print()
            Helpers.title(tam=tela, espaco=0)
            print()
