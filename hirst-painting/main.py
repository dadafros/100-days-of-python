###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)
screen = Screen()
screen.tracer(0, 0)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

for line in range(10):
    t.penup()
    t.hideturtle()
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    t.setpos(0, 50 * (line + 1))

screen.exitonclick()
