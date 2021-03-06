from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        #Keeps paddle on screen
        if new_y < 270:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        #Keeps paddle on screen
        if new_y > -270:
            self.goto(self.xcor(), new_y)
