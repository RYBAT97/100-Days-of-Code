# http://codeperspectives.com/reeborg-dev/world.html

# Hurdle 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

# Hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    count = 0
    while not right_is_clear():
        move()
        count += 1
    turn_right()
    move()
    turn_right()
    while count > 0:
        move()
        count -= 1
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

# Maze Project

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if not right_is_clear():
        if not front_is_clear():
            turn_left()
        else:
            move()
    elif right_is_clear() and front_is_clear():
        move()
    else:
        turn_right()
        move()

