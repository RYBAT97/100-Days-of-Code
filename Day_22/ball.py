from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('circle')
        self.speed(1)
        self.x_move_value = 10
        self.y_move_value = 10

    def move(self):
        self.goto(self.xcor() + self.x_move_value, self.ycor() + self.y_move_value)

    def wall_bounce(self):
        self.y_move_value *= -1

    def paddle_bounce(self):
        self.x_move_value *= -1