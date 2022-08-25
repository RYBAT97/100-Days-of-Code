import time
from turtle import Screen
from Day_22.paddle import Paddle
from Day_22.ball import Ball
from Day_22.scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.title('Pong 1.0')
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

ball = Ball()

r_score = 0
l_score = 0
scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_is_in = True
sleep_duration = 0.1

while game_is_in:
    screen.update()
    time.sleep(sleep_duration)

    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 325) or (ball.distance(l_paddle) < 50 and ball.xcor() < -325):
        ball.paddle_bounce()
        # Increase speed after each score
        sleep_duration *= 0.9

    # Detect out-of-bound situation
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            scoreboard.l_increase()
        else:
            scoreboard.r_increase()
        ball.paddle_bounce()
        ball.goto(0, 0)
        # Reset speed
        sleep_duration = 0.1

    scoreboard.update_scoreboard()

screen.exitonclick()
