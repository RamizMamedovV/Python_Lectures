def count_vowels(word):
    vowels = "AEIOUaeiou"  # Список гласных букв
    count = 0
    
    for char in word:
        if char in vowels:
            count += 1
            
    return count

def main():
    poem = input("Введите стихотворение: ")
    lines = poem.split()  # Разделение стихотворения на строки
    
    prev_count = None  # Предыдущее количество слогов
    
    for line in lines:
        words = line.split('-')  # Разделение строки на слова
        
        line_count = count_vowels(''.join(words))  # Подсчет гласных в строке
        
        if prev_count is None:
            prev_count = line_count
        elif prev_count != line_count:
            print("Пам парам")
            return
    
    print("Парам пам-пам")

if __name__ == "__main__":
    main()
