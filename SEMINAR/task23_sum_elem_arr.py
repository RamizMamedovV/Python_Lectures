"""
Задача №23. Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""

import random

array = []
count = 0

for i in range(7):
    array.append(random.randint(0, 7))

print(array)

for i in range(len(array)-1):
    if array[i+1] > array[i]:
        count += 1

print(f"Количество элементов массива, больших предыдущего = {count}")
