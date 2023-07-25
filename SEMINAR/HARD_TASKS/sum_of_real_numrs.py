"""
Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя. Можно юзать decimal
"""
from decimal import Decimal, getcontext

getcontext().prec = 4

num = int(input("Введите кол-во чисел: "))

array = []
for i in range(num):
    inp = input(f"Введите {i+1} число: ")
    d = Decimal(inp)
    array.append(d)


print(array)

