from turtle import Turtle

MAX_Y = 190

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() > MAX_Y:
            pass
        else:
            new_y = self.ycor() + 25
            self.goto(self.xcor(),new_y )

    def move_down(self):
        if self.ycor() <= -MAX_Y:
            pass
        else:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)