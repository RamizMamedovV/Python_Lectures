"""
11. Добавьте виджет Progressbar
11.1 Изменение цвета индикатора прогресса
12 Добавьте диалоговое окно файла (выбор файлов и каталогов)
12.1 Укажите типы файлов (фильтруйте расширения файлов)
13 Добавьте строку меню
14 Добавьте виджет «Блокнот» (управление вкладками)
14.1 Добавление виджетов в блокноты
15 Добавьте интервал для виджетов (отступы)
"""

#                   Добавьте виджет Progressbar
"""Чтобы создать индикатор выполнения, вы можете использовать класс индикатора выполнения следующим образом:"""

# from tkinter.ttk import Progressbar
# bar = Progressbar(window, length=200)

        # Вы можете установить значение индикатора выполнения следующим образом:
# bar['value'] = 70

""" Вы можете установить это значение в зависимости от любого процесса, например загрузки файла или выполнения задачи."""

#                           Изменить цвет прогрессбара

"""Изменить цвет индикатора прогресса немного сложно, но очень просто.

Сначала мы создадим стиль, установим цвет фона и, наконец, установим созданный стиль для индикатора прогресса."""

# Проверьте следующий пример:

# from tkinter import *

# from tkinter.ttk import Progressbar

# from tkinter import ttk

# window = Tk()

# window.title("Ra")

# window.geometry('350x200')

# style = ttk.Style()

# style.theme_use('default')

# style.configure("black.Horizontal.TProgressbar", background='black')

# bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

# bar['value'] = 10

# bar.grid(column=0, row=0)

# window.mainloop()


#                       Добавить файловый диалог (выбор файлов и каталогов)
"""Чтобы создать диалог файла (выбор файла), вы можете использовать класс filedialog следующим образом:"""
# from tkinter import filedialog
# file = filedialog.askopenfilename()

"""После того, как вы выберете файл и нажмете кнопку «Открыть», переменная файла будет содержать этот путь к файлу.
Кроме того, вы можете запросить несколько файлов, например:"""

# files = filedialog.askopenfilenames()


"""Укажите типы файлов (фильтруйте расширения файлов)
Вы можете указать типы файлов для диалогового окна файла, используя параметр filetypes, просто укажите расширения в кортежах:"""

# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))


# Вы можете запросить каталог, используя метод AskDirectory:

#dir = filedialog.askdirectory()


"""Вы можете указать начальный каталог для диалогового окна файла, указав начальный каталог следующим образом:"""

# from os import path
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))


#                           Добавить строку меню
# Чтобы добавить строку меню, вы можете использовать класс меню следующим образом:

# from tkinter import *
# from tkinter import Menu

# window = Tk()

# window.title("Ra")

# window.geometry('350x200')
# menu = Menu(window)

# menu.add_command(label='File')

# window.config(menu=menu)
# window.mainloop()

"""Сначала мы создаем меню, затем добавляем первую метку и, наконец, назначаем меню нашему окну.

Вы можете добавлять пункты меню в любое меню, используя функцию add_cascade() следующим образом:"""

# menu.add_cascade(label='File', menu=new_item)

#                                   В результате:
# from tkinter import *
# from tkinter import Menu

# window = Tk()
# window.title("RA")
# menu = Menu(window)

# # Используя этот способ, вы можете добавлять столько пунктов меню, сколько захотите.
# new_item = Menu(menu)
# new_item.add_command(label='New')
# new_item.add_separator()
# new_item.add_command(label='Edit')

# menu.add_cascade(label='File', menu=new_item)

# window.config(menu=menu)

# window.mainloop()

"""Здесь мы добавляем еще один пункт меню под названием «Редактировать» с разделителем меню.

Вы можете заметить пунктирную линию в начале. Если вы щелкнете по этой линии, пункты меню отобразятся в небольшом отдельном окне.

Вы можете отключить эту функцию, отключив функцию отрыва следующим образом:"""

# new_item = Menu(menu, tearoff=0)

"""Просто замените new_item в приведенном выше примере на этот, и пунктирная линия больше не будет отображаться.

Мне не нужно напоминать вам, что вы можете ввести любой код, который будет работать, когда пользователь щелкает любой пункт меню, указав свойство команды."""

# new_item.add_command(label='New', command=clicked)


#                       Добавьте виджет «Блокнот» (управление вкладками)
"""Чтобы создать элемент управления вкладками, необходимо выполнить 3 шага.

    - Сначала мы создаем элемент управления вкладками, используя класс Notebook.
    - Создайте вкладку, используя класс Frame.
    - Добавьте эту вкладку в элемент управления вкладками.
    - Упакуйте элемент управления вкладками, чтобы он стал видимым в окне."""

# from tkinter import *
# from tkinter import ttk

# window = Tk()
# window.title("Welcome to LikeGeeks app")

# tab_control = ttk.Notebook(window)

# tab1 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='First')

# tab_control.pack(expand=1, fill='both')

# window.mainloop()
"""Таким же образом вы можете добавить множество вкладок по своему усмотрению."""


#                       Добавляйте виджеты в блокноты
"""После создания вкладок вы можете размещать виджеты внутри этих вкладок, присвоив нужной вкладке родительское свойство."""

# from tkinter import *
# from tkinter import ttk

# window = Tk()
# window.title("Welcome to LikeGeeks app")

# tab_control = ttk.Notebook(window)

# tab1 = ttk.Frame(tab_control)

# tab2 = ttk.Frame(tab_control)

# tab_control.add(tab1, text='First')
# tab_control.add(tab2, text='Second')

# lbl1 = Label(tab1, text= 'label1')
# lbl1.grid(column=0, row=0)

# lbl2 = Label(tab2, text= 'label2')
# lbl2.grid(column=0, row=0)

# tab_control.pack(expand=1, fill='both')

# window.mainloop()


#                       Добавить интервал для виджетов (отступы)
"""Вы можете добавить отступы для своих элементов управления, чтобы они выглядели хорошо организованными, используя свойства Padx и Pady.

Просто передайте Padx и Pady любому виджету и присвойте им значение."""

# lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)