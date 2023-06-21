import sqlite3
import sqlite3 as sq

with sqlite3.connect('example.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS cars(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Mark TEXT,
    Model TEXT,
    Price INTEGER CHECK ( Price >= 800 and Price <= 1200)
    )''')
    cur.execute('''INSERT INTO cars
    VALUES(1, 'Nissan', 'Qushkai', 900)''')
    cur.execute('''INSERT INTO cars
        VALUES(2, 'Nissan2', 'Qushkai2', 1000)''')
    cur.execute('''INSERT INTO cars
        VALUES(3, 'Nissan3', 'Qushkai3', 800)''')
    cur.execute('''INSERT INTO cars
        VALUES(4, 'Nissan4', 'Qushkai4', 1200)''')
    cur.execute('''INSERT INTO carS
        VALUES(5, 'Nissan5', 'Qushkai5', 1100)''')
