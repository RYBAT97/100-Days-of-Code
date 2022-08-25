from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def r_increase(self):
        self.r_score += 1

    def l_increase(self):
        self.l_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.setheading(270)
        self.pensize(1)
        for _ in range(30):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))