from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, posx, posy):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.goto(posx,posy)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.showturtle()
        self.color("white")

    def movepaddleup(self):
        self.goto(self.xcor(), 40+self.ycor())

    def movepaddledown(self):
        self.goto(self.xcor(), self.ycor()-40)