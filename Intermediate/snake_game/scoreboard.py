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
        self.hideturtle()
        self.penup()
        self.color(FONT_COLOR)
        self.setposition(0, 270)
        self.update_score()
    
    def update_score(self):
        self.write(f"Score: {self.score}", align=FONT_ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=FONT_ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()