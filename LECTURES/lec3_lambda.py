"""
Что будет на лекции сегодня
● Анонимные, lambda-функции
● Функция map
● Функция filter
● Функция zip
● Функция enumerate
● Файлы
● Модуль os
● Модуль shutil
"""


# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):           # ор - ссылка на другую фенкцию
#     print(op(x, y))

# math(calk2, 5, 55)            # 275


#           в лямбде можно сразу описать передаваемую функцию
"""
некоторые функции могут
понадобиться всего раз за всю работу приложения.
"""
# def math(op, a, b):
#     print(op(a, b))

# math(lambda a, b: a + b, 5, 55)     # 60
# math(lambda a, b: a * b, 5, 55)     # 275



# list_ = [1, 2, 3, 5, 8, 15, 23, 38]
# list_1 = [(x, x**2) for x in list_ if x % 2 == 0]
# print(list_1)

# def select(f, col):                                   # select == map 
#     return [f(x) for x in col]

# def where(f, col):                                    # where == filter
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)                                # select == map 
# print(res)
# res = where(lambda x: x % 2 == 0, res)                 # where == filter
# print(res)
# res = list(select(lambda x: (x, x**2), res))           # select == map 
# print(res)

#          т.е. можно воспользоваться встроенными функциями python и записать так:

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)                                      # [(2, 4), (8, 64), (38, 1444)]
"""
Итак:
1. Сначала мы избавились от классического описания функций.
2. Затем научились описывать лямбды, присваивая результат какой-то переменной.
3. После избавились от этой переменной, пробрасывая всю лямбду в качестве функции.

"""




#                               map
"""
Функция map
Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с новыми объектами.

Результат работы map() — это итератор. По итератору можно пробежаться только один раз. Чтобы
работать несколько раз с одними данными, нужно сохранить данные (например, в виде списка).

class map(
    __func: (_T1@__init__) -> int,
    __iter1: Iterable[_T1@__init__],
    /
)
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from each of the iterables. 
Stops when the shortest iterable is exhausted.
Создайте итератор, который вычисляет функцию, используя аргументы от каждого из итерируемых объектов.
Останавливается, когда самая короткая итерация исчерпана.
"""

# list_ = [x for x in range(1, 10)]
# print(list_)

# list_ = list(map(lambda x: x + 10, list_))
# print(list_)



#                    как превратить list строк в list чисел с помощью map?

# data = '1 2 3 4 13 12'

# # data = int(data)     # ValueError: invalid literal for int() with base 10: '1 2 3 4 13 12'

# data = list(map(int,data.split())) # [1, 2, 3, 4, 13, 12]
# print(data)

"""
 функция строка.split() - убирает все пробелы и создаем список из
значений строки, пример:
data = '1 2 3 5 8 15 23 38'.split()
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

"""




#                               filter
"""
Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с теми объектами, для которых функция вернула True.


class filter(
    __function: (int) -> Any,
    __iterable: Iterable[int],
    /
)
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item) is true. 
If function is None, return the items that are true.
Возвращает итератор, возвращающий те элементы итерации, для которых функция (элемент) истинна.
Если функция имеет значение None, верните элементы, которые верны.
"""

# data = [15, 65, 44, 3]
# res = list(filter(lambda x: x % 10 ==5, data))
# print(res)                                      #  [15, 65]




#                               zip

"""
Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
из элементов входных данных

class zip(
    __iter1: Iterable[_T1@__new__],
    __iter2: Iterable[_T2@__new__],
    __iter3: Iterable[_T3@__new__],
    *,
    strict: bool = ...
)
"""
# users = ['user1', 'user2', 'user3', 'user4']    # 4 элемента
# ids = [1, 2, 3, 4, 5]                           # 5 элементов
# salary = [100, 200, 300]                        # 3 элемента

# data = list(zip(ids, users, salary))
# print(data) # [(1, 'user1', 100), (2, 'user2', 200), (3, 'user3', 300)] 3 элемента




#                               enumerate

"""
Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
кортежами из индекса и элементов входных данных.


class enumerate(
    iterable: Iterable[str],
    start: int = ...
)
"""
# enum = ['zero', 'one', 'two']
# data = list(enumerate(enum))
# print(data)                 # [(0, 'zero'), (1, 'one'), (2, 'two')] 





#                                           Файлы
"""
Файлы в текстовом формате используются для:
● Хранения данных
● Передачи данных в клиент-серверных проектах
● Хранения конфигов
● Логирования действий
Что нужно для работы с файлами:
1. Завести переменную, которая будет связана с этим текстовым файлом.
2. Указать путь к файлу.
3. Указать, в каком режиме мы будем работать с файлом.


Варианты режима (мод):
a – открытие для добавления данных.
○ Позволяет дописывать что-то в имеющийся файл.
○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
и в него начнется запись.
r – открытие для чтения данных.
○ Позволяет читать данные из файла.
○ Если вы попробуете считать данные из файла, которого не существует, программа
выдаст ошибку.
w – открытие для записи данных.
○ Позволяет записывать данные и создавать файл, если его не существует.

Миксованные режимы:
1. w+
○ Позволяет открывать файл для записи и читать из него.
○ Если файла не существует, он будет создан.
2. r+
○ Позволяет открывать файл для чтения и дописывать в него.
○ Если файла не существует, программа выдаст ошибку.
"""

#                   Примеры использования различных режимов в коде:
# 1. Режим a
 
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать
                                    # encoding='utf-8' применяется по умолчанию!!!  можно изменить
# data.writelines(colors) # разделителей не будет
# data.close()

"""
при перезапуске дописыват к имеющимся
● data.close() — используется для закрытия файла, чтобы разорвать подключение файловой
переменной с файлом на диске.
● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
● При повторном выполнении скрипта redbluedreenredbluedreen — добавление в
существующий файл, а не перезапись файлов.
"""


#                   Ещё один способ записи данных в файл:
"""
режим with позволяет закрывать автоматически для этого используем в конце команду print("ok")
 т.е. не использовать data.close()
open........... as data: открываем с именем "data"
режим называется 'w'
создается файл file.txt, если он не существовал
при перезапуске перезаписыват всё, а не домисыват
"""

# with open('file.txt', 'w') as data:        
#     data.write('line 1\n')
#     data.write('line 4\n')

# print("ok")                 # что-бы не использовать data.close()



#                                           2. Режим r
# ● Чтение данных из файла:

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()




#                                           Модуль os

# """
# Модуль os предоставляет множество функций для работы с операционной системой, причем их
# поведение, как правило, не зависит от ОС, поэтому программы остаются переносимыми.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать в свою
# программу:
# import os
# Познакомимся с базовыми функциями данного модуля:
# # ● os.chdir(path) - смена текущей директории.
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
# # ● os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# # ● os.path - является вложенным модулем в модуль os и реализует некоторые полезные функции
# для работы с путями, такие как:

# # ○ os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #'main.py'

# # ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'
# Это лишь малая часть возможностей модуля os.
# """




#                                       Модуль shutil

"""
Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок. В частности,
доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки. Часто используется вместе
с модулем os.
Для того, чтобы начать работать с данным модулем необходимо его импортировать в свою программу:
import shutil
Познакомимся с базовыми функциями данного модуля:
● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst.
● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path должен указывать на
директорию, а не на символическую ссылку.

"""

# orbits = [(1, 3), (2.5, 10)]
# print(orbits[1])
# res = list(map(lambda x: x[0] * x[1], orbits))
# print(res)