import sqlite3 as sq

with sq.connect('example.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    NAME NOT NULL,
    age
    )''')