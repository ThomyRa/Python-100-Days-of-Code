from turtle import Turtle, Screen
import random

def drawing_square(timmy):
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)

########### Challenge 2 - Draw a Dashed Line ########
def dashed_line(timmy):
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def random_rgb():
    random_color = []
    for _ in range(3):
        random_color.append(random.randint(0, 255))
    return tuple(random_color)


########### Challenge 3 - Draw a different shapes ########
def drawing_shapes(timmy):
    num_sides = 3
    while num_sides <= 10:
        timmy.color(random_rgb())
        for _ in range(num_sides):
            timmy.fd(50)
            timmy.rt(360 // num_sides)
        num_sides += 1


def random_walk(timmy):
    timmy.width(5)
    steps = 0
    timmy.speed("fast")
    while steps < 100:
        timmy.color(random_rgb())
        angle = [0, 90, 180, 270]
        direction = random.choice(angle)
        timmy.setheading(direction)
        timmy.fd(20)
        steps += 1


def spirograph(timmy):
    degrees = 5
    timmy.speed("fastest")
    timmy.width(2)
    for _ in range(360 // degrees):
        timmy.color(random_rgb())
        timmy.circle(100)
        timmy.lt(degrees)


timmy = Turtle()
timmy.shape("turtle")

screen = Screen()
screen.colormode(255)

spirograph(timmy)
# random_walk(timmy)
# drawing_shapes(timmy)
# drawing_square(timmy)
# dashed_line(timmy)


screen.exitonclick()
