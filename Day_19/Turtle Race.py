from turtle import Turtle, Screen
import random

red_turtle = Turtle()
orange_turtle = Turtle()
yellow_turtle = Turtle()
green_turtle = Turtle()
blue_turtle = Turtle()
purple_turtle = Turtle()

turtles = [red_turtle, orange_turtle, yellow_turtle, green_turtle, blue_turtle, purple_turtle]

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(6):
    turtles[i].color(colors[i])
    turtles[i].shape("turtle")
    turtles[i].penup()


def start_turtle_positions():
    start_degree = 0
    for j in range(6):
        turtles[j].goto(-225, -125 + start_degree)
        start_degree += 50


def start_race():
    while True:
        for k in range(6):
            turtles[k].forward(random.randint(1, 10))
            if turtles[k].xcor() >= 225:
                winner = turtles[k].fillcolor()
                return winner


screen = Screen()
screen.setup(width=500, height=400)
chosen_winner = screen.textinput(title='Make your bet!', prompt="Which turtle is going to win?\n(Red, Orange, Yellow, "
                                                                "Green, Blue or Purple?)")
chosen_winner = chosen_winner.lower()
start_turtle_positions()

winner_turtle = start_race()

if chosen_winner == winner_turtle:
    print("Congratulation! You've won!")
else:
    print("Sorry :( You did not win...")

screen.exitonclick()
