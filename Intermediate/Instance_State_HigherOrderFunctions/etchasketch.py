from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def rotate_clockwise():
    turtle.setheading(turtle.heading() + 5)

def rotate_counter_clockwise():
    turtle.setheading(turtle.heading() - 5)

def clear_reset():
    turtle.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_clockwise)
screen.onkey(key="d", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear_reset)





screen.exitonclick()