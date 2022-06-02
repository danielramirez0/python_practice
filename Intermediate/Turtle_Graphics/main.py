#####Turtle Intro######
from turtle import Turtle as t, Screen as s
timmy_the_turtle = t()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
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

screen = s()
screen.exitonclick()
