import sqlite3 as sq


# def read_avatar(n):
#     try:
#         with open(f'Avatars/{n}.png', 'rb') as file:
#             return file.read()
#     except IOError as e:
#         print(e)
#         return None
#
#
# def write_avatar(filepath, data):
#     try:
#         with open(filepath, 'wb') as file:
#             file.write(data)
#             return True
#     except IOError as e:
#         print(e)
#         return False
#
#
# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#    cur.row_factory = sq.Row  # Смена представления данных из бд (в данном случае sq..Row позволяет получать к ним
#    # доступ по названию свойств (столбцов)
#    cur.execute('''SELECT model, price FROM cars''')
#    for car in cur:
#        print(car['model'], car['price'])
#       Создание таблицы для пользователей
#    cur.execute('''CREATE TABLE IF NOT EXISTS users(
#    User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#    Avatar BLOB,
#    Name TEXT
#    )''')
#       Запись данных с картинкой в бд:
#    img = read_avatar('Avatar1')
#    sql_img = sq.Binary(img)
#    cur.execute('''INSERT INTO users VALUES(NULL, ?, ?)''', (sql_img, 'Vasiliy'))
#
#    Чтение картинки из бд и запись в файл:
#    cur.execute('''SELECT Avatar FROM users LIMIT 1''')
#    img = cur.fetchone()[0]
#    write_avatar('out.png', img)
#       Создания файла бэкапа, который содержит скрипт для воссоздания бд
#    with open('cars_backup.sql', 'w') as f:
#        for i in con.iterdump():
#            f.write(f'{i}\n')
#       Выполнение срипта для восстановления бд
#    sql_script = open('cars_backup.sql').read()
#   cur.executescript(sql_script)

# Бд внутри оперативной памяти
# with sq.connect(':memory:') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users(
#     User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     Avatar BLOB,
#     Name TEXT
#     )''')
#     cur.executemany('''INSERT INTO users VALUES(NULL, ?, ?)''', [(i, i*2) for i in range(10000)])
#     cur.execute('''SELECT * FROM users''')
#     print(cur.fetchall())
