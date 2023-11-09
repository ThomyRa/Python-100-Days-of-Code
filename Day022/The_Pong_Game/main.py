
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

paddle1 = Paddle()

screen.listen()
screen.onkey(fun=paddle1.move_up, key="Up")
screen.onkey(fun=paddle1.move_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
