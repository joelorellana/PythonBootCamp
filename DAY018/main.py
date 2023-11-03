from colorgram import colorgram
from turtle import Turtle, Screen
import random

test= colorgram.extract('image.jpg', 10)
my_list_colors = []
for colors in test:
    my_list_colors.append((colors.rgb.r, colors.rgb.g, colors.rgb.b))

squartle = Turtle()
squartle.hideturtle()
squartle.speed(0)
squartle.penup()
my_screen = Screen()
my_screen.colormode(255)
columns = 0
squartle.setpos(-200,-200)
while columns < 10:
    for i in range(10):
        squartle.dot(20, random.choice(my_list_colors))
        if i !=9:
            squartle.forward(50)
    squartle.setheading(90)
    squartle.forward(50)
    if columns % 2 == 0:
        squartle.left(90)
    else:
        squartle.right(90)
    columns += 1
my_screen.exitonclick()
