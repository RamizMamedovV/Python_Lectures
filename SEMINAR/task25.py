"""
Задача №25. Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

letters = 'a a a b c a a d c d d'
str1 = letters.split(" ")
dictionary = {}
final_str = ''
for i in str1:
    if i in dictionary:
        dictionary[i] += 1
        final_str += f"{i}_{dictionary[i]} "
    else:
        dictionary[i] = 0
        final_str += f"{i} "

print(final_str)