from turtle import Turtle, Screen

squartle = Turtle()
my_screen = Screen()

def move_with_key():
    squartle.forward(10)

def back_with_key():
    squartle.backward(10)

def rotate():
    squartle.right(10)

def counter_rotate():
    squartle.left(10)

my_screen.listen()

my_screen.onkeypress(move_with_key,'Right')
my_screen.onkeypress(back_with_key, 'Left')
my_screen.onkeypress(rotate, 'c')
my_screen.onkeypress(counter_rotate, 'v')
my_screen.onkeypress(my_screen.resetscreen, 'q')
my_screen.exitonclick()