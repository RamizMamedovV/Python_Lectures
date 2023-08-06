"""
Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:                                       Вывод:
values = [0, 2, 10, 6]                      same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
"""

def same_by(characteristic, objects)-> bool:
    new = list(filter(characteristic, objects))
    print(new)

    if new == objects:
        return True
    return False


def char(x)-> bool:
    return x % 2 == 0


values = [2, 4, 5]
# values = [0, 3, 2, 10, 6]
print(same_by(char, values))

