import sqlite3 as sq

with sq.connect("phone_book.db") as con:    
    cur = con.cursor()

def show_data_f_name(first_name: str):
    query = "SELECT * FROM contacts WHERE first_name = ?"
    cur.execute(query, (first_name,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_f_l_name(first_name: str, last_name: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND last_name = ?"
    cur.execute(query, (first_name, last_name,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_f_s_name(first_name: str, surname: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND surname = ?"
    cur.execute(query, (first_name, surname,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_f_name_p_num(first_name: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND phone_num = ?"
    cur.execute(query, (first_name, phone_num,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_f_l_s_name(first_name: str, last_name: str, surname: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND last_name = ? AND surname = ?"
    cur.execute(query, (first_name, last_name, surname))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_f_l_name_p_num(first_name: str, last_name: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND last_name = ? AND phone_num = ?"
    cur.execute(query, (first_name, last_name, phone_num))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_f_s_name_p_num(first_name: str, surname: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE first_name = ? AND surname = ? AND phone_num = ?"
    cur.execute(query, (first_name, surname, phone_num))
    result = cur.fetchall()
    print(result)
    con.commit()