# SANKE GAME
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("SNAKE by JoelDev89.")
my_screen.tracer(0)
my_snake = Snake()
my_food = Food()
my_score = Scoreboard()
my_screen.listen()
my_screen.onkey(my_snake.up,"Up")
my_screen.onkey(my_snake.down,"Down")
my_screen.onkey(my_snake.right,"Right")
my_screen.onkey(my_snake.left,"Left")

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()
    #Detect collision
    if my_snake.head.distance(my_food) < 20:
        my_food.refresh()
        my_score.update_score()
        my_snake.add_new_segment()

    if my_snake.head.xcor()>290 or my_snake.head.xcor()<-290 or my_snake.head.ycor()>290 or my_snake.head.ycor()<-290:
        my_score.reset_score()
        my_snake.reset_snake()

    #detect collision
    for segment in my_snake.my_snake_list[1:]:
        if my_snake.head.distance(segment) <10:
            my_score.reset_score()

my_screen.exitonclick()
