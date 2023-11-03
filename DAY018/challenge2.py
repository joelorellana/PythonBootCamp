from turtle import Turtle, Screen
from random import randint

squartle = Turtle()
squartle.shape("turtle")
my_screen = Screen()
my_screen.colormode(255)
for i in range(3,11):
    squartle.color(randint(0,255),randint(0,255),randint(0,255))
    for v in range(i):
        squartle.forward(100)
        squartle.right(360/i)
    squartle.home()
my_screen.exitonclick()
