from random import choice, choices
from player import Player
class Dealer(Player):
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        super().__init__(name='Mrs. Dealer')

    def deal_cards(self, players):
        for player in players:
            player.hand = choices(self.cards, k=2)
            player.set_score()
        self.hand = choices(self.cards, k=2)
        super().set_score()

    def hit(self, player):
        player.hand.append(choice(self.cards))
        player.set_score()
