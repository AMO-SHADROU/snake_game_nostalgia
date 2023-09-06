from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
    # Detect collision with head
    for part in snake.full_snake[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()
my_screen.exitonclick()
