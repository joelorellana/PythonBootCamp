# POKEMON APP
from turtle import Turtle, Screen
import random
colors = ["red", "black", "green", "gray", "blue", "yellow"]
my_screen = Screen()
my_screen.setup(width=500, height=400)
my_screen.colormode(255)

my_turtle_list = []
def start_game(user_choice):
    race = True
    while race:
        for i in my_turtle_list:
            if i.xcor()>230:
                race = False
                win_color = i.pencolor()
                if win_color == user_choice:
                    print(f" Congratulations! The {win_color} is the turtle winner!")
                else:
                    print(f"You lose! The winner is {win_color}")
            else:
                i.forward(random.randint(0,10))

for i in range(6):
    squirtle = Turtle(shape="turtle")
    my_turtle_list.append(squirtle)
    my_turtle_list[i].color(colors[i])
    my_turtle_list[i].penup()
    my_turtle_list[i].goto(x=-240, y=-80+40*i)

user_choice = my_screen.textinput(title="Haga su apuesta", prompt="Cuál Pokémon ganará?").lower()
if user_choice
start_game(user_choice)

my_screen.exitonclick()
