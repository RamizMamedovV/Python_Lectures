import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER DEFAULT 1,
                old INTEGER,
                score INTEGER
    )
                """)



#                          for delete
# cur.execute("DROP TABLE IF EXISTS users")


#                           без with
# con = sq.connect("saper.db")
# cur = con.cursor()

# cur.execute("""
# """)

# con.close()
"""  если в части кода произойдёт ощибка, то не сработает close(), 
#  поэтому применяем контекст меньшера with тогда уже без close(), т.к. сработает 
# автоматически
"""
# for exampe:
# with sq.connect("saper.db") as con:
#     cur = con.cursor()

#     cur.execute("""
#     """)