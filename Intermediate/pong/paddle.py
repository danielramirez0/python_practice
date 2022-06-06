from turtle import Turtle

MOVE_DISTANCE = 20
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1
PADDLE_SPEED = "fastest"

class Paddle(Turtle):

    def __init__(self, x_start) -> None:
        super().__init__()
        self.penup()
        self.speed(PADDLE_SPEED)
        self.goto(x_start, 0)
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH)
    
    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
