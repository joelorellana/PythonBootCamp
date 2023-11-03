from turtle import Turtle, Screen
from random import randint

squartle = Turtle()
squartle.pensize(5)
squartle.hideturtle()
squartle.speed(0)
my_screen = Screen()
my_screen.colormode(255)
while True:
    squartle.color(randint(0,255),randint(0,255),randint(0,255))
    squartle.forward(20)
    squartle.right(90*randint(0,3))
my_screen.exitonclick()