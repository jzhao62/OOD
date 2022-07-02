class Card:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Hand:
    def __init__(self):
        self.cards = []

    def get_possible_values(self):
        pass

    def get_best_value(self):
        pass

    def insert_card(self, card):
        self.cards.insert(card)

    def print_hand(self):
        pass

class NormalPlayer:
    def __init__(self, id, bets):
        self.game = None
        self.id = id
        self.hand = Hand()
        self.total_bets = bets
        self.bets = 0
        try:
            self.place_bets(bets)
        except ValueError:
            print(ValueError)
        self.stop_dealing = False

    def get_id(self): pass
    def insert_card(self, card): pass
    def get_best_value(self): pass
    def stop_dealing(self): pass
    def join_game(self, game):
        self.game = game
        game.add_player = self

    def place_bets(self, amount):
        if self.total_bets < amount:
            raise "Not enough money"
        self.bets = amount
        self.total_bets -= self.bets



class Dealer:
    def __init_(self):
        self.game = None
        self.hand = Hand()
        bets = 10000

    def insert_card(self, card):
        self.hand.insert_card(card)

    def larger_than(self, normal_player):
        pass

    def update_bets(self, amount):
        self.bets += amount

    def set_game(self, game):
        self.game = game

    # 根据游戏规则，处理下一张手牌
    def deal_next_card(self):
        pass

    # print dealer outputs
    def print_dealer(self):
        pass


class black_jack:
    def __init__(self):
        self.players = []
        self.dealer
