"""
Задана нат. степень К. 
сформировать случ. образом список коэфф. (знач: от 0 до 100)
мпногочлена и записать как мноочлен степени К
Пример:
К = 2 -> 2 * X^2 + 4 * X + 5 = 0 or X^2 + 5 = 0 or 10 * X^2 = 0
"""
import random

def equation(coef: int, deg: int) -> str:
    if deg == 0:
        return f"{coefficients[coef]} = 0"
    else:
        if deg == 1:
            return f"{coefficients[coef]}*x + " + equation(coef + 1, deg - 1)
        elif coefficients[coef] == 1:
            return f"x^{deg} + " + equation(coef + 1, deg - 1)
        elif coefficients[coef] == 0:
            return equation(coef + 1, deg - 1)
        else:
            return f"{coefficients[coef]}*x^{deg} + " + equation(coef + 1, deg - 1)
    

degree = int(input("Введите степень: "))

coefficients = []
for i in range(degree + 1):
    coefficients.append(random.randint(0, 5))

# index = 0
print(coefficients)
print(equation(0, degree))



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