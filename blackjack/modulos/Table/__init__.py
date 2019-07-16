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
    plays: dict

    def __init__(self):
        self.dealer = Hand()
        self.gamer = Gamer()
        self.split = Gamer()
        self.deck = Deck()
        self.start()

    def init_plays(self):
        self.plays = {'h': '[H]it', 's': '[S]tand', 'u': 'S[u]rrender', 'e': '[E]xit'}
        # Double
        if (len(self.gamer.hand.get()) == 2 and not self.split_active and not self.dealer_active) or (
                len(self.split.hand.get()) == 2 and self.split_active):
            self.plays['d'] = '[D]ouble'
        # Split
        if self.gamer.split_verify() and not self.split_active and not self.dealer_active:
            self.plays['p'] = 'S[p]lit'
        # Insurance
        if self.second_card_is_hidden and not self.split_active and \
                self.dealer.get()[0].get_number() == 'A' and self.gamer.insurance == 0:
            self.plays['i'] = '[I]nsurance'

    def start(self):
        if not self.verify_deck():
            self.end_game()

        """
        Inicia o Jogo
        """
        # Libera a mão
        self.dealer.free()
        self.gamer.hand.free()
        self.split.hand.free()
        self.second_card_is_hidden = True
        self.gamer.bet = 0
        self.split.bet = 0

        # Dá as cartas do Dealer
        self.dealer.add(self.deck.get_card())
        self.dealer.add(self.deck.get_card())

        # Dá as cartas do Jogador
        self.gamer.hand.add(self.deck.get_card())
        self.gamer.hand.add(self.deck.get_card())

        # Verifica se o Gamer não teve Black Jack de cara
        if self.gamer.hand.count() == 21:
            self.hit()
        else:
            # Imprime a tela
            self.print_table(new_game=True)

    def verify_deck(self):
        """
        Retorna se o deck ainda tem cartas
        :rtype: bool
        """
        if self.deck.qt() < 10:
            self.deck = Deck()

        return self.deck.qt_garbage() < 90 and (self.gamer.amount >= 1 or self.gamer.bet > 0 or self.split.bet > 0)

    def hit(self, is_double=False):
        """
        Dá um hit para a mão da vez
        :param is_double: É pra dobrar?
        :rtype: bool
        """
        if not self.verify_deck():
            self.end_hound()
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

        if not self.dealer_active and (self.gamer.hand.count() >= 21 or self.split.hand.count() >= 21):
            self.stand()
        elif not self.verify_deck() or (not self.dealer_active and self.gamer.hand.count() >= 21):
            self.end_hound()
            return False

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

    def insurance(self):
        self.gamer.add_insurance()
        self.print_table()

    def end_hound(self):
        """
        Faz a contagem e paga ou recolhe as apostas
        """

        split = self.split.hand.count()
        gamer = self.gamer.hand.count()
        dealer = self.dealer.count()
        win = ''

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
            if gamer == dealer or gamer > 21 < dealer:
                self.gamer.game_tie()
                win = 'Gamer 1 e Bancada Empatam!'
            elif dealer > 21 >= gamer or dealer < gamer <= 21:
                self.gamer.bet_wins()
                win = 'Gamer 1 Ganha de Bancada'
            else:
                self.gamer.bet_lost()
                win = 'Bancada Ganha de Gamer 1'

            # Split
            if split > 0:
                if split == dealer or split > 21 < dealer:
                    self.split.game_tie()
                    win += ' | Gamer 2 e Bancada Empatam!'
                elif dealer > 21 >= split or dealer < split <= 21:
                    self.split.bet_wins()
                    win += ' | Gamer 2 Ganha de Bancada'
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
        self.gamer.game_tie()
        Helpers.print_color('Fim de Jogo!', color='red', style='bold', length=self.screen, align='center')
        Helpers.print_color('─' * 14, align='center', length=self.screen, color='pink')
        Helpers.print_color(f'Amount: ${self.gamer.amount:>7.1f}', align='center', length=self.screen, color='pink')
        print()
        Helpers.title(tam=self.screen, espaco=0, character='─')
        exit()

    def print_table(self, status='', new_game=False, end_game=False):
        """
        Impressão de tela
        :param end_game: É fim de Jogo?
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
        if self.gamer.bet == 0 and new_game and self.verify_deck() and not end_game:
            while True:
                error = False
                bet = 0
                try:
                    print(f'Caixa: {self.gamer.amount}')
                    bet = float(input('Aposta Inicial (0 para sair): '))

                except ValueError:
                    error = True

                if bet == 0:
                    self.print_table(end_game=True)
                    return
                elif error or bet > self.bet_max or bet > self.gamer.amount:
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
        if dealer_count == 21 and len(self.dealer.get()) == 2:
            dealer_status = ' (Black Jack!)'
        elif dealer_count <= 21:
            dealer_status = ''
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
        if gamer_count == 21 and len(self.gamer.hand.get()) == 2:
            gamer_status = ' (Black Jack!)'
        elif gamer_count <= 21:
            gamer_status = ''
        else:
            gamer_status = ' (Estouro!)'
        Helpers.print_color(
            f'~ Gamer 1: {gamer_count:0>2}{gamer_status} ~',
            color='yellow' if not self.split_active else 'gray',
            align='center',
            style='bold' if not self.split_active else 'none',
            length=tela
        )
        cards_gamer = ''
        cards_gamer_before = ''
        cards_gamer_after = ''
        for i, card in enumerate(self.gamer.hand.get()):
            cards_gamer_before += ' ┌─────┐ '
            cards_gamer_after += ' └─────┘ '
            cards_gamer += f' │ {card} │ '
        color = 'green' if not self.split_active else 'gray'
        bold = 'bold' if not self.split_active else 'none'
        Helpers.print_color(cards_gamer_before, color=color, style=bold, align='center', length=tela)
        Helpers.print_color(cards_gamer, color=color, style=bold, align='center', length=tela)
        Helpers.print_color(cards_gamer_after, color=color, style=bold, align='center', length=tela)

        # Gamer
        split_count = self.split.hand.count()
        if split_count == 21 and len(self.split.hand.get()) == 2:
            split_status = ' (Black Jack!)'
        elif split_count <= 21:
            split_status = ''
        else:
            split_status = ' (Estouro!)'
        if split_count > 0:
            if len(self.split.hand.get()) > len(self.gamer.hand.get()):
                bigger = len(self.split.hand.get())
            Helpers.print_color('─' * bigger * 9, align='center', length=tela, color='pink')
            split_count = self.split.hand.count()
            Helpers.print_color(
                f'~ Gamer 2: {split_count:0>2}{split_status} ~',
                color='yellow' if self.split_active else 'gray',
                align='center',
                style='bold' if self.split_active else 'none',
                length=tela
            )
            cards_split = ''
            cards_split_before = ''
            cards_split_after = ''
            for i, card in enumerate(self.split.hand.get()):
                cards_split_before += ' ┌─────┐ '
                cards_split_after += ' └─────┘ '
                cards_split += f' │ {card} │ '
            color = 'green' if self.split_active else 'gray'
            bold = 'bold' if self.split_active else 'none'
            Helpers.print_color(cards_split_before, color=color, style=bold, align='center', length=tela)
            Helpers.print_color(cards_split, color=color, style=bold, align='center', length=tela)
            Helpers.print_color(cards_split_after, color=color, style=bold, align='center', length=tela)

        # Aposta
        Helpers.print_color('─' * bigger * 9, align='center', length=tela, color='pink')
        Helpers.print_color(
            f'Bet...: ${self.gamer.bet + self.split.bet:>7.1f}',
            align='center', length=tela, color='pink'
        )
        if self.gamer.insurance > 0:
            Helpers.print_color(f'Insur.: ${self.gamer.insurance:>7.1f}', align='center', length=tela, color='pink')
        Helpers.print_color(f'Amount: ${self.gamer.amount:>7.1f}', align='center', length=tela, color='pink')

        print()
        Helpers.title(tam=tela, espaco=0)
        print()

        if end_game:
            self.end_game()
        elif status != '':
            Helpers.print_color(status, color='red', style='bold', align='center', length=tela)
            print()
            Helpers.title(tam=tela, espaco=0)
            if self.verify_deck():
                input('Press [ENTER] to continue...')
                self.start()
            else:
                self.end_game()
        elif self.verify_deck():
            self.init_plays()
            Helpers.print_color(f'Gamer {"2" if self.split_active else "1"}', color='blue', style='bold', end='')
            for i, value in enumerate(self.plays.values()):
                if i == 0:
                    print(f' ({value}', end='')
                else:
                    print(f' | {value}', end='')
            print(')')
            while True:
                jogada = str(input('Jogada: ')).strip().lower()
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
                self.second_card_is_hidden = False
                self.end_hound()
            elif jogada == 'd':
                self.hit(True)
            elif jogada == 'p':
                self.slice()
            elif jogada == 'i':
                self.insurance()
            else:
                self.print_table()
        else:
            self.end_game()
