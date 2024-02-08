import colorgram
import turtle as t
from color import color_list
import random

colors = color_list

t.colormode(255)
nav = t.Turtle()
screen = t.Screen()
x = -350
y = -350
nav.penup()
nav.setx(x)
nav.sety(y)
nav.pendown()
nav.hideturtle()


for _ in range(10):
    for _ in range(10):
        nav.dot(20, random.choice(colors))
        nav.penup()
        nav.forward(50)
    nav.setx(x)
    y += 50
    nav.sety(y)
    nav.pendown()

screen.exitonclick()
