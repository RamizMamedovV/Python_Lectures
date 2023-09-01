"""
Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 10^5
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:                       Вывод:
300                             220 284
"""


#                    Этот метод заполняет стек!!!


# def sum_div(num,res = 0, start = 1):
#     if start > num - num // 2 or num == 1:
#         return res
#     else:
#         if num % start == 0:
#             res += start
#         return sum_div(num, res, start + 1)
    

# num_1 = int(input("Введите число больше 3-х: "))
# for i in range(4, num_1):
#     temp_1 = sum_div(i)
#     temp_2 = sum_div(temp_1)
#     if temp_2 == i:
#         print(f"{i} == {temp_1}")



#                           мой лучший метод!!!

# def sum_div(num):
#     res = 0
#     for start in range(1, num // 2 + 1):
#         if num % start == 0:
#             res += start
#     return res

# num_1 = int(input("Введите число больше 3-х: "))
# res = {}

# for i in range(4, num_1):  
#     temp_1 = sum_div(i)
#     temp_2 = sum_div(temp_1)
#     if i == temp_2 and temp_1 != i and i < temp_1:
#         res[temp_1] = temp_2
#         print(f"{temp_2} == {temp_1}")
       

#                           метод коллег учшее

def sum_div1(num):
    res = 1
    for start in range(2, int(num ** 0.5) + 1):
        if num % start == 0:
            res += start
            if start != num // start:
                res += num // start
    return res

def find_frendly_numbers(num) -> list[tuple[int, int]]:
    frendly_pairs = []

    for n in range(1, num + 1):
        m = sum_div1(n)

        if m < n and sum_div1(m) == n :
            pair = (n , m)
            frendly_pairs.append(pair)
    return frendly_pairs

num1 = int(input("Введите число: "))
pairs = find_frendly_numbers(num1)

for pair in pairs:
    print(pair[0], pair[1])