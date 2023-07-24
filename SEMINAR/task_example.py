"""
Задача №1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2
"""
# import math
# per_day = int(input("Введите дистанцию за день: "))
# dist = int(input("Введите общую дистанцию: "))

# if dist <= 0:
#     print("Не корректный ввод")
# # print(f"Потребуется дней: {(dist + per_day - 1) // per_day }") 
# print(f"Потребуется дней: {math.ceil(dist / per_day)}")

from decimal import Decimal, getcontext

# Устанавливаем точность в 4 знака после запятой
getcontext().prec = 4

# Создаем Decimal объекты для чисел
x = Decimal('10.345')
y = Decimal('3.1416')
z = Decimal('2.71828')

# Выполняем арифметические операции с Decimal объектами
sum_result = x + y
diff_result = x - y
mul_result = x * y
div_result = x / y

print("Сумма:", sum_result)  # Сумма: 13.49
print("Разность:", diff_result)  # Разность: 7.20
print("Умножение:", mul_result)  # Умножение: 32.44
print("Деление:", div_result)  # Деление: 3.290
