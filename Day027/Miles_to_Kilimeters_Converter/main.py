from tkinter import *


def convert_miles_to_kms():
    miles = float(txt_miles.get())
    kms = 1.6093 * miles
    lbl_result.config(text=round(kms, 3))


window = Tk()
window.title("Convert Miles to Kilometers")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)

# Input
txt_miles = Entry(width=10)
window.config(pady=10)
txt_miles.grid(row=0, column=1)

# Label Miles
lbl_miles = Label(text="Miles",
                  font=("Arial", 14,))
lbl_miles.config(padx=10, pady=10)
lbl_miles.grid(row=0, column=2)

# Label is equal
lbl_is_equal = Label(text="is equal to",
                     font=("Arial", 14,))
lbl_miles.config(pady=10)
lbl_is_equal.grid(row=1, column=0)


# Label Result
lbl_result = Label(text="",
                   font=("Arial", 14,))
lbl_miles.config(pady=10)
lbl_result.grid(row=1, column=1)

# Label Kms
lvl_kms = Label(text="Kms",
                font=("Arial", 14,))
lvl_kms.config(padx=10, pady=10)
lvl_kms.grid(row=1, column=2)

# Button Calculate
btn_calculate = Button(text="Calculate", command=convert_miles_to_kms)
lbl_miles.config(pady=10)
btn_calculate.grid(row=2, column=1)


window.mainloop()
