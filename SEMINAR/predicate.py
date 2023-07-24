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
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not(x or y or z) == (not x and not y and not z))