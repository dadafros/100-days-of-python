from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen_limit_x, screen_limit_y):
        super().__init__()
        self.screen_limit_x = screen_limit_x
        self.screen_limit_y = screen_limit_y
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-self.screen_limit_x, self.screen_limit_x),
                  random.randint(-self.screen_limit_y, self.screen_limit_y))
