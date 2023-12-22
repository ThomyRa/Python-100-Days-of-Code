from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
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
            width=280,
            text="Question goes here...",
            font=("arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = PhotoImage(file="./images/true.png")
        self.btn_true = Button(image=img_true, highlightthickness=0)
        self.btn_true.grid(row=2, column=1)

        img_false = PhotoImage(file="./images/false.png")
        self.btn_false = Button(image=img_false, highlightthickness=0)
        self.btn_false.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)


