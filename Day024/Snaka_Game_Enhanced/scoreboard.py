from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {get_high_score()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_high_score(self):
        with open("data.txt", "w") as data:
            data.write(str(self.score))


def get_high_score():
    with open("data.txt") as data:
        highscore = data.read()
    return int(highscore)

