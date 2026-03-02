from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")
l_pad=Paddle((-350,0))
r_pad=Paddle((350,0))

game_over = False
while not game_over:
    screen.update()

    screen.onkey(l_pad.pad_up, "Up")
    screen.onkey(l_pad.pad_down, "Down")
    screen.onkey(r_pad.pad_up, "w")
    screen.onkey(r_pad.pad_down, "s")




screen.exitonclick()