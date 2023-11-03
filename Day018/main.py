from turtle import Turtle, Screen
import random


############################################################
# Drawing square
def drawing_square(turtle_obj):
    for _ in range(4):
        turtle_obj.forward(100)
        turtle_obj.right(90)


############################################################
# Dash Line
def dash_line(turtle_obj):
    for _ in range(10):
        turtle_obj.pendown()
        turtle_obj.forward(10)
        turtle_obj.penup()
        turtle_obj.forward(10)


############################################################
# Drawing different shapes
def drawing_shape(turtle_obj, num_of_sides, size):
    degree = 360 / num_of_sides
    for _ in range(num_of_sides):
        turtle_obj.forward(size)
        turtle_obj.right(degree)


def random_color():
    color = []
    for _ in range(3):
        layer = random.randint(0, 255)
        color.append(layer)
    return tuple(color)


def drawing_different_shapes(turtle_obj, size):
    for _ in range(3, 11):
        turtle_obj.color(random_color())
        drawing_shape(turtle_obj, _, size)


############################################################
# Random Walk
def random_walk(turtle_obj):
    direction = [90, 180, 270, 360]
    for _ in range(250):
        turtle_obj.pensize(5)
        turtle_obj.color(random_color())
        turtle_obj.setheading(random.choice(direction))
        turtle_obj.forward(20)


############################################################
# Spirograph
def spirograph(turtle_obj, gap_size):
    num_circles = 360 // gap_size
    degrees = 0
    for _ in range(num_circles):
        turtle_obj.setheading(degrees)
        turtle_obj.color(random_color())
        turtle_obj.circle(100)
        degrees += 5


timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

screen = Screen()
screen.colormode(255)

# drawing_square(timmy)
# dash_line(timmy)
# drawing_different_shapes(timmy, 50)
# random_walk(timmy)
spirograph(timmy, 5)

screen.exitonclick()
