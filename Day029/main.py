from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

WIDTH = 40
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    txt_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_user_data():
    website = txt_website.get()
    email = txt_email.get()
    password = txt_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it ok save?")

        if is_ok:
            user_info = f"{website}, {email}, {password}\n"
            with open("./data.txt", "a") as data:
                data.write(user_info)
                txt_website.delete(0, "end")
                txt_password.delete(0, "end")


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
txt_website.focus()
txt_website.grid(row=1, column=1, columnspan=2)

# Label Email
lbl_email = Label(text="Email/Username",
                  font=("Arial", 10),
                  bg="white")
lbl_email.config(padx=10, pady=5)
lbl_email.grid(row=2, column=0)

# Input Email
txt_email = Entry(width=WIDTH)
txt_email.insert(0, "my_email@email.com")
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
                               font=("Arial", 10),
                               command=generate_password)
btn_generate_password.grid(row=3, column=2)

# Button Add
btn_add = Button(text="Add",
                 width=44,
                 font=("Arial", 10),
                 command=save_user_data)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
