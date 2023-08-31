from tkinter import *


def add_digit(digit):
    val = calc.get()
    if val[0] == '0':
        val = val[1:]
    calc.delete(0, END)
    calc.insert(0, val + digit)


def add_operand(operand):
    val = calc.get()
    if val[-1] in '+-/*':
        val = val[:-1]
    calc.delete(0, END)
    calc.insert(0, val + operand)


def make_digit_button(digit):
    return Button(
        text=digit, bd=5, font=("Arial", 15), command=lambda: add_digit(digit)
    )


def make_operand_button(operand):
    return Button(
        text=operand, bd=5, font=("Arial", 15), fg="red", command=lambda: add_operand(operand)
    )


def make_calc_button(operand):
    return Button(
        text=operand, bd=5, font=("Arial", 15), fg="red", command=lambda: make_calc(operand)
    )


win = Tk()
win.title("Calc")
win.geometry("280x500+600+80")

calc = Entry(win, justify=RIGHT, font=("Arial", 25), width=15)
calc.insert(0, '0')
calc.grid(column=0, row=0, columnspan=4, sticky="we", pady=5)

make_digit_button("7").grid(column=0, row=2, sticky="wesn", padx=3, pady=3)
make_digit_button("8").grid(column=1, row=2, sticky="wesn", padx=3, pady=3)
make_digit_button("9").grid(column=2, row=2, sticky="wesn", padx=3, pady=3)
make_digit_button("4").grid(column=0, row=3, sticky="wesn", padx=3, pady=3)
make_digit_button("5").grid(column=1, row=3, sticky="wesn", padx=3, pady=3)
make_digit_button("6").grid(column=2, row=3, sticky="wesn", padx=3, pady=3)
make_digit_button("1").grid(column=0, row=4, sticky="wesn", padx=3, pady=3)
make_digit_button("2").grid(column=1, row=4, sticky="wesn", padx=3, pady=3)
make_digit_button("3").grid(column=2, row=4, sticky="wesn", padx=3, pady=3)
make_digit_button("0").grid(column=0, row=5, sticky="wesn", padx=3, pady=3)
make_digit_button("00").grid(column=1, row=5, sticky="wesn", padx=3, pady=3)

make_operand_button("*").grid(column=3, row=1, sticky="wesn", padx=3, pady=3)
make_operand_button("/").grid(column=3, row=2, sticky="wesn", padx=3, pady=3)
make_operand_button("-").grid(column=3, row=3, sticky="wesn", padx=3, pady=3)
make_operand_button("+").grid(column=3, row=4, sticky="wesn", padx=3, pady=3)

make_calc_button("=").grid(column=3, row=5, sticky="wesn", padx=3, pady=3)

make_operand_button(".").grid(column=2, row=5, sticky="wesn", padx=3, pady=3)

win.columnconfigure(0, minsize=60)
win.columnconfigure(1, minsize=60)
win.columnconfigure(2, minsize=60)
win.columnconfigure(3, minsize=60)

win.rowconfigure(1, minsize=60)
win.rowconfigure(2, minsize=60)
win.rowconfigure(3, minsize=60)
win.rowconfigure(4, minsize=60)
win.rowconfigure(5, minsize=60)

win.mainloop()


# import tkinter as tk

# def add_to_display(value):
#     display.insert(tk.END, value)

# win = tk.Tk()
# win.geometry('300x400')
# win.title('Calculator')

# display = tk.Text(win, wrap=tk.NONE, height=2)
# display.grid(column=0, row=0, padx=10, pady=10)

# button_frame = tk.Frame(win)
# button_frame.grid(column=0, row=1)

# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]

# row_val = 1
# col_val = 0

# for button in buttons:
#     tk.Button(button_frame, text=button, padx=20, pady=20, command=lambda b=button: add_to_display(b)).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# win.mainloop()
