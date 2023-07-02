# import sqlite3 as sq
#
# # cars = [
# #     ('Pejo', 1700),
# #     ('Subaru', 1800),
# #     ('Mazda', 1900),
# #     ('Nissan', 1800),
# #     ('Ford', 1500)
# # ]
#
# cars = [
#     ('Ford', 1700),
#     ('Lada', 1800),
#     ('KIA', 1900),
#     ('Honda', 1800),
#     ('Hyondai', 1700)
# ]
#
# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     # Добавление даннных в таблицу
#     cur.execute('CREATE TABLE IF NOT EXISTS Cars('
#                 'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
#                 'Model TEXT NOT NULL,'
#                 'Price INTEGER CHECK(price >= 0)'
#                 ')')
# cur.execute('INSERT INTO cars VALUES( NULL,"Tesla", 2000)')
# cur.execute('INSERT INTO cars VALUES( NULL,"Toyota", 1700)')
# cur.execute('INSERT INTO cars VALUES( NULL,"BMW", 2200)')
# cur.execute('INSERT INTO cars VALUES( NULL,"Renault", 1800)')
# cur.execute('INSERT INTO cars VALUES( NULL,"Ferrari", 3500)')
# import sqlite3
# for i in range(5):
#     cur.execute(f'INSERT INTO Cars VALUES(NULL, "{cars[i][0]}", {cars[i][1]})')

# cur.executemany(f'INSERT INTO cars VALUES(NULL, ?, ?)', cars)

# Вывод данных с таблицы
# cur.execute('SELECT * '
#             'FROM cars')
# print(cur.fetchall())
# # Вывод первого вхождения с таблицы
# cur.execute('SELECT model '
#             'FROM cars '
#             'WHERE Price >= 1900')
# print(cur.fetchone())

# Выполнение нескольких операций в одном скрипте
# try:
#      cur.executescript('BEGIN; '
#                        'UPDATE cars SET price = price +100; '
#                        'CREATE TABLE IF NOT EXISTS expensive_cars('
#                        'car_ID INTEGER PRIMARY KEY AUTOINCREMENT,'
#                        'Model TEXT NOT NULL,'
#                        'price INTEGER'
#                        ');'
#                        'INSERT INTO expensive_cars '
#                        'SELECT * '
#                        'FROM cars '
#                        'WHERE price >= 2000')
# except sq.Error as e:
#      print(f'При выполнении операций произошла ошибка: {e}')
#      if con:
#          con.rollback() # Команда для отката изменений
# else:
#     if con:
#         con.commit() # Команда для сохранения изменений


import sqlite3 as sq

with sq.connect('db_9.db') as con:
    cur = con.cursor()
    cur.execute('')
