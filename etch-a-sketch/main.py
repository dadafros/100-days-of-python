import random
from turtle import Turtle, Screen

OFFSET = 20
screen = Screen()
screen.setup(width=500, height=400)
info_turtle = Turtle()
info_turtle.hideturtle()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "blue", "green", "yellow", "violet", "indigo", "orange"]
num_turtles = len(colors)
turtles = []
for index in range(num_turtles):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(OFFSET - screen.window_width() / 2,
                    ((index + 1) * (screen.window_height() - OFFSET) / num_turtles)
                    - (screen.window_height() - OFFSET) / 2)
    turtles.append(new_turtle)

run = True
while run:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > screen.window_width() / 2 - OFFSET:
            run = False
            if user_bet.lower() == turtle.pencolor():
                info_turtle.write("Your turtle won!", font=("Arial", 10, "bold"))
            else:
                info_turtle.write(f"The {turtle.pencolor()} turtle is the winner.", font=("Arial", 10, "bold"))

screen.listen()
screen.exitonclick()
