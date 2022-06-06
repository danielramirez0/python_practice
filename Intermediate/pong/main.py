import time
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard 
from paddle import Paddle

WALL_THRESHOLD = 280
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
TITLE = "PONG"

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title(TITLE)
screen.tracer(0)

left_paddle = Paddle(-350)
right_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "i")
screen.onkey(right_paddle.move_down, "k")
gaming = True



while gaming:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() < -380:
        scoreboard.increase_score("right")
        ball.reset() 

    if ball.xcor() > 380:
        scoreboard.increase_score("left")
        ball.reset() 
    
    time.sleep(ball.move_speed)

screen.exitonclick()
