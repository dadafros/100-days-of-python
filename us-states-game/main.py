from turtle import Turtle, Screen
from PIL import Image
import pandas as pd

width, height = Image.open("blank_states_img.gif").size
screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(width, height)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

correct_states = 0
while correct_states < 50:
    state = screen.textinput(f"{correct_states}/50 States Correct", "What's another state name?").title()
    if state in states:
        correct_states += 1
        states.remove(state)
        state_turtle = Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        row = data[data.state == state]
        state_turtle.goto(int(row.x), int(row.y))
        state_turtle.write(state)

screen.exitonclick()
