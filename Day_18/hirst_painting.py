import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract('dot_painting.jpg', 2 ** 32)
rgb_colors = []

for item in colors:
    if not (item.rgb.r > 245 and item.rgb.g > 245 and item.rgb.b > 245):
        rgb_colors.append(tuple(item.rgb))

print(rgb_colors)  # For some reason, less than the actual number of colors is extracted

tim = Turtle()
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

my_screen = Screen()
my_screen.colormode(255)

for _ in range(10):
    for _ in range(10):
        tim.pendown()
        current_color = random.choice(rgb_colors)
        tim.pencolor(current_color)
        tim.fillcolor(current_color)
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        # tim.dot(20, current_color)
        tim.penup()
        tim.forward(50)
    tim.right(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)


my_screen.exitonclick()
