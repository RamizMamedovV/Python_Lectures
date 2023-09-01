"""
Задача №17. Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""

import random

list = []
for _ in range(10):
    list.append(random.randint(0,5))

list_res = []
for i in list:
    if not (i in list_res):
        list_res.append(i)

print(list)
print(list_res)

print(set(list))                # second option