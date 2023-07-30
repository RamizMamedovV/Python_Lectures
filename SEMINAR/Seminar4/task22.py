"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
"""

def quick_sort(list):
    if len(list) <= 1:
        return list
    middle = list[0]
    left_list = [x for x in list if x < middle]
    right_list = [y for y in list if y > middle]

    return quick_sort(left_list) + [middle] + quick_sort(right_list)

amount1 = input("Введите несколько чисел для 1-ого списка ЧЕРЕЗ ПРОБЕЛ: ")
amount2 = input("Введите несколько чисел для 2-ого списка ЧЕРЕЗ ПРОБЕЛ: ")

values1 = amount1.split(" ")
values2 = amount2.split(" ")

numbers1 = [int(x) for x in values1]
numbers2 = [int(y) for y in values2]

num_set1 = set(numbers1)
num_set2 = set(numbers2)

res_set = num_set1.union(num_set2)
set_to_list = list(res_set.copy())

print(quick_sort(set_to_list))
