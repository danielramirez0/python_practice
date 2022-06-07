from turtle import Turtle

FONT_ALIGNMENT = "center"
FONT_NAME = "Arial"
FONT_COLOR = "black"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color(FONT_COLOR)
        self.goto(-220, 260)
        self.update_score()
    
    def update_score(self):
        self.write(f"Level: {self.level}", align=FONT_ALIGNMENT, font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=FONT_ALIGNMENT, font=(FONT))

    def increase_score(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=FONT_ALIGNMENT, font=(FONT))