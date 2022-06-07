from turtle import Turtle

FONT_ALIGNMENT = "center"
FONT_NAME = "Arial"
FONT_SIZE = 24
FONT_STYLE = "normal"
FONT_COLOR = "white"

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color(FONT_COLOR)
        self.setposition(0, 270)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=FONT_ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()