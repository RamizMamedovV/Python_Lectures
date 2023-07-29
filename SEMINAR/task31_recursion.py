"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""

def fibonacci(num):
    if num == 0 or num == 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

num = 2
print(f"fibonacci {num}-й = {fibonacci(num)}")