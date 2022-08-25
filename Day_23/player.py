from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_YCOR = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape('turtle')

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
