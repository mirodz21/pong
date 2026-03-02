from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

MAX_Y = 230

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-390, 0))
r_paddle = Paddle((380, 0))

l_score = Scoreboard((-100,190))
r_score = Scoreboard((100,190))

ball = Ball()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # BOUNCE IF COLLISION WITH MAX Y AND MAX -Y
    if ball.ycor() > MAX_Y or ball.ycor() < -MAX_Y:
        ball.bounce_y()

    # BOUNCE IF COLLISION WITH PADDLE
    if (ball.distance(r_paddle) < 30 and ball.xcor() > 330 or
    ball.distance(l_paddle) < 30 and ball.xcor() < -330):
        ball.bounce_x()

    # SCORE AND RESET IF BALL GOES OUT OF BOUND
    if ball.xcor() > 380:
        l_score.add_score()
        ball.ball_reset()
    if ball.xcor() < -380:
        ball.ball_reset()
        r_score.add_score()

screen.exitonclick()