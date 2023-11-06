import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [80, 50, 20, -20, -50, -80]
all_turtles = []

# Create 6 turtles
for turtle_idx in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_idx])
    new_turtle.goto(x=-230, y=y_positions[turtle_idx])
    all_turtles.append(new_turtle)

while bool(user_bet):
    for turtle_idx in range(6):
        if all_turtles[turtle_idx].xcor() <= 230:
            all_turtles[turtle_idx].forward(random.randint(1, 10))
        else:
            winner = all_turtles[turtle_idx].color()
            if winner == user_bet.lower():
                print("You've won!")
            else:
                print("You've lost")
            print(f"The winner turtle is: {winner[0]}")
            turtle_idx = 5
            user_bet = False

screen.exitonclick()
