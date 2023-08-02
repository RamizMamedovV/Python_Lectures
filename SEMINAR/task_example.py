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


# x: int = 3
# y: int = 5
# print(x + y)          # 8

# x: int = 'hello '
# y: int = 'world'
# print(x + y)            # hello world

# x: int = 'hello '
# y: int = 5
# print(x * y)                # hello hello hello hello hello 

# def sum(spisok):
#     s = 0
#     for i in spisok:
#         s += i
#     print(s)                    # без return

# def sum1(spisok):
#     s = 0
#     for i in spisok:
#         s += i
#     return s                    # c return

# def sum2(spisok: list) -> int:          # int - для аннотации результата!
#     s: int = 0
#     for i in spisok:
#         s += i
#     return s                    # c аннотацией для понимания! list,int



# sum([5, 4, 3])
# print(sum1([5, 4, 3]))

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     more = [i for i in array[1:] if i > pivot]

#     return quick_sort(less) + [pivot] + quick_sort(more)

# print(quick_sort([10, 2, 5]))

"""
seminar 6
from random import randint
def find_and_square(sp):
    result = []
    for item in sp:
        if item > 4:
            result.append(item**2)
    return result



sp = [5, 8, 1, 3, 10, 0]
print(find_and_square(sp))
print([x**2 for x in sp if x > 4])
rsp = [randint(0,11) for _ in range(10)]
print(rsp)

#надо найти все элементы больше 4 ,
# далее получить новый список с квадратами таких элементов
# s2 = sp[::]
# print(s2)
# sp.append(888)
# print(s2)
"""



"""                               #       if isinstance(item,list)
def sum_count(sp):
    total = 0
    for item in sp:
        # if str(type(item)) == "<class 'list'>" :
        # if type(item) == type([]):
        if isinstance(item,list):
            total = total + sum_count(item)
        else:
            total += item
    return total



count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york, count_chicago]
count_all = [count_angola, count_usa]
print(count_all)
print(type(count_all))
print(sum_count(count_all))
"""