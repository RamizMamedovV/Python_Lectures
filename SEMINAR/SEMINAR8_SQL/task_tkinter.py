from tkinter import *



def clicked():
    lbl.configure(text= 'clicked')


# Создайте новое окно и назначьте его переменной window :
window = Tk()


#                           title of window
window.title("Hello")
window.geometry('350x200')


#                       created a simple label

lbl = Label(window, text= "Hello Ra", font=("Arial Bold", 10))
lbl.grid(column= 0, row= 0)



# txt = Entry(window,width=10, state='disabled') # эта запись исключит возможность записи в этом окне!!
txt = Entry(window, width= 10)
txt.grid(column= 1, row= 0)
txt.focus()


#                создаём кнопку clickable
def clicked():
#    lbl.configure(text= 'clicked') # при вызове этой функции на lbl отобразит 'clicked'

    res = "Welcome " + txt.get() # с помощью txt.get() добавится к записи "Welcome" то, что полбзоватеь наберёт в окошке "txt = Entry"
    lbl.configure(text= res)

#   здесь задаем цвет и ссылку на функцию которая отобразит обработку команды 'command'
btn = Button(window, text = 'click', bg = 'red', fg = 'black', command= clicked)

btn.grid(column= 2, row= 0)

"""                         # записи из другого источника
# greeting = Label(text="Hello, Tkinter")
# greeting.pack()

# Добавьте главный цикл событий для отображения окна:
"""
window.mainloop()