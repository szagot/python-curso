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
    bet_max = 300
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
        self.print_table(new_game=True)

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
            self.end_hound()
            return True
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

    def end_hound(self):
        """
        Faz a contagem e paga ou recolhe as apostas
        """

        split = self.split.hand.count()
        gamer = self.gamer.hand.count()
        dealer = self.dealer.count()
        win = ''

        # Em caso de rendição, completa o hit do Dealer
        if dealer < 17:
            self.dealer_active = True
            self.split_active = False
            self.hit()
            return

        # Black Jack!
        split_bj = len(self.split.hand.get()) == 2 and split == 21
        gamer_bj = len(self.gamer.hand.get()) == 2 and gamer == 21
        dealer_bj = len(self.dealer.get()) == 2 and dealer == 21
        if split_bj or gamer_bj or dealer_bj:
            # Gamer
            if gamer_bj and not dealer_bj:
                self.gamer.bet_wins()
                win = 'Gamer 1 Ganha de Bancada'
            elif dealer_bj and not gamer_bj:
                self.gamer.bet_lost()
                win = 'Bancada Ganha de Gamer 1'
            elif dealer_bj and gamer_bj:
                self.gamer.game_tie()
                win = 'Gamer 1 e Bancada Empatam!'

            # Split
            if split > 0:
                if split_bj and not dealer_bj:
                    self.split.bet_wins()
                    win += ' | Gamer 2 Ganha de Bancada'
                elif dealer_bj and not split_bj:
                    self.split.bet_lost()
                    win += ' | Bancada Ganha de Gamer 2'
                elif dealer_bj and split_bj:
                    self.split.game_tie()
                    win += ' | Gamer 2 e Bancada Empatam!'

                self.gamer.amount += self.split.amount
                self.split.amount = 0
                self.split.bet = 0

        # (sem Black Jack)
        else:
            # Gamer
            if dealer > 21 >= gamer or dealer < gamer <= 21:
                self.gamer.bet_wins()
                win = 'Gamer 1 Ganha de Bancada'
            elif gamer == dealer:
                self.gamer.game_tie()
                win = 'Gamer 1 e Bancada Empatam!'
            else:
                self.gamer.bet_lost()
                win = 'Bancada Ganha de Gamer 1'

            # Split
            if split > 0:
                if dealer > 21 >= split or dealer < split <= 21:
                    self.split.bet_wins()
                    win += ' | Gamer 2 Ganha de Bancada'
                elif split == dealer:
                    self.split.game_tie()
                    win += ' | Gamer 2 e Bancada Empatam!'
                else:
                    self.split.bet_lost()
                    win += ' | Bancada Ganha de Gamer 2'

                self.gamer.amount += self.split.amount
                self.split.amount = 0
                self.split.bet = 0

        self.print_table(win)

    def slice(self):
        if not self.gamer.split_verify():
            return False

        # Divide a mão
        self.split.hand.free()
        self.split.hand.add(self.gamer.hand.get()[1])
        self.gamer.hand.cards.pop(1)

        # Divide a aposta
        self.split.amount = 0
        self.split.bet = self.gamer.bet
        self.gamer.amount -= self.split.bet

        # Entrega cartas
        self.gamer.hand.add(self.deck.get_card())
        self.split.hand.add(self.deck.get_card())

        self.print_table()

    def end_game(self):
        Helpers.print_color('Fim de Jogo!', color='red', style='bold', length=self.screen, align='center')
        print()
        Helpers.title(tam=self.screen, espaco=0, character='─')

    def print_table(self, status='', new_game=False):
        """
        Impressão de tela
        :param new_game: É um novo jogo?
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

        # Aposta inicial realizada?
        if self.gamer.bet == 0 and new_game:
            while True:
                error = False
                bet = 0
                try:
                    print(f'Caixa: {self.gamer.amount}')
                    bet = float(input('Aposta Inicial: '))

                except ValueError:
                    error = True

                if error or 0 > bet > self.bet_max or bet > self.gamer.amount:
                    Helpers.print_color('Valor inválido! Tente novamente.', color='red')
                    Helpers.print_color(f'Min: 1, Máx: {self.bet_max}', color='pink')
                else:
                    break

                print('-' * 20)

            self.gamer.betting(bet)

            self.print_table()
            return

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
        Helpers.print_color('Bet: min. 1, max 300', align='center', length=tela, color='pink')

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
        Helpers.print_color(
            f'Bet...: ${self.gamer.bet + self.split.bet:>7.1f}',
            align='center', length=tela, color='pink'
        )
        if self.gamer.insurance > 0:
            Helpers.print_color(f'Insurance: ${self.gamer.insurance:>7.1f}', align='center', length=tela, color='pink')
        Helpers.print_color(f'Amount: ${self.gamer.amount:>7.1f}', align='center', length=tela, color='pink')

        print()
        Helpers.title(tam=tela, espaco=0)
        print()

        if status != '':
            Helpers.print_color(status, color='red', style='bold', align='center', length=tela)
            print()
            Helpers.title(tam=tela, espaco=0)
            input('Press [ENTER] to continue...')
            self.start()
        else:
            for value in self.plays.values():
                print(value, end=' | ')

            while True:
                jogada = str(input('-> Jogada: ')).strip().lower()
                if jogada in self.plays.keys():
                    break
                Helpers.print_color('Opção inválida. Escolha uma das opções acima!')

            print()
            Helpers.title(tam=tela, espaco=0)
            print()

            if jogada == 'e':
                self.end_game()
            elif jogada == 'h':
                self.hit()
            elif jogada == 's':
                self.stand()
            elif jogada == 'u':
                self.end_hound()
            else:
                self.print_table()
