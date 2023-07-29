"""
Задача №29. Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах
"""
#      Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)

#       Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     print(f"max_number = {max_number}")
#     print(f"n = {n}")
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n) 

def g_s(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    more = [i for i in array[1:] if i > pivot]

    return g_s(less) + [pivot] + g_s(more)

print(g_s([10, 2, 5]))