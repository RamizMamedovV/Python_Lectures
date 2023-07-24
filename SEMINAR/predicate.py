"""
Это утверждение представляет первую теорему де Моргана, 
которую я описал в предыдущем ответе. Давайте разберемся, что оно означает:

¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

Здесь:
¬ обозначает операцию "НЕ" (отрицание).
⋁ обозначает операцию "ИЛИ" (дизъюнкция).
⋀ обозначает операцию "И" (конъюнкция).
Итак, утверждение гласит: "Отрицание объединения (дизъюнкции) 
трех утверждений X, Y и Z равно пересечению (конъюнкции) отрицаний 
каждого из этих утверждений отдельно."
"""
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not(x or y or z) == (not x and not y and not z))

"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат.
теперь надо проверить ее практически в цикле 100 раз прогоняем
каждый раз генерируем случайное количество предикат от 3 до 15
и конечно со случайным булевым значением
и засекаем общее время выполнения программы
юзаем библиотеки random и time
предикаты НЕ ЗАДАЕМ как целое число!
"""
import random
import time

start = time.time()
for _ in range(100):
    predicates_gty = random.randint(3, 15)
    array_pred = []
    array_pred_not = []
    for i in range(predicates_gty):
        array_pred.append(random.choice([True, False]))
        array_pred_not.append(not array_pred[i])
    for i in range(len(array_pred)):
        print(not(array_pred[i]) == array_pred_not[i])  

print(time.time() - start)