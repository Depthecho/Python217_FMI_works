# 1.
# SELECT DISTINCT CITY2
# FROM ZAKAZ

# 2.
# SELECT DISTINCT CITY
# FROM ZAKAZ

# 3.
# SELECT *
# FROM ZAKAZ
# WHERE KOD = 1005

# 4.
# SELECT *
# FROM ZAKAZ
# WHERE RATING > 380

# 5.
# SELECT *
# FROM ZAKAZ
# WHERE REM IS NULL

# 6.
# SELECT KOD
# FROM ZAKAZ
# WHERE SUM > 4000

# 7
# SELECT *
# FROM ZAKAZ
# WHERE SUM < 1000 AND CITY != 'Иркутск'

# 8.
# SELECT *
# FROM ZAKAZ
# WHERE RATING > 100 AND RATING < 270

# 9.
# SELECT NAME, KOD, CITY
# FROM ZAKAZ
# WHERE CITY != CITY2

# 10.
# SELECT KOD
# FROM ZAKAZ
# WHERE RATING > 200 OR RATING > 350

# 11.
# SELECT NAME, PROD
# FROM ZAKAZ
# WHERE PROD = 'столы обеденные'

# 12.
# SELECT NAME
# FROM ZAKAZ
# WHERE NAME LIKE "%a%a%"

# 13.
# SELECT NAME, KOD
# FROM ZAKAZ
# WHERE NAME LIKE 'K%'

# 14.
# SELECT NAME
# FROM ZAKAZ
# WHERE CITY2 = 'Химки' AND PROD = 'стулья'

# 15.
# SELECT *
# FROM ZAKAZ
# WHERE CITY2 = 'Химки' AND CITY = 'Химки' AND SUM BETWEEN 1000 AND 1750

# 16
# SELECT KOD
# FROM ZAKAZ
# WHERE PROD IS NOT 'сейфы'

# 17.
# SELECT CNUM, PROD
# FROM ZAKAZ
# WHERE PROD == 'диваны' AND SUM > 4000

# 18.
# SELECT NAME
# FROM ZAKAZ
# WHERE PROD == 'стулья' AND SUM > 1200

# 19.
# SELECT NAME
# FROM ZAKAZ
# WHERE CITY != 'Иркутск' AND RATING > 200

# 20.
# SELECT NAME
# FROM ZAKAZ
# WHERE REM LIKE '%льготная доставка'

# 21.
# SELECT NAME
# FROM ZAKAZ
# WHERE SUM > 14000 AND CITY != 'Москва' AND CITY != 'Липецк'