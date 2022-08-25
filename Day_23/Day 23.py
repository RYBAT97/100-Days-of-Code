import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
speed = 0.01

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('white')
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()

screen.onkey(fun=player.move, key='Up')

game_in_on = True
is_collision_detected = False
blocks_list = []

while game_in_on:
    time.sleep(speed)
    screen.update()

    blocks_list.append(CarManager())

    for item in blocks_list:
        if item.distance(player) < 20:
            is_collision_detected = True

    for item in blocks_list:
        item.move()
        if item.xcor() > 350:
            blocks_list.remove(item)

    if player.ycor() > 250:
        scoreboard.level += 1
        speed *= 0.95
        player.reset_position()

    if is_collision_detected:
        scoreboard.game_over()
        break

    scoreboard.update_scoreboard()

screen.exitonclick()
