from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

MAX_X = 600
MAX_Y = 800

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")

l_pad = Paddle((-350,0))
r_pad = Paddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(l_pad.pad_up, "w")
screen.onkey(l_pad.pad_down, "s")
screen.onkey(r_pad.pad_up, "Up")
screen.onkey(r_pad.pad_down, "Down")

game_over = False
while not game_over:
    time.sleep(.1)
    screen.update()
    ball.move()

    if ball.ycor() > 220 or ball.ycor() < -220:
        ball.y_bounce()

    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.x_bounce()

screen.exitonclick()