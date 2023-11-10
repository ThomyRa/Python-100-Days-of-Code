from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            arg=f"Level {self.lvl}",
            align="center",
            font=FONT
        )

    def level_up(self):
        self.lvl += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg="GAME OVER",
            align="center",
            font=FONT
        )
