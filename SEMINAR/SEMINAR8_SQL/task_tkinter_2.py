"""
5 Добавьте виджет со списком
6 Добавьте виджет Checkbutton (флажок Tkinter)
6.1 Установка состояния проверки кнопки Check
7. Добавьте виджеты переключателей
7.1 Получить значение переключателя (выбранный переключатель)
8. Добавьте виджет ScrolledText (текстовое поле Tkinter)
8.1 Настройка содержимого прокручиваемого текста
8.2 Удаление/очистка содержимого прокручиваемого текста
9. Создайте окно сообщения
9.1 Отображение предупреждений и сообщений об ошибках
9.2 Отображение диалоговых окон с вопросами
10. Добавьте SpinBox (виджет чисел)
10.1 Установите значение по умолчанию для Spinbox
"""

from tkinter import *

from tkinter import scrolledtext
from tkinter import messagebox

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5, "Text")

combo.current(4) #set the selected item (index = 4)

combo.grid(column=0, row=0)


#                   To create a checkbutton widget кнопка-галочка
# chk_state = BooleanVar()

# chk_state.set(False) #set check state False - без галочки True- с галочкой

#                можно использовать IntVar вместо BooleanVar и установить значение 0 или 1.
chk_state = IntVar()

# chk_state.set(0) #uncheck - без галочки 

chk_state.set(1) #check - с галочкой

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=1, row=0)


#               Добавить виджеты переключателей         

rad1 = Radiobutton(window,text='First', value=1) # следует установить для каждого переключателя разное значение, иначе они не будут работать.

rad2 = Radiobutton(window,text='Second', value=2)

rad3 = Radiobutton(window,text='Third', value=3)

rad1.grid(column=0, row=1)

rad2.grid(column=1, row=1)

rad3.grid(column=2, row=1)

# command=clicked - установить команду любого из этих переключателей на определенную функцию
""" 
rad1 = Radiobutton(window,text='First', value=1, command=clicked)

def clicked():
    # Do what you need
"""


#                   Получить значение переключателя (выбранный переключатель)

selected = IntVar()

rad11 = Radiobutton(window,text='First', value=1, variable=selected)

rad12 = Radiobutton(window,text='Second', value=2, variable=selected)

rad13 = Radiobutton(window,text='Third', value=3, variable=selected)

def clicked():

   print(selected.get())

btn = Button(window, text="Click Me", command=clicked)

rad11.grid(column=0, row=2)

rad12.grid(column=1, row=2)

rad13.grid(column=2, row=2)

btn.grid(column=3, row=2)


#                          Add a ScrolledText widget (Tkinter textarea) 
#                               (from tkinter import scrolledtext)

txt = scrolledtext.ScrolledText(window,width=10,height=5)

txt.grid(column=0,row=3)

"""
Чтобы установить содержимое прокручиваемого текста, вы можете использовать метод вставки следующим образом:

txt.insert(INSERT, «Ваш текст идет сюда»)
Удалить/очистить содержимое прокручиваемого текста
Чтобы очистить содержимое виджета прокручиваемого текста, вы можете использовать метод удаления следующим образом:
txt.delete(1.0,КОНЕЦ)
"""
# т.е эту и след. строки кода я не совсем понял
txt.insert(INSERT,'You text goes here')  

txt.delete(1.0,END)


#                                  Create a MessageBox   
#                           (from tkinter import messagebox)
# and                        Show warning and error messages
def clicked():

    messagebox.showinfo('Message title', 'Message content')

    messagebox.showwarning('Message title', 'Message content')  #shows warning message

    messagebox.showerror('Message title', 'Message content')    #shows error message

btn = Button(window,text='Click here', command=clicked)

btn.grid(column=1,row=3)

# можете проверить, какая кнопка была нажата, используя переменную res
res = messagebox.askquestion('Message title','Message yes no')

res = messagebox.askyesno('Message title','Message yes no')

res = messagebox.askyesnocancel('Message title','Message yes no cancel')

res = messagebox.askokcancel('Message title','Message ok cancel')

res = messagebox.askretrycancel('Message title','Message retry cancel')



#                       Add a SpinBox (numbers widget)
spin = Spinbox(window, from_=0, to=100, width=15) # задаём с шириной width=15
spin.grid(column=1,row=4)
spin1 = Spinbox(window, values=(3, 8, 11), width=5)
spin1.grid(column=1,row=5) # Здесь виджет Spinbox показывает только эти 3 числа: 3, 8 и 11.

# Чтобы установить значение по умолчанию для Spinbox, вы можете передать значение параметру textvariable следующим образом:
var =IntVar()
var.set(36)
spin2 = Spinbox(window, from_=0, to=100, width=15, textvariable=var)
spin2.grid(column=1,row=6)


window.mainloop()