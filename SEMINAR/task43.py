"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:                   Вывод:
1 2 3 2 3                   2

"""
import random

#                               first way

def check_pairs(array : list) -> int:
    dic = {}
    count = 0
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
    for i in dic:
        count += dic[i] // 2
    return count




list_ = [random.randint(1, 5) for _ in range(9)]
print(list_)
print()
print(check_pairs(list_))


#                               second way

print(f"set = {set(list_)}")
pairs = sum(list_.count(i)  // 2 for i in set(list_))
print(pairs)