"""
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод:                       Ввод:
5                               5
1 2 3 4 5                   1 5 1 5 1
Вывод:                      Вывод
       0                            2
"""

from random import randint

def check_neighbors(list):
    count =  0
    for i in range(len(list)):
        if i == len(list)-1:
            if list[i - 1] < list[i] and list[0] < list[i]:
                count += 1
        else:
            if list[i - 1] < list[i] and list[i] > list[i + 1]:
                count += 1
    return count
           



mas2 = [randint(1,10) for _ in range(5)]
print(mas2)

print(check_neighbors(mas2))


#                                    second way

# def check_neighbors(index, sp: list):
#     mid = sp[index]
#     left = sp[index-1]
#     if index == len(sp)-1:
#         right = sp[0]
#     else:
#         right = sp[index+1]
#     return int(mid > left and mid > right)


# current_list = [5, 1, 3, 2, 5, 4]

# res = [check_neighbors(index, current_list) for index in range(len(current_list))]

# print(current_list)
# print(sum(res))