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
#               Находится на стадии разработки!!!))))

# exercise = '3+2*4*(5+65)'
# p = '*'
# d = '/'
# s = '+'
# m = '-'
# br_l = '('
# br_r = ')'
# priority1 = ''
# delet = ''
# res = ''
# if br_l in exercise:
#     delet = exercise[exercise.index(br_l):exercise.index(br_r) + 1]
#     for i in exercise[exercise.index(br_l) + 1:exercise.index(br_r)].split():
#         priority1 += i
#     if s in priority1:
#         res = int(priority1[0]) + int(priority1[2:])
#         print(res)
# exercise = exercise.replace(str(delet), str(res))
# if p in exercise:
#     delet = exercise[exercise.index(p)-1 : exercise.index(p) + 2]
#     if p in delet:
#         res = int(delet[0]) * int(delet[2])
#         print(res)
# exercise = exercise.replace(str(delet), str(res))
# if p in exercise:
#     delet = exercise[exercise.index(p)-1 : exercise.index(p) + 2]
#     if p in delet:
#         res = int(delet[0]) * int(delet[2])
#         print(res)
# exercise = exercise.replace(str(delet), str(res))
# if s in exercise:
#     delet = exercise[exercise.index(s)-1 : exercise.index(s) + 2]
#     if s in delet:
#         res = int(delet[0]) + 560
#         print(res)
# exercise = exercise.replace(str(delet), str(res))
# print(exercise)