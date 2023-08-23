import sqlite3 as sq

with sq.connect("phone_book.db") as con:
    cur = con.cursor()



def show_data_s_name(surname: str):
    query = "SELECT * FROM contacts WHERE surname = ?"
    cur.execute(query, (surname,))
    result = cur.fetchall()
    print(result)
    con.commit()


def show_data_s_name_p_num(surname: str, phone_num: str):
    query = "SELECT * FROM contacts WHERE surname = ? AND phone_num = ?"
    cur.execute(query, (surname, phone_num,))
    result = cur.fetchall()
    print(result)
    con.commit()