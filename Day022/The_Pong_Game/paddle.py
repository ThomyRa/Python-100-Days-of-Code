from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, initial_cords):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(initial_cords)

    def move_up(self):
        y_pos = self.ycor()
        self.goto(self.xcor(), y_pos + 20)

    def move_down(self):
        y_pos = self.ycor()
        self.goto(self.xcor(), y_pos - 20)
