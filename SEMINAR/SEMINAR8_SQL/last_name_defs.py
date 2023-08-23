import sqlite3 as sq

with sq.connect("phone_book.db") as con:
    cur = con.cursor()


def show_data_l_name(last_name: str):
    query = "SELECT * FROM contacts WHERE last_name = ?"
    cur.execute(query, (last_name,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_l_s_name(last_name: str, surname: str):
    query = "SELECT * FROM contacts WHERE last_name = ? AND surname = ?"
    cur.execute(query, (last_name, surname,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_l_name_p_num(last_name: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE last_name = ? AND phone_num = ?"
    cur.execute(query, (last_name, phone_num,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_l_s_name_p_num(last_name: str, surname: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE last_name = ? AND surname = ? AND phone_num = ?"
    cur.execute(query, (last_name, surname, phone_num))
    result = cur.fetchall()
    print(result)
    con.commit()