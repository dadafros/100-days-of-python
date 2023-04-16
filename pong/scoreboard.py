from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 40
FONT = ("Courier", FONT_SIZE, "bold")


class Scoreboard(Turtle):
    def __init__(self, screen_limit_y):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, screen_limit_y - FONT_SIZE)
        self.update()

    def mark_point_1(self):
        self.score1 += 1
        self.update()

    def mark_point_2(self):
        self.score2 += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score1} {self.score2}", align=ALIGNMENT, font=FONT)
