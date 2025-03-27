from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scores import ScoreBoard
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddles = Paddle((350,0))
l_paddles = Paddle((-350,0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(key="w", fun=r_paddles.goup)
screen.onkey(key="s", fun=r_paddles.godown)
screen.onkey(key="Up", fun=l_paddles.goup)
screen.onkey(key="Down", fun=l_paddles.godown)




game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddles) < 50 and ball.xcor() > 320 or ball.distance(l_paddles) < 50 and ball.xcor() < -320:
        ball.bounce_X()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()