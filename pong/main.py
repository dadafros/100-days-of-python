from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

PAD_OFFSET = 10
SCREEN_OFFSET = 20
COLLISION_OFFSET = 50
SCREEN_LIMIT_X = screen.window_width() / 2
SCREEN_LIMIT_Y = screen.window_height() / 2

ball = Ball()
scoreboard = Scoreboard(SCREEN_LIMIT_Y - SCREEN_OFFSET)
paddle1 = Paddle(-SCREEN_LIMIT_X + PAD_OFFSET, SCREEN_LIMIT_Y - SCREEN_OFFSET)
paddle2 = Paddle(SCREEN_LIMIT_X - PAD_OFFSET, SCREEN_LIMIT_Y - SCREEN_OFFSET)

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ball.setheading(random.randint(30, 60))
run = True
while run:
    screen.update()
    ball.move()
    sleep(0.005)
    if ball.xcor() < -SCREEN_LIMIT_X:
        scoreboard.mark_point_2()
        ball.home()
        ball.setheading(random.randint(30, 60))
        ball.step(reset=True)
    elif ball.xcor() > SCREEN_LIMIT_X:
        scoreboard.mark_point_1()
        ball.home()
        ball.setheading(random.randint(120, 150))
        ball.step(reset=True)
    elif ball.ycor() > SCREEN_LIMIT_Y or ball.ycor() < -SCREEN_LIMIT_Y:
        ball.wall_collision()
    if ball.distance(paddle1) < COLLISION_OFFSET and ball.xcor() < -SCREEN_LIMIT_X + SCREEN_OFFSET + PAD_OFFSET \
            or ball.distance(paddle2) < COLLISION_OFFSET and ball.xcor() > SCREEN_LIMIT_X - SCREEN_OFFSET - PAD_OFFSET:
        ball.pad_collision()
        ball.step(increase=0.1)

screen.exitonclick()
