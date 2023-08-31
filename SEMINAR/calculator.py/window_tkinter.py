import tkinter as tk


def add_digit(digit):
    val = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, val)


def make_operation():
    val = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, val)

    
def make_digit_button(digit):
    return tk.Button(
        text=digit, bd=5, font=("Arial", 22), command=lambda: add_digit(digit)
    )


def make_operation_button(operation):
    return tk.Button(
        text=operation,
        bd=5,
        font=("Arial", 22),
        fg="red",
        command=lambda: add_digit(operation),
    )


def make_calc_button(operation):
    return tk.Button(
        text=operation,
        bd=5,
        font=("Arial", 22),
        fg="red",
        command=lambda: make_operation(),
    )


win = tk.Tk()
win.title("Calculator")
win.geometry(f"273x420+600+50")
win["bg"] = "#33ffe6"


calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 22), width=16)
calc.grid(column=0, row=1, columnspan=4, padx= 5,pady= 5, sticky="we")

make_digit_button("1").grid(column=0, row=2, sticky="wesn", padx=5, pady=5)
make_digit_button("2").grid(column=1, row=2, sticky="wesn", padx=5, pady=5)
make_digit_button("3").grid(column=2, row=2, sticky="wesn", padx=5, pady=5)
make_digit_button("4").grid(column=0, row=3, sticky="wesn", padx=5, pady=5)
make_digit_button("5").grid(column=1, row=3, sticky="wesn", padx=5, pady=5)
make_digit_button("6").grid(column=2, row=3, sticky="wesn", padx=5, pady=5)
make_digit_button("7").grid(column=0, row=4, sticky="wesn", padx=5, pady=5)
make_digit_button("8").grid(column=1, row=4, sticky="wesn", padx=5, pady=5)
make_digit_button("9").grid(column=2, row=4, sticky="wesn", padx=5, pady=5)
make_digit_button("0").grid(column=0, row=5, sticky="wesn", padx=5, pady=5)
make_digit_button("00").grid(column=1, row=5, sticky="wesn", padx=5, pady=5)
make_digit_button(",").grid(column=2, row=5, sticky="wesn", padx=5, pady=5)

make_operation_button("*").grid(column=3, row=2, sticky="wesn", padx=5, pady=5)
make_operation_button("/").grid(column=3, row=3, sticky="wesn", padx=5, pady=5)
make_operation_button("-").grid(column=3, row=4, sticky="wesn", padx=5, pady=5)
make_operation_button("+").grid(column=3, row=5,rowspan=2, sticky="wesn", padx=5, pady=5)

make_calc_button("=").grid(column=0, row=6,columnspan=3, sticky="wesn", padx=5, pady=5)

win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=50)
win.grid_columnconfigure(2, minsize=50)
win.grid_columnconfigure(3, minsize=50)

win.grid_rowconfigure(2, minsize=50)
win.grid_rowconfigure(3, minsize=50)
win.grid_rowconfigure(4, minsize=50)
win.grid_rowconfigure(5, minsize=50)
win.grid_rowconfigure(6, minsize=50)

win.mainloop()


#                               Вид чернового варианта калькулятор
# import tkinter as tk

# win = tk.Tk()
# win.title("Calculator")
# win.geometry(f"350x500+100+200")
# win['bg'] = '#33ffe6'

# def add_digit(digit):
#     val = calc.get() + str(digit)
#     calc.delete(0, tk.END)
#     calc.insert(0, val)

# calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 22), width=18)
# calc.grid(column= 0, row= 0, columnspan= 3, sticky='we')

# tk.Button(text= '1', bd=5, font=('Arial', 22), command=lambda: add_digit(1)).grid(column=0, row=1, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '2', bd=5, font=('Arial', 22), command=lambda: add_digit(2)).grid(column=1, row=1, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '3', bd=5, font=('Arial', 22), command=lambda: add_digit(3)).grid(column=2, row=1, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '4', bd=5, font=('Arial', 22), command=lambda: add_digit(4)).grid(column=0, row=2, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '5', bd=5, font=('Arial', 22), command=lambda: add_digit(5)).grid(column=1, row=2, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '6', bd=5, font=('Arial', 22), command=lambda: add_digit(6)).grid(column=2, row=2, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '7', bd=5, font=('Arial', 22), command=lambda: add_digit(7)).grid(column=0, row=3, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '8', bd=5, font=('Arial', 22), command=lambda: add_digit(8)).grid(column=1, row=3, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '9', bd=5, font=('Arial', 22), command=lambda: add_digit(9)).grid(column=2, row=3, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '0', bd=5, font=('Arial', 22), command=lambda: add_digit(0)).grid(column=0, row=4, sticky='wesn', padx=5, pady=5)
# tk.Button(text= '00', bd=5, font=('Arial', 22), command=lambda: add_digit('00')).grid(column=1, row=4, sticky='wesn', padx=5, pady=5)
# tk.Button(text= ',', bd=5, command=lambda: add_digit(',')).grid(column=2, row=4, sticky='wesn', padx=5, pady=5)

# win.grid_columnconfigure(0, minsize= 60)
# win.grid_columnconfigure(1, minsize= 60)
# win.grid_columnconfigure(2, minsize= 60)

# win.grid_rowconfigure(1, minsize= 60)
# win.grid_rowconfigure(2, minsize= 60)
# win.grid_rowconfigure(3, minsize= 60)
# win.grid_rowconfigure(4, minsize= 60)
# win.mainloop()
