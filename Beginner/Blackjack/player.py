class Player:
    def __init__(self, name):
        self.name = name
        self.hand = list
        self.score = int
        self.playing = True
        self.busted = False

    def __str__(self) -> str:
        return self.name
    
    def set_score(self):
        self.score = 0
        for card in self.hand:
            self.score += card

    def bid(self):
        pass

    def double_down(self):
        pass

    def hold(self):
        self.playing = False

    def bust(self):
        self.playing = False
        self.busted = True
