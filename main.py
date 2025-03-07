from turtle import Turtle, Screen, colormode
from random import choice
import colorgram

colormode(255)
colors = colorgram.extract("hirsty.jpeg", 30)
formatted_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    formatted_colors.append((r, b, g))

jack = Turtle()
jack.speed("fastest")
jack.hideturtle()
jack.penup()
jack.setpos(-275, -275)

def draw_dot():
    jack.pendown()
    jack.dot(30, choice(formatted_colors))
    jack.penup()
    jack.forward(60)

def move_back():
    jack.left(90)
    jack.forward(60)
    jack.left(90)
    jack.forward(600)
    jack.left(180)

for _ in range(1, 101):
    draw_dot()
    if _ % 10 == 0:
        move_back()


screen = Screen()
screen.exitonclick()