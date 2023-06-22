# 1
# SELECT Produce
# FROM Ware
# WHERE ID_salespeople  IS NULL

# 2
# SELECT REM, ID, Country
# FROM Ware
# WHERE Country = 'Украина'

# 3
# DELETE
# FROM Ware
# WHERE Country = 'Германия'

# 4
# UPDATE Ware
# SET Country = 'Россия'
# WHERE Country = 'Польша'

# 5
# Пришлось создавать копию 1ой таблицы, чтобы оттуда вставлять данные, иначе никак не придумал (
# INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM)
# SELECT ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM
# FROM Ware2
# WHERE Country = 'Германия'

# 6
# SELECT Produce, Price, ID
# FROM Ware
# WHERE Color != 'ч'

# 7
# INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM)
# VALUES (1046, 'NTC-117BK', 'нейлон', 'ч', '13,3x8,3x5', 'Украина', 2016, 321, 0, 'Micro Camera Case')

# 8
# Тоже какие-то сомнения, ибо в задании было написано, что ID не определён, а он является обязательным ключом, поэтому
# добавил свой
# INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM)
# VALUES (1206, ' POC-463BK', 'полиэстер', 'ч', '11x7x4,5', NULL, NULL, NULL, NULL, 'Compact Camera Case')

# 9
# SELECT *
# FROM Ware
# WHERE Country = 'Россия' AND ID_salespeople = 2065

# 10
# SELECT Produce
# FROM Ware
# WHERE Price BETWEEN 200 AND 345

# 11
# SELECT *
# FROM Ware
# WHERE Material = 'кожа' AND Size >= '40x30x5'

# 12
# SELECT Produce, ID_salespeople
# FROM Ware
# WHERE Price*Count < 1200

# 13
# UPDATE Ware
# SET ID_salespeople = 2000
# WHERE Price*Count < 500

# 14
# SELECT *
# FROM Ware
# WHERE Material = 'кожа' AND Count < 5 AND (Price * Count) <= 450

# 15
# SELECT *
# FROM Ware
# WHERE Material = 'нейлон' AND Price <= 250

# 16
# UPDATE Ware
# SET Material = 'брезент'
# WHERE Material = 'нейлон' AND Price <= 200

# 17
# SELECT *
# FROM Ware
# WHERE REM LIKE '%косметичка'

# 18
# SELECT *
# FROM Ware
# WHERE Material = 'кожа' AND Color = 'ч' AND Country = 'Китай'

# 19
# Не особо понял задание :(
# SELECT *
# FROM Ware
# WHERE Size > 15

# 20
# SELECT DISTINCT ID_salespeople
# FROM Ware
# WHERE Color != 'черный'

# 21
# UPDATE Ware
# SET Material = 'нейлон'
# WHERE Country = 'Китай' AND Material = 'полиэстер'

# 22
# UPDATE Ware
# SET Material = 'полиэстер'
# WHERE Country = 'Китай' AND ID IN (1015, 1041, 1032, 1010) AND Material = 'нейлон'