import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
p = Turtle()
p.shape(None)
p.speed('fastest')

def draw_circle(heading):
    p.color(random_color())
    p.setheading(heading)
    p.circle(200)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def draw_spirograph(degree_shift):
    for n in range(int(360 / degree_shift)):
        draw_circle(p.heading() + degree_shift)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
