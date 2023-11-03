from turtle import Turtle, Screen
import colorgram
import random


def random_rgb_color(colorg_colors):
    while True:
        color_rgb = random.choice(colorg_colors).rgb
        if color_rgb.r and color_rgb.b and color_rgb.g > 230:
            continue
        color = (color_rgb.r, color_rgb.g, color_rgb.b)
        return color


colors = colorgram.extract("./Day018/hirst_paint/image.jpeg", 30)


timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.penup()
timmy.setpos(-300, -200)
timmy.speed("fastest")

count = 0
y_pos = -200
while count < 10:
    timmy.setpos(-300, y_pos)
    for _ in range(10):
        timmy.color(random_rgb_color(colors))
        timmy.dot(20)
        timmy.penup()
        timmy.fd(50)
    count += 1
    y_pos += 50

screen.exitonclick()
