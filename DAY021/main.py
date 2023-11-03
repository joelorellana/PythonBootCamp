# SNAKE GAME PART 2
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_on = True
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.title("PONG GAME by JoelDev89")
my_screen.bgcolor("black")
my_screen.tracer(0)
paddle_right = Paddle(350,0)
paddle_left = Paddle(-350,0)

my_ball = Ball()
my_scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkeypress(paddle_right.movepaddleup,"Up")
my_screen.onkeypress(paddle_right.movepaddledown,"Down")
my_screen.onkeypress(paddle_left.movepaddledown, "s")
my_screen.onkeypress(paddle_left.movepaddleup, "w")
while game_on:
    my_screen.update()
    time.sleep(my_ball.move_speed)
    my_ball.move()

    #detect collision
    if (my_ball.distance(paddle_right)<60 and my_ball.xcor()>340) or (my_ball.distance(paddle_left)<60 and my_ball.xcor()<-340):
        my_ball.bounce()
        my_ball.change_speed()

    #detect ball pass
    if my_ball.xcor() > 380:
        my_ball.reset_position()
        my_scoreboard.left_point()

    if my_ball.xcor() < -380:
        my_ball.reset_position()
        my_scoreboard.right_point()

my_screen.exitonclick()

#class Player
#class Ball
#class Score
#class Stadium
