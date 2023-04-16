from turtle import Turtle

BALL_STEP = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ball_step = BALL_STEP

    def move(self):
        self.forward(self.ball_step)

    def wall_collision(self):
        self.setheading(-self.heading())

    def pad_collision(self):
        self.setheading(self.heading() - 90)

    def step(self, reset=False, increase=0):
        if reset:
            self.ball_step = BALL_STEP
        self.ball_step += increase
