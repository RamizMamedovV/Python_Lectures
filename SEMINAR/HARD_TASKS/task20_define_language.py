"""
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод: 12
"""

# from langdetect import detect

# text1 = input("Введите слово на английском или русском языке: ")

# language = detect(text1)
# print("Определенный язык:", language)

# if language == "en":
#     print("hello")
# elif language == "mk" or language == "ru":
#     print("привет")
# else:
#     print("I don't know this language!")

# # def detect_alphabet(text):
#     cyrillic_count = sum(1 for char in text if 0x0400 <= ord(char) <= 0x04FF)
#     latin_count = sum(1 for char in text if 0x0041 <= ord(char)
#                        <= 0x007A or 0x0061 <= ord(char) <= 0x007A)

    # if cyrillic_count > latin_count:
    #     return "Кириллице"
    # elif latin_count > cyrillic_count:
    #     return "Латинице"
    # else:
    #     return "Не удалось определить"
# print(f"Текст написан на {alphabet}.")




def detect(text):
    cyrillic_count = sum(1 for char in text if 0x0400 <= ord(char) <= 0x04FF)
    latin_count = sum(1 for char in text if 0x0041 <= ord(char) <= 0x007A 
                      or 0x0061 <= ord(char) <= 0x007A)

    if cyrillic_count > latin_count:
        result = scoring_rus(text)
    elif latin_count > cyrillic_count:
        result = scoring_lat(text)
    else:
        result = "Не удалось определить"

    return result
"""
def scoring_rus(text):
    count = text.count("ф") + text.count("щ") + text.count("ъ")
    count += 10 * text.count("ф") + text.count("щ") + text.count("ъ")
    count += 8 * text.count("ш") + text.count("э") + text.count("ю")
    count += 5 * text.count("ж") + text.count("з") + text.count("х") + text.count("ц") + text.count("ч")
    count += 4 * text.count("й") + text.count("ы")
    count += 3 * text.count("б") + text.count("г") + text.count("ё") + text.count("ь") + text.count("я")
    count += 2 * text.count("д") + text.count("к") + text.count("л") + text.count("м") + text.count("п") + text.count("у")
    count += 1 * text.count("а") + text.count("в") + text.count("е") + text.count("и") + text.count("н") + text.count("о")
    count += 1 * text.count("р") + text.count("с") + text.count("т") 
    return count
"""   
def scoring_rus(text):
    count = 0
    for i in text:
        if i == "ф" or i == "щ" or i == "ъ":
            count += 10
        elif i == "ш" or i == "э" or i == "ю":
            count += 8
        elif i == "ж" or i == "з" or i == "х" or i == "ц" or i == "ч":
            count += 5
        elif i == "й" or i == "ы":
            count += 4
        elif i == "б" or i == "г" or i == "ё" or i == "ь" or i == "я":
            count += 3
        elif i == "д" or i == "к" or i == "л" or i == "м" or i == "п" or i == "у":
            count += 2
        else:
            count += 1
    return count

def scoring_lat(text):
    count = 0
    for i in text:
        if i == "q" or i == "z":
            count += 10
        elif i == "j" or i == "x":
            count += 8
        elif i == "k":
            count += 5
        elif i == "f" or i == "h" or i == "v" or i == "w" or i == "y":
            count += 4
        elif i == "b" or i == "c" or i == "m" or i == "p":
            count += 3
        elif i == "d" or i == "g":
            count += 2
        else:
            count += 1
    return count

# Ваш текст
text = input("Введите текст латинскими буквами или кириллицей: ")

count = detect(text.lower())
print(count)