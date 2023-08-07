"""
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

#               Оформлять всё через функции! это обязательное условие)))

def arithmetic_progression(start = 0, step = 2, amount = 10):
    array = []
    stop = amount * step + start
    for i in range(start, stop, step):
        array.append(i)
    return array

start = int(input("Введите начало: "))
step = int(input("Введите шаг: "))
amt = int(input("Введите кол-во элем-ов: "))

print(arithmetic_progression(start, step, amt))

# stop = amt * step + start
# arr = [x for x in range(start, stop, step)]

# print(arr)