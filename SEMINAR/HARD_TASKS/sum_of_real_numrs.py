"""
Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя. 
Можно юзать decimal
"""
from decimal import Decimal, getcontext

getcontext().prec = 4

# num = int(input("Введите кол-во чисел: "))

# array = []
# for i in range(num):
#     inp = input(f"Введите {i+1} число: ")
#     d = Decimal(inp)
#     array.append(d)

array = [4, 55, 77.55, 0.35, 2,45, 5,55]

count = 0

for i in array:
    if i %1 != 0:
        while i % 1 != 0:
            i *= 10
    while i > 0:
        if i %10 == 5:
            count += 1
        i = i // 10


print(f"count = {count}")


