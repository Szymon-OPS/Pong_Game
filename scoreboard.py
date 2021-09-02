from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))

    #Add points to left player
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    #Add points to right player
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
