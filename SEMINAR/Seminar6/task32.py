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
from random import randint

min_num = int(input("Введите минимум: "))
max_num = int(input("Введите максимум: "))

list_ = [randint(-10, 30) for _ in range(10)]
print(list_)
list_res = list(filter(lambda x: x[1] > min_num and x[1] < max_num, enumerate(list_)))
# print(list_res)

res = []
for i, j in list_res:
    res.append(i)
print(res)