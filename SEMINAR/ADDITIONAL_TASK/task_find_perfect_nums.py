"""
Совершенными считаются числа, если E(n) = 2n
сумма делителей числа n = 2n, 
кроме него самого = ему самому!
При вводе чат. число (> 0),
программа выведит все совершенные числа в этом диапозоне
например:
Ввод:                       Вывод:
500                             6, 28, 496
"""

def sum_div(num,res = 0, start = 1):
    if start > num - num // 2 or num == 1:
        return res
    else:
        if num % start == 0:
            res += start
        return sum_div(num, res, start + 1)
    

user_num = int(input("Введите число больше 3-х: "))
for i in range(4, user_num + 1):
    temp_1 = sum_div(i)
    temp_2 = sum_div(temp_1)
    if temp_1 == i:
        print(f"Совершенное число: {temp_1}")