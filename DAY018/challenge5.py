from turtle import Turtle, Screen
from random import randint
squartle = Turtle()
squartle.shape("turtle")
# squartle.hideturtle()
squartle.speed(0)
angle = 0
my_screen = Screen()
my_screen.colormode(255)
while angle < 360:
    squartle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    squartle.right(2)
    squartle.circle(-100)
    angle += 2
my_screen.exitonclick()
