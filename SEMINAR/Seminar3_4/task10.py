# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

coins = int(input("Введите кол-во манет: "))
qerb = int(input("Введите кол-во манет лежащих гербом: "))

res = coins // 2
if res > qerb:
    print(f"Монеты с решкой, мин в кол-ве {res - qerb} шт, нужно перевернуть ")
elif qerb > res:
    print(f"Монеты с гербом, мин в кол-ве {qerb - res} шт, нужно перевернуть ")
else:
    print("Ничего переворачивать не нужно!")