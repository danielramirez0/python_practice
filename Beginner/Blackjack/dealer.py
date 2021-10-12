from random import choices
class Dealer:
    def __init__(self):
        self.cards = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.hand = list
        self.score = int

    def deal_cards(self, players):
        for player in players:
            player.hand = choices(self.cards, k=2)
        self.hand = choices(self.cards, k=2)