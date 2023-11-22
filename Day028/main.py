from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
TOMATO_RED = "#f26849"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "☑"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_title.config(text="Timer")
    lbl_repetitions.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        lbl_title.config(text="Work", bg=YELLOW, fg=TOMATO_RED)
        count_down(work_sec)
    elif reps % 8 == 0:
        lbl_repetitions.config(text="{lbl_repetitions.cget('text')}{CHECK}")
        lbl_title.config(text="Break", bg=YELLOW, fg=GREEN)
        count_down(long_break_sec)
        lbl_repetitions.config(text="")
    else:
        lbl_repetitions.config(text=f"{lbl_repetitions.cget('text')}{CHECK}")
        lbl_title.config(text="Break", bg=YELLOW, fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = count // 60
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label Timer
lbl_title = Label(text="Timer",
                  font=(FONT_NAME, 40, "bold"))
lbl_title.config(bg=YELLOW, fg=GREEN)
lbl_title.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200,
                height=224,
                bg=YELLOW,
                highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130,
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Button Start
btn_start = Button(text="Start",
                   command=start_timer,
                   highlightthickness=0)
btn_start.grid(row=2, column=0)

# Button Reset
btn_reset = Button(text="Reset",
                   command=reset_timer,
                   highlightthickness=0)
btn_reset.grid(row=2, column=2)

# Label Checks
lbl_repetitions = Label(font=(FONT_NAME, 40))
lbl_repetitions.config(bg=YELLOW,
                       fg=GREEN)
lbl_repetitions.grid(row=3, column=1)

window.mainloop()
