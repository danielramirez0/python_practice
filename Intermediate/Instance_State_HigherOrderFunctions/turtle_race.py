from operator import truediv
import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_start_marker = -100
x_start_marker = -230

def print_colors():
    str = ""
    for color in colors:
        if color == "purple":
            str = str + color
        else:
            str = str + color + " "
    return str

def make_turtles():
    y_incrementer = 0
    for color in colors:
        turtle = Turtle()
        turtle.penup()
        turtle.color(color)
        turtle.shape("turtle")
        turtle.goto(x_start_marker, y_start_marker + y_incrementer)
        turtles.append(turtle)
        y_incrementer += 50


def race_turtles(turtles):
    racing = True
    while racing == True:
        for turtle in turtles:
            turtle.forward(random.randint(0,10))
            if turtle.xcor() > 230:
                racing == False
                return turtle.pencolor()


screen = Screen()
screen.setup(width=500, height=400)

bet = ""
while True:
    bet = screen.textinput(title="Place your bet", prompt="Enter color: " + print_colors())
    if bet in colors:
        print("You bet it all on " + bet)
        break

make_turtles()

result = race_turtles(turtles)

if result == bet:
    print(f"Good bet! {result} won the race!")
else:
    print(f"Sorry {bet} lost the race!")

screen.exitonclick()