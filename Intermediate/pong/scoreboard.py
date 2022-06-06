from turtle import Turtle

FONT_ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_SIZE = 80
FONT_STYLE = "normal"
FONT_COLOR = "white"
L_POSITION = (-100, 200)
R_POSITION = (100, 200)

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(FONT_COLOR)
        self.setposition(0, 270)
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    
    def update_score(self):
        self.goto(L_POSITION)
        self.write(f"{self.l_score}", align=FONT_ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
        self.goto(R_POSITION)
        self.write(f"{self.r_score}", align=FONT_ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=FONT_ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))

    def increase_score(self, side):
        self.clear()
        if side == "left":
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_score()