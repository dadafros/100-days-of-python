import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.speed = MOVE_INCREMENT

    def new_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.goto(280, random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

