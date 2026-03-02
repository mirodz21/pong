from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", False, "center", ("Courier", 30, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def display_game_over(self):
        self.goto(0,0)
        self.color("RED")
        self.write("Game Over",False, "center", ("Courier",8,"normal"))


