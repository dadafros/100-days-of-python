import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

FINISH_LINE_Y = 280
COLLISION_OFFSET = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.005)
    screen.update()

    if player.ycor() >= FINISH_LINE_Y:
        car_manager.increase_speed()
        player.reset_position()
        scoreboard.level_up()

    if random.randint(1, 60) == 1:
        car_manager.new_car()

    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < COLLISION_OFFSET:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
