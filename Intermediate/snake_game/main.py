from turtle import Screen
from food import Food
from scoreboard import Scoreboard 
from snake import Snake
import time

WALL_THRESHOLD = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gaming = True

while gaming:
    snake.move()
    screen.update()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect collision with wall
    if snake.head.xcor() > WALL_THRESHOLD or snake.head.xcor() < -WALL_THRESHOLD or snake.head.ycor() > WALL_THRESHOLD or snake.head.ycor() < -WALL_THRESHOLD:
        scoreboard.reset_game()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]: # slices from first to end of list
        if snake.head.distance(segment) < 10:
            scoreboard.reset_game()
    time.sleep(0.1)

screen.exitonclick()
