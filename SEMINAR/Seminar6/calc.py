"""
Задача CALC необязательная. Напишите рекурсивную программу вычисления 
арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
приоритет операций стандартный.

*Пример:* 
2+2 => 4; 
1+2*3 => 7; 
1-2*3 => -5;

- Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:* 
    1+2*3 => 7; 
    (1+2)*3 => 9;
"""
#       user = '-1*12*(40+(20 + 81 / 2))*(2+ 4)'

def do_solve(nums: list, marks: list):
    right = nums.pop()
    mark = marks.pop()

    if len(nums) > 0:
        left = nums.pop()
    else:
        left = 0

    if mark == '*':
        nums.append(left * right)
    elif mark == '/':
        nums.append(left / right)
    elif mark == '+':
        nums.append(left + right)
    elif mark == '-':
        nums.append(left - right)


def select_str(string: str) -> list:
    marks = []
    nums = []
    i = 0

    while i < len(string):
        if string[i] == ' ':
            i += 1
        elif string[i] in '*/-+=(':
            marks += string[i]
            i += 1
        elif string[i] == ')':
            while marks[-1] != '(':
                do_solve(nums, marks)
            marks.pop()
            i += 1
        else:
            j = i
            num = ''
            while j < len(string) and string[j] not in '*/()+-' and string[j] != ' ':
                num += string[j]
                j += 1
            nums.append(int(num))
            i = j 
    while marks:
        do_solve(nums, marks)
    
    return nums

user = '-1*12*(40+(20 + 80 / 2))*(2+ 4)'
print(select_str(user))