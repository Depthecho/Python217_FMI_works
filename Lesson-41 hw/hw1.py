# 1
# SELECT DISTINCT Klient.ID_KL, Klient.Name_KL, Klient.City_KL, Zakaz.ID_Z, Zakaz.SUMMA
# FROM Klient
# JOIN Zakaz ON Klient.ID_KL = Zakaz.ID_KL

# 2
# SELECT k.Name_KL, AVG(z.Cena_Dostavki) AS AverageDeliveryPrice,
#   (
#     SELECT AVG(Cena_Dostavki) AS AvgDeliveryPrice
#     FROM Zakaz
#   ) AS OverallAvgDeliveryPrice,
#   CASE
#     WHEN AVG(z.Cena_Dostavki) > (
#       SELECT AVG(Cena_Dostavki) AS AvgDeliveryPrice
#       FROM Zakaz
#     ) THEN 'Lot'
#     ELSE 'Few'
#   END AS DeliveryStatus
# FROM Klient k
# INNER JOIN Zakaz z ON k.ID_KL = z.ID_KL
# GROUP BY k.Name_KL

# 3
# SELECT *
# FROM Prodaves p
# LEFT JOIN Klient k ON p.ID_Pr = k.ID_Pr
# LEFT JOIN Zakaz z ON p.ID_Pr = z.ID_Pr AND k.ID_KL = z.ID_KL

# 4
# SELECT p.Name_Pr, k.Name_KL, k.Discoun
# FROM Prodaves p
# JOIN Klient k ON p.ID_Pr = k.ID_Pr

# 5
# SELECT City_Pr AS City FROM Prodaves
# UNION
# SELECT City_KL AS City FROM Klient

# 6
# SELECT k.Name_KL, z.ID_Z, z.DATA, z.SUMMA
# FROM Klient k
# LEFT JOIN Zakaz z ON k.ID_KL = z.ID_KL
# WHERE DATE(z.DATA) >= '1996-10-04' AND DATE(z.DATA) <= '1996-10-07'

# 7
# SELECT Name_Pr, ID_Pr
# FROM Prodaves
# WHERE City_Pr IN (
#   SELECT DISTINCT City_KL
#   FROM Klient
# ) AND ID_Pr NOT IN (
#   SELECT DISTINCT ID_Pr
#   FROM Klient
# )

# 8
# SELECT City_Pr AS City, Name_Pr AS Name
# FROM Prodaves
# WHERE City_Pr = 'London'
# UNION
# SELECT City_KL AS City, Name_KL AS Name
# FROM Klient
# WHERE City_KL = 'London'