from tkinter import *


def button_clicked():
    text = my_input.get()
    label.config(text=text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
label = Label(text="I'm a label",
              font=("Arial", 24, "bold"))
label.config(text="New Text")
label.grid(row=0, column=0)

button1 = Button(text="Button 1", command=button_clicked)
button1.grid(row=1, column=1)

button2 = Button(text="Button 2", command=button_clicked)
button2.grid(row=0, column=2)

# Entry
my_input = Entry(width=10)
my_input.grid(row=2, column=3)


window.mainloop()
