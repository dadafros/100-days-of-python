from turtle import Turtle

MOVE_STEP = 50
UP = 90
DOWN = 270
PAD_STRETCH = 5


class Paddle(Turtle):
    def __init__(self, position_x, screen_limit_y):
        super().__init__()
        self.screen_limit_y = screen_limit_y
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=PAD_STRETCH, stretch_wid=0.2)
        self.setheading(UP)
        self.goto(position_x, 0)
        self.speed("fastest")

    def up(self):
        if self.ycor() < self.screen_limit_y - PAD_STRETCH * 10:
            self.setheading(UP)
            self.forward(MOVE_STEP)

    def down(self):
        if self.ycor() > -self.screen_limit_y:
            self.setheading(DOWN)
            self.forward(MOVE_STEP)
