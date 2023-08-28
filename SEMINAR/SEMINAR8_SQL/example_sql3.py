"""
Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

#                         не рабочий пока вариант

import sqlite3 as sq


with sq.connect("phone_book.db") as con:    
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS contacts")

    cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            surname TEXT,
            phone_num TEXT
    )""")


def insert_into(first_name: str,last_name: str, surname: str, ph_num: str):
    query = "INSERT INTO contacts(first_name, last_name, surname, phone_num) VALUES (?, ?, ?, ?)"
    # если добавляются все поля можно пропустить первую скобку:
    # если конечно там нет id INTEGER PRIMARY KEY AUTOINCREMENT,
    # query = "INSERT INTO contacts VALUES (?, ?, ?, ?, ?)"
    values = (first_name, last_name, surname, ph_num)
    cur.execute(query, values)
    con.commit()



def show_data_four_str(first_name: str, last_name: str, surname: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND last_name = ? AND surname = ? AND phone_num = ?"
    cur.execute(query, (first_name, last_name, surname, phone_num))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_one_str(string: str):
    query = "SELECT * FROM contacts WHERE first_name = ? OR last_name = ? OR surname = ? OR phone_num = ?"
    cur.execute(query, (string, string, string, string))
    # 2 вариана вывода. но второй более эконом, т.к. не создается лист
    # result = cur.fetchall() 
    # print(result)
    for result in cur:
        print(result)
    con.commit()


def delete_data_one_str(string: str):
    query = "DELETE FROM contacts WHERE first_name = ? OR last_name = ? OR surname = ? OR phone_num = ?"
    cur.execute(query, (string, string, string, string))
    # 2 вариана вывода. но второй более эконом, т.к. не создается лист
    # result = cur.fetchall() 
    # print(result)
    for result in cur:
        print(result)
    con.commit()


def user_choise():
    show_data()
    wish = True
    while(wish):
        choise = input("\nДля поиска по справочнику 1\nДля удаления из справочника 2\nВведите ваш выбор для продолжения: ")
        if choise == '1':
            enter = input(f"\nВведите искомый контакт: ")
            show_data_one_str(enter)
        elif choise == '2':
            enter = input(f"\nВведите удаляемый контакт: ")
            delete_data_one_str(enter)
        elif choise != '1':
            wish = False
    con.close()


def user_input():
    wish = True
    while(wish):
        first_name = input(f"\nВведите имя: ")
        last_name = input("Введите фамилию: ")
        surname = input("Введите отчество: ")
        phone_num = input("Введите номер телефона: ")
        insert_into(first_name,last_name, surname, phone_num)
        choise = input(f"\nВведите 1 для продожения: ")
        if choise != '1':
            wish = False
    print()
    user_choise()


def show_data(): # показываем все записи таблицы users
    cur.execute("SELECT * from contacts")
    for row in cur.fetchall():
        print(row)


first_name = ''
last_name = ''
surname = ''
phone_num = ''

if __name__ == "__main__":
    user_input()