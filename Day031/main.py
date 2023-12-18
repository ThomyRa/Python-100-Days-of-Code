from tkinter import *
import pandas as pd
import random

data = pd.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,
                height=526,
                highlightthickness=0,
                bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150,
                                text="",
                                font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263,
                               text="",
                               font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

img_right = PhotoImage(file="./images/right.png")
btn_right = Button(image=img_right, highlightthickness=0, command=next_card)
btn_right.grid(row=1, column=1)

img_wrong = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card)
btn_wrong.grid(row=1, column=0)

next_card()

window.mainloop()
