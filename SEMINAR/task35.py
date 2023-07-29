"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

def simple_num(num, dif = 2):
    if (dif == num):
        print("yes")
        return
    if num % dif == 0:
        print("no")
        return
    else:
        simple_num(num, dif + 1)
            

num = int(input("Введите число: "))
simple_num(num)