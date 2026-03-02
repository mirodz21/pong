from turtle import Turtle

PADDLE_POSITION = [(-350, 0), (350, 0)]

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)


    def pad_up(self):
        go_up = self.ycor() + 20
        self.goto(self.xcor(), go_up)

    def pad_down(self):
        go_down =self.ycor() - 20
        self.goto(self.xcor(), go_down)
