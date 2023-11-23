from tkinter import *

WIDTH = 40
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200,
                height=200,
                bg="white",
                highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Label Website
lbl_website = Label(text="Website",
                    font=("Arial", 10),
                    bg="white")
lbl_website.config(padx=10, pady=5)
lbl_website.grid(row=1, column=0)

# Input Website
txt_website = Entry(width=WIDTH)
txt_website.grid(row=1, column=1, columnspan=2)

# Label Email
lbl_email = Label(text="Email/Username",
                  font=("Arial", 10),
                  bg="white")
lbl_email.config(padx=10, pady=5)
lbl_email.grid(row=2, column=0)

# Input Email
txt_email = Entry(width=WIDTH)
txt_email.grid(row=2, column=1, columnspan=2)

# Label Password
lbl_password = Label(text="Password",
                     font=("Arial", 10),
                     bg="white")
lbl_password.config(padx=10, pady=10)
lbl_password.grid(row=3, column=0)

# Input Password
txt_password = Entry(width=24)
txt_password.grid(row=3, column=1)

# Button Generate Password
btn_generate_password = Button(text="Generate Password",
                               width=14,
                               font=("Arial", 10))
btn_generate_password.grid(row=3, column=2)

# Button Add
btn_add = Button(text="Add",
                 width=44,
                 font=("Arial", 10))
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
