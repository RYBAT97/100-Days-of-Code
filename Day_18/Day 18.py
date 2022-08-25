from turtle import Turtle, Screen
import random

colors_list = ['', '', '', 'red', 'green', 'blue', 'cyan', 'brown', 'black', 'yellow', 'purple']
random_degrees = [90, 180, 270, 360]


def draw_square(my_turtle):
    for i in range(4):
        my_turtle.right(90)
        my_turtle.forward(100)


def draw_dashed(my_turtle):
    for i in range(15):
        my_turtle.pendown()
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)


def draw_weird(my_turtle):
    for i in range(3, 11):
        for j in range(0, i):
            my_turtle.pencolor(colors_list[i])
            my_turtle.right(360 / i)
            my_turtle.forward(100)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_walk(my_turtle):
    for i in range(100):
        my_turtle.right(random.choice(random_degrees))
        my_turtle.pencolor(random_color())
        my_turtle.forward(20)


def draw_spirograph(my_turtle):
    my_turtle.speed(0)
    for j in range(60):
        my_turtle.pencolor(random_color())
        for i in range(60):
            my_turtle.right(6)
            my_turtle.forward(10)
        my_turtle.right(6)


def draw_spirograph_Angelas_version(my_turtle):
    my_turtle.speed(0)
    for j in range(60):
        my_turtle.pencolor(random_color())
        my_turtle.circle(100)
        my_turtle.right(6)

tim = Turtle()
tim.shape("turtle")
tim.color('violet')

screen = Screen()
screen.colormode(255)

# Draw Square
# draw_square(tim)

# Draw dashed line
# draw_dashed(tim)

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# draw_weird(tim)

# Random Walk
# tim.pensize(10)
# tim.speed('fast')
# random_walk(tim)

# Draw spirograph
# draw_spirograph(tim)
draw_spirograph_Angelas_version(tim)

screen.exitonclick()
