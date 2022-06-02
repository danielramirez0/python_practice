#####Turtle Intro######
import random
from turtle import Turtle as t, Screen as s, right
import turtle

timmy_the_turtle = t()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.speed(10)

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1 :
#         break
# end_fill()



######## Challenge 1 - Draw a Square ############

timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)


######## Challenge 2 - Draw a Dashed Line ############

for n in range(1, 50):
    if n % 2 == 0:
        timmy_the_turtle.penup()
    else:
        timmy_the_turtle.pendown()

    timmy_the_turtle.forward(10)

timmy_the_turtle.clear()
timmy_the_turtle.right(90)
timmy_the_turtle.penup()
timmy_the_turtle.back(100)
timmy_the_turtle.pendown()

######## Challenge 3 - Draw multiple shapes #############

# triangle
# for n in range(0, 3):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360 / 3)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "lightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape in range(3, 11):
    # i = random.randint(0, len(colors))
    # timmy_the_turtle.pencolor(colors[i])
    # colors.remove(colors[i])
    timmy_the_turtle.pencolor(random.choice(colors))
    draw_shape(shape)

timmy_the_turtle.clear()
timmy_the_turtle.penup()
timmy_the_turtle.home()
timmy_the_turtle.shape()
timmy_the_turtle.pendown()
timmy_the_turtle.pensize(10)

######## Challenge 4 - Draw Random Walk #############

# change color mode for rgb
turtle.colormode(255)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

for _ in range(200):
    # timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(random.choice(directions))



screen = s()
screen.exitonclick()