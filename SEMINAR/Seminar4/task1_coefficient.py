"""
Задана нат. степень К. 
сформировать случ. образом список коэфф. (знач: от 0 до 100)
мпногочлена и записать как мноочлен степени К
Пример:
К = 2 -> 2 * X^2 + 4 * X + 5 = 0 or X^2 + 5 = 0 or 10 * X^2 = 0
"""
import random
from equations import *
    

degree = int(input("Введите степень: "))

coefficients = []
for i in range(degree + 1):
    coefficients.append(random.randint(0, 8))

print(coefficients)
print(equation(0, degree, coefficients))



                            # РЕШЕНИЕ В ГРУППЕ НЕ ИСПОЛЬЗУЯ РЕКУРСИЮ
                            
# k = int(input("Input your degree: "))

# coefficients = []
# for i in range(k+1):
#     coefficients.append(random.randint(0, 11))
# result = ''

# for i in range(len(coefficients) - 1):
#     degree = len(coefficients)-i-1
#     if degree > 1:
#         degree = f"*X^{degree}"
#     elif degree == 1:
#         degree = "*X"
#     else:
#         degree = ""
#     if coefficients[i] > 1:
#         result += f"{coefficients[i]}{degree} + "
#     elif coefficients[i] == 1:
#         result += f"{degree[1:]} + "

# result += f"{coefficients [-1]} = 0"
# print(coefficients)
# print(result)