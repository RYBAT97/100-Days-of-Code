import time
from turtle import Screen
from Day_24.Snake import Snake
from Day_24.Food import Food
from Day_24.Scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game 0.1")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Start snake's movement
    snake.move()

    # Find collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.score += 1
        score_board.refresh()
        snake.extend()

    # Detect collision with wall
    if -280 > snake.head.xcor() or snake.head.xcor() > 280 or -280 > snake.head.ycor() or snake.head.ycor() > 280:
        score_board.reset_game()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset_game()
            snake.reset_snake()

screen.exitonclick()
