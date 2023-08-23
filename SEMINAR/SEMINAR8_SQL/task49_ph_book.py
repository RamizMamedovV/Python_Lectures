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

import sqlite3 as sq
from first_name_defs import *
from last_name_defs import *
from surname_defs import *

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

    con.commit()

def insert_into(first_name: str,last_name: str, surname: str, ph_num: str):
    query = "INSERT INTO contacts(first_name, last_name, surname, phone_num) VALUES (?, ?, ?, ?)"
    values = (first_name, last_name, surname, ph_num)
    cur.execute(query, values)
    con.commit()



def show_data_f_l_s_name_p_num(first_name: str, last_name: str, surname: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND last_name = ? AND surname = ? AND phone_num = ?"
    cur.execute(query, (first_name, last_name, surname, phone_num))
    result = cur.fetchall()
    print(result)
    con.commit()

def show_data_p_num(phone_num: str):
    query = "SELECT * FROM contacts WHERE phone_num = ?"
    cur.execute(query, (phone_num,))
    result = cur.fetchall()
    print(result)
    con.commit()


def user_choise():
    show_data()
    wish = True
    while(wish):
        print("Для поиска по справочнику 1")
        print("Для удаления из справочника 2")
        choise = input("Введите ваш выбор для продолжения: ")
        if choise != '1' or choise != '2':
            wish = False


def user_input():
    wish = True
    while(wish):
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        surname = input("Введите отчество: ")
        phone_num = input("Введите номер телефона: ")
        insert_into(first_name,last_name, surname, phone_num)
        choise = input("Введите 1 для продожения: ")
        if choise != '1':
            wish = False
    print()
    user_choise()


def show_data(): # показываем все записи таблицы users
    cur.execute("SELECT * from contacts")
    for row in cur.fetchall():
        print(row)
    con.close()


first_name = ''
last_name = ''
surname = ''
phone_num = ''

user_input()