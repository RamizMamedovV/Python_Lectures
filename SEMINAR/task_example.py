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