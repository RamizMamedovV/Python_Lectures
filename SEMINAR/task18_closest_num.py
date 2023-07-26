"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
"""
import random
import math

length = int(input("Введите длину массива: "))
desired_num = int(input("Введите искомое число: "))

array = []
closest_arr = []

for i in range(length):
    array.append(random.randint(0, 50))


# for i in range(length):
#     closest_arr.append(desired_num - array[i])
#     closest_arr[i] = abs(closest_arr[i])

for i in range(length):
    closest_arr.append(desired_num - array[i])
    if closest_arr[i] < 0:
        closest_arr[i] = closest_arr[i] * (-1)

min = closest_arr[0]
for i in range(len(closest_arr)):
    if closest_arr[i] < min:
        min = closest_arr[i]

for i in range(len(closest_arr)):
    if min == closest_arr[i]:
        print(f"самый близкий = {array[i]}")
        break


print(f"closest_arr = {closest_arr}")
print(array)
