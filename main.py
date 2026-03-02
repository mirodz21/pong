from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

MAX_Y = 230

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-390, 0))
r_paddle = Paddle((380, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


game_over = False
while not game_over:
    time.sleep(.1)
    screen.update()
    ball.move()

    # BOUNCE IF COLLISION WITH MAX Y AND MAX -Y
    if ball.ycor() > MAX_Y or ball.ycor() < -MAX_Y:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 30 and ball.xcor() > 330 or
    ball.distance(l_paddle) < 30 and ball.xcor() < -330):
        ball.bounce_x()

screen.exitonclick()