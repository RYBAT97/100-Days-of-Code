from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.pencolor('black')
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def level_increase(self):
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 250)
        self.setheading(0)
        self.pensize(1)
        for _ in range(30):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()
        self.goto(-215, 255)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 24, "normal"))

