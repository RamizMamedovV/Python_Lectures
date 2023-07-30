"""
задача 1 необязательная. Напишите программу, которая получает целое число и 
возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата.
*Дополнительно
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов где это возможно
Используйте функции
"""

def binary(num):
    if num == 2:
        return [1, 0]
    elif num <= 1:
        return [num]
    else:
        bin = num % 2
        return binary(num // 2) + [bin]
    
def octal(num):
    if num <= 8:
        return [num]
    else:
        oc = num % 8
        return octal(num // 8) + [oc]

def user_enter():
    print("Двоичная система = '2', Восьмеричная = '8'")
    choice = int(input("Введите требуюмую систему счисления: "))
    num = int(input("Введите число: "))

    if choice == 2:
        bin = []
        bin = binary(num)
        print()
        print(*bin)
        print()
        enter = int(input("Для продолжения наберите: '1': "))
        if enter == 1:
            user_enter()
        else:
            return

    elif choice == 8:
        oct = []
        oct = octal(num)
        print()
        print(*oct)
        print()
        enter = int(input("Для продолжения наберите: '1': "))
        if enter == 1:
            user_enter()
        else:
            return

    else:
        print("Не корректный ввод!")
        enter = int(input("Для продолжения наберите: '1': "))
        if enter == 1:
            user_enter()
        else:
            return




user_enter()
