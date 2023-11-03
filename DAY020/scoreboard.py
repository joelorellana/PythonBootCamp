from turtle import Turtle
ALIGN = "center"
FONT = ("Consolas", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as max_score:
            self.high_score = int(max_score.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=280)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Actual Score: {self.score}, High Score: {self.high_score}",align=ALIGN, font=FONT)

    def update_score(self):
        self.score +=1
        self.show_score()

    #def game_over(self):
        #self.goto(0,0)
        #self.write(f"CAME OVER", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as max_score:
                max_score.write(str(self.high_score))
        self.score = 0
        self.show_score()