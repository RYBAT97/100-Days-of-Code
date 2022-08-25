from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    tim.right(15)


def rotate_counter_clockwise():
    tim.left(15)


def clear_drawing():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=rotate_clockwise, key='d')
screen.onkey(fun=rotate_counter_clockwise, key='a')
screen.onkey(fun=clear_drawing, key='c')
screen.exitonclick()
