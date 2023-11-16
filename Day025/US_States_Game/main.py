import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
correct_states = []
states = states_data["state"].to_list()
while len(correct_states) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in states:
        states.remove(answer_state)
        state_info = states_data[states_data["state"] == answer_state]
        correct_states.append(state_info.state.item())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_coor = int(state_info.x.item())
        y_coor = int(state_info.y.item())
        t.goto(x_coor, y_coor)
        t.write(state_info.state.item())

    if answer_state == "Exit":
        states_to_learn = {
            "states": states
        }
        pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break
