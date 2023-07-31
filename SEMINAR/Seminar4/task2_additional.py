"""
задача 2 необязательная.
Даны два многочлена, которые вводит пользователь.
Задача - сформировать многочлен, содержащий сумму многочленов.
Степени многочленов могут быть разные.

например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re
"""

from equations import *

def sum_coefs(list_1, list_2):
    if len(list_1) > len(list_2):
        res_coefs = list_1
        for a, i in zip(reversed(list_2), reversed(range(len(res_coefs)))):
            res_coefs[i] += a
        return res_coefs
    elif len(list_1) == len(list_2):
        res_coefs = list_1
        for a, i in zip(reversed(list_2), reversed(range(len(res_coefs)))):
            res_coefs[i] += a
        return res_coefs
    else:
        return sum_coefs(list_2, list_1)

    


deg_1 = int(input("Введите степень первого многочлена: "))

coeffs_1 = []
for i in range(deg_1 + 1):
    coeffs_1.append(int(input(f"Введите его коэффициенты (можно с '-') номер {i}: ")))

deg_2 = int(input("Введите степень первого многочлена: "))

coeffs_2 = []
for i in range(deg_2 + 1):
    coeffs_2.append(int(input(f"Введите его коэффициенты (можно с '-') номер {i}: ")))

res_coefs = sum_coefs(coeffs_1, coeffs_2)
res_deg = max(deg_1, deg_2)
print(res_coefs)
print(res_deg)

format_list(res_coefs)
print(res_coefs)
print(equation(0, res_deg, res_coefs))