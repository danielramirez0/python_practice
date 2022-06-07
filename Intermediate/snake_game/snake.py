from turtle import Turtle as t

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_segment(self, position):
        segment = t("square")
        segment.penup()
        segment.color("white")
        segment.setposition(position)
        return segment

    def create_snake(self):
        x_offset = 0
        for _ in range(3):
            position = (x_offset, 0)
            self.segments.append(self.create_segment(position))
            x_offset -= 20
    
        
    def move(self):
        for i in range(len(self.segments) -1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i -1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def extend(self):
        self.segments.append(self.create_segment(self.segments[-1].position()))

    def reset_snake(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
