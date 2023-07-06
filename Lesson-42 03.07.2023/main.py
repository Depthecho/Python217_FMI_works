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

import os

from sqlalchemy import or_, not_, desc, func, text
from Models.Database import DATABASE_NAME, Session
import create_database as db_creator

from Models.Students import Student
from Models.Groups import Group
from Models.Lessons import Lesson, association_table

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    # print(session.query(Lesson).all())

    # for lesson in session.query(Lesson).all():
    #     print(lesson.lesson_title, lesson.groups)

    # print(session.query(Student).count())

    # print(session.query(Student).get(4))
    # print(session.get(Student, 4))

    # for lesson in session.query(Lesson).filter(Lesson.id <= 3):
    #     print(lesson)
    #
    # for lesson in session.query(Lesson).filter(Lesson.id <= 3, Lesson.lesson_title.like('Ф%')):
    #     print(lesson) # AND
    #
    # for lesson in session.query(Lesson).filter(or_(Lesson.id <= 3, Lesson.lesson_title.like('Ф%'))):
    #     print(lesson) # OR

    # for lesson, gr in session.query(Lesson.lesson_title, Group.group_name).filter(association_table.c.lesson_id ==
    #                                                                               Lesson.id,
    #                                                                               association_table.c.group_id ==
    #                                                                               Group.id):
    #     print(lesson, gr)

    # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Физика'])).all())
    # print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Физика'])).all())

    # print(session.query(Student).filter(Student.age.between(18,19)).all())
    # print(session.query(Student).filter(Student.age.between(18,19)).count())

    # print(session.query(Student).filter(not_(Student.age.between(18,19))).all())
    # print(session.query(Student).filter(not_(Student.age.between(18, 19))).count())

    # print(session.query(Student).filter(Student.age.like('1%')).all())
    # print(session.query(Student).filter(Student.age.like('1%')).count())
    # print(session.query(Student).filter(Student.age.like('1%')).limit(4).all())
    # print(session.query(Student).filter(Student.age.like('1%')).limit(4).offset(2).all())

    # print(session.query(Student).filter(Student.age.like('1%')).order_by(desc(Student.name)).all())

    # for it in session.query(Student, Group.group_name).join(Group).all():
    #     print(it)

    # for it in session.query(Group.group_name, func.count(Student.surname)).join(Group).group_by(Group.group_name):
    #     print(it)
    # for it in session.query(Group.group_name, func.count(Student.surname)).join(Group).group_by(Group.group_name).having(func.count(Student.surname) > 25):
    #     print(it)

    # for it in session.query(Student).filter(text('surname LIKE "М%" ')):
    #     print(it)