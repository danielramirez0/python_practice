import random
import colorgram
import turtle
from turtle import Turtle, Screen

x_marker = -500
y_marker = -500
ref_image = 'rainbow.jpg'
rows = 20
cols = 20

cursor = Turtle()
cursor.speed('fastest')
cursor.hideturtle()
cursor.penup()
cursor.setx(x_marker)
cursor.sety(y_marker)

def get_colors(ref):
    colors = []
    extracted = colorgram.extract(ref, 6)
    for color in extracted:
        colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return colors

def draw_dot(color):
    cursor.dot(40, color)
    cursor.forward(50)

def draw_row():
    for _ in range(cols):
        draw_dot(random.choice(colors))
    
turtle.colormode(255)
colors = get_colors(ref_image)

for _ in range(rows):
    draw_row()
    y_marker += 50
    cursor.setx(x_marker)
    cursor.sety(y_marker)

screen = Screen()
screen.exitonclick()