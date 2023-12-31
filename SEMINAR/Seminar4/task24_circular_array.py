"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном списке урожайности грядки.
"""

import random

def picking_berries(list, bush_num):
    if len(list) >= 3:
        if bush_num == 0:
            return list[-1] + list[0] + list[1]
        elif bush_num == len(list)-1:
            return list[-2] + list[-1] + list[0]
        else:
            return list[bush_num -1] + list[bush_num] + list[bush_num +1] 
    elif len(list) == 2:
        return list[0] + list[1]
    elif len(list) == 1:
        return list[0]

def user_print():
    amount_bushes = int(input("Введите кол-во кустов: "))
    list_bushes = []
    for i in range(amount_bushes):
        list_bushes.append(random.randint(5, 10))
    
    return list_bushes


    




arr = []
arr = user_print()
print(f"Ягоды созрели: {arr}")
gather = int(input("Введите номер куста(от 0) для сборки: "))

print(f"Максимально число ягод: {picking_berries(arr, gather)}")