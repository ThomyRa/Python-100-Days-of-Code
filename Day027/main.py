from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label",
                 font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")

###################################################
# Button
def button_clicked():
    text = my_input.get()
    my_label.config(text=text)


my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()

# Entry
my_input = Entry(width=10)
my_input.pack()


window.mainloop()
