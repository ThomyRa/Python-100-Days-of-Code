from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR
        )

        self.lbl_score = Label(
            text="Score: 0",
            font=("Arial", 10),
            bg=THEME_COLOR,
            fg="white"
        )
        self.lbl_score.grid(row=0, column=1)

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.question = self.canvas.create_text(
            150,
            125,
            text="Question goes here...",
            font=("arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = PhotoImage(file="./images/true.png")
        self.btn_true = Button(image=img_true, highlightthickness=0)
        self.grid(row=2, column=1)

        img_false = PhotoImage(file="./images/false.png")
        self.btn_false = Button(image=img_false, highlightthickness=0)
        self.btn_false.grid(row=2, column=0)

        self.window.mainloop()

