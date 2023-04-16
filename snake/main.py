from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
from turtle import Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

SCREEN_OFFSET = 20
FOOD_OFFSET = 15
TEXT_OFFSET = 15
TAIL_OFFSET = 15
SCREEN_LIMIT_X = screen.window_width() / 2 - SCREEN_OFFSET
SCREEN_LIMIT_Y = screen.window_height() / 2 - SCREEN_OFFSET

snake = Snake()
food = Food(SCREEN_LIMIT_X, SCREEN_LIMIT_Y)
score = Scoreboard(0, SCREEN_LIMIT_Y - TEXT_OFFSET)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

run = True
while run:
    screen.update()
    sleep(0.1)
    snake.move()

    if snake.head.xcor() > SCREEN_LIMIT_X or snake.head.xcor() < -SCREEN_LIMIT_X or \
            snake.head.ycor() > SCREEN_LIMIT_Y or snake.head.ycor() < -SCREEN_LIMIT_Y:
        score.game_over()
        run = False

    if snake.head.distance(food) <= FOOD_OFFSET:
        snake.create_segment()
        food.refresh()
        score.update()

    for segment in snake.segments:
        if snake.head.distance(segment) <= TAIL_OFFSET:
            if segment != snake.head:
                score.game_over()
                run = False

screen.exitonclick()
