import sqlite3 as sq

with sq.connect('homework.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER,
                       email TEXT UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       id_user INTEGER,
                       product_name TEXT NOT NULL,
                       FOREIGN KEY (id_user) REFERENCES Users(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       price REAL,
                       quantity INTEGER CHECK (quantity >= 0))''')

    cursor.execute("INSERT INTO Users (name, age, email) VALUES (?, ?, ?)", ('Egor Egorov', 21, 'egor.egorov@gmail.com'))
    cursor.execute("INSERT INTO Users (name, age, email) VALUES (?, ?, ?)", ('Nikita Belov', 30, 'bnekit@mail.ru'))
    cursor.execute("INSERT INTO Users (name, age, email) VALUES (?, ?, ?)", ('Petr Romanov', 35, 'petroman@mail.ru'))
    cursor.execute("INSERT INTO Users (name, age, email) VALUES (?, ?, ?)", ('Anna Krugova', 27, 'annakrug@outlook.com'))

    cursor.execute("INSERT INTO Orders (id_user, product_name) VALUES (?, ?)", (1, 'Product 1'))
    cursor.execute("INSERT INTO Orders (id_user, product_name) VALUES (?, ?)", (2, 'Product 2'))
    cursor.execute("INSERT INTO Orders (id_user, product_name) VALUES (?, ?)", (3, 'Product 3'))
    cursor.execute("INSERT INTO Orders (id_user, product_name) VALUES (?, ?)", (4, 'Product 4'))

    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", ('Product 1', 9.99, 100))
    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", ('Product 2', 19.99, 50))
    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", ('Product 3', 29.99, 30))
    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", ('Product 4', 19.99, 15))

    conn.commit()

    cursor.execute('''SELECT Orders.product_name FROM Orders
                      JOIN Users ON Orders.id_user = Users.id
                      WHERE Users.name = 'Egor Egorov' ''')
    print("Заказы пользователя 'Egor Egorov':")
    for it in cursor.fetchall():
        print(it[0])

    cursor.execute('''SELECT Products.name, Users.name FROM Products
                      JOIN Orders ON Products.name = Orders.product_name
                      JOIN Users ON Orders.id_user = Users.id
                      WHERE Users.age >= 30''')
    print("\nПродукты, заказанные пользователями старше 25 лет:")
    for row in cursor.fetchall():
        print("Продукт:", row[0])
        print("Заказчик:", row[1])

    cursor.execute("UPDATE Users SET name = ?, age = ?, email = ? WHERE id = ?", ('Kylie Rebecca', 29, 'kyliestormy'
                                                                                                       '@example.com', 3
                                                                                  ))

    cursor.close()