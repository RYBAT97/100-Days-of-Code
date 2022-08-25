from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.segments.append(Turtle())
            self.segments[i].color('white')
            self.segments[i].shape('square')
            self.segments[i].penup()
            self.segments[i].speed('slowest')

        for j in range(1, 3):
            self.segments[j].goto(self.segments[j - 1].xcor() - 20, 0)

    def extend(self):
        new_segment = Turtle()
        new_segment.color('white')
        new_segment.shape('square')
        new_segment.penup()
        new_segment.speed('slowest')
        self.segments.append(new_segment)
        self.segments[-1].goto(self.segments[-2].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)
