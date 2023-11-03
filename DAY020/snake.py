from turtle import Turtle

MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, large=3):
        self.large = large
        self.my_snake_list = []
        self.create_snake()

    def create_snake(self):
        for i in range(self.large):
            self.my_snake_list.append(Turtle(shape="square"))
            self.my_snake_list[i].penup()
            self.my_snake_list[i].color("white")
            self.my_snake_list[i].setposition(x=-20 * i, y=0)
        self.head = self.my_snake_list[0]

    def add_new_segment(self):
        z = len(self.my_snake_list) - 1  # posicion del ultimo elemento a agregar
        last_x = self.my_snake_list[z].xcor()
        last_y = self.my_snake_list[z].ycor()
        self.my_snake_list.append(Turtle(shape="square"))
        self.my_snake_list[z].penup()
        self.my_snake_list[z].setposition(x=last_x, y=last_y)
        self.my_snake_list[z].color("white")

    def move(self):
        for seg_num in range(len(self.my_snake_list) - 1, 0, -1):
            new_x = self.my_snake_list[seg_num - 1].xcor()
            new_y = self.my_snake_list[seg_num - 1].ycor()
            self.my_snake_list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for i in range(len(self.my_snake_list)):
            self.my_snake_list[i].color("black")
        self.my_snake_list.clear()
        self.create_snake()
