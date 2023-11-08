from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 265)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(
            align=ALIGNMENT,
            arg=f"Score: {self.score}",
            font=FONT
            )

    def update_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg="GAME OVER",
            align=ALIGNMENT,
            font=FONT
        )
