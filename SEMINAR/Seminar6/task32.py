"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""

#               Оформлять всё через функции! это обязательное условие)))

from random import randint

def find_index(min_number, max_number, array):
    return list(filter(lambda x: x[1] > min_num and x[1] < max_num, enumerate(list_)))



min_num = int(input("Введите минимум: "))
max_num = int(input("Введите максимум: "))

list_ = [randint(-10, 10) for _ in range(10)]
print(list_)


res = []
for i, j in find_index(min_num, max_num, list_):
    res.append(i)
print(res)