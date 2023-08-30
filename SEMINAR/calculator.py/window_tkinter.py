import tkinter as tk

win = tk.Tk()
win.title("Calculator")
win.geometry(f"350x500+100+200")
win['bg'] = '#33ffe6'

def add_digit(digit):
    val = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, val)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 22), width=18)
calc.grid(column= 0, row= 0, columnspan= 3, sticky='we')

tk.Button(text= '1', bd=5, font=('Arial', 22), command=lambda: add_digit(1)).grid(column=0, row=1, sticky='wesn', padx=5, pady=5)
tk.Button(text= '2', bd=5, font=('Arial', 22), command=lambda: add_digit(2)).grid(column=1, row=1, sticky='wesn', padx=5, pady=5)
tk.Button(text= '3', bd=5, font=('Arial', 22), command=lambda: add_digit(3)).grid(column=2, row=1, sticky='wesn', padx=5, pady=5)
tk.Button(text= '4', bd=5, font=('Arial', 22), command=lambda: add_digit(4)).grid(column=0, row=2, sticky='wesn', padx=5, pady=5)
tk.Button(text= '5', bd=5, font=('Arial', 22), command=lambda: add_digit(5)).grid(column=1, row=2, sticky='wesn', padx=5, pady=5)
tk.Button(text= '6', bd=5, font=('Arial', 22), command=lambda: add_digit(6)).grid(column=2, row=2, sticky='wesn', padx=5, pady=5)
tk.Button(text= '7', bd=5, font=('Arial', 22), command=lambda: add_digit(7)).grid(column=0, row=3, sticky='wesn', padx=5, pady=5)
tk.Button(text= '8', bd=5, font=('Arial', 22), command=lambda: add_digit(8)).grid(column=1, row=3, sticky='wesn', padx=5, pady=5)
tk.Button(text= '9', bd=5, font=('Arial', 22), command=lambda: add_digit(9)).grid(column=2, row=3, sticky='wesn', padx=5, pady=5)
tk.Button(text= '0', bd=5, font=('Arial', 22), command=lambda: add_digit(0)).grid(column=0, row=4, sticky='wesn', padx=5, pady=5)
tk.Button(text= '00', bd=5, font=('Arial', 22), command=lambda: add_digit('00')).grid(column=1, row=4, sticky='wesn', padx=5, pady=5)
tk.Button(text= ',', bd=5, command=lambda: add_digit(',')).grid(column=2, row=4, sticky='wesn', padx=5, pady=5)

win.grid_columnconfigure(0, minsize= 60)
win.grid_columnconfigure(1, minsize= 60)
win.grid_columnconfigure(2, minsize= 60)

win.grid_rowconfigure(1, minsize= 60)
win.grid_rowconfigure(2, minsize= 60)
win.grid_rowconfigure(3, minsize= 60)
win.grid_rowconfigure(4, minsize= 60)
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
