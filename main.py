from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.add_tail()

    # Detect wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 5:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
