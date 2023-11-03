from turtle import Turtle
import random

DIRECTIONS = [+10, -10]
RAND_X = random.choice(DIRECTIONS)
RAND_Y = random.choice(DIRECTIONS)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.color("white")
        self.showturtle()
        self.move_speed = 0.07

    def move(self):
        global RAND_X
        global RAND_Y
        self.goto(self.xcor() + RAND_X, self.ycor() + RAND_Y)
        if self.ycor() > 280 or self.ycor()<-280:
            RAND_Y *= -1

    def bounce(self):
        global RAND_X
        RAND_X *= -1
        self.move()

    def reset_position(self):
        self.goto(0,0)
        global RAND_X
        RAND_X *=-1
        self.move()

    def change_speed(self):
        self.move_speed /= 1.1
