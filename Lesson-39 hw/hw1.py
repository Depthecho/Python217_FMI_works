# 1
# SELECT COUNT(DISTINCT INNClient) AS TotalClients
# FROM ClientGoods

# 2
# SELECT COUNT(DISTINCT sg.INNSeller) AS TotaSellers
# FROM SallerGoods sg

# 3
# SELECT Goods, AVG(CostUnit * Count) AS AverageAmount
# FROM SallerGoods
# GROUP BY Goods

# 4
# SELECT SUM(CostUnit * Count) AS TotalAmount
# FROM SallerGoods

# 5
# SELECT MAX(cg.Count) AS MaxCount
# FROM ClientGoods cg, SallerGoods sg
# WHERE cg.ID = sg.ID

# 6
# SELECT MIN(cg.CostUnit * cg.Count) AS MinAmount
# FROM ClientGoods cg, SallerGoods sg
# WHERE cg.ID = sg.ID

# 7
# SELECT SUM(cg.CostUnit * cg.Count) AS TotalSalesAmount
# FROM ClientGoods cg, Client c, SallerGoods sg
# WHERE c.Status == 'магазин' AND sg.ID = cg.ID AND c.INNClient = cg.INNClient

# 8
# SELECT COUNT(DISTINCT sg.Goods) AS TotalWaffleTypes
# FROM SallerGoods sg
# WHERE sg.Goods LIKE 'Вафли%'

# 9
# SELECT AVG(sg.CostUnit) AS AveragePurchasePrice
# FROM SallerGoods sg
# WHERE sg.Goods LIKE 'масло%'

# 10
# SELECT SUM(sg.Count) AS TotalApplesSold
# FROM SallerGoods sg, ClientGoods cg
# WHERE sg.Goods LIKE 'Яблоки%' AND cg.ID = sg.ID

# 11
# SELECT SUM(sg.Count) AS TotalPotatoPrice
# FROM SallerGoods sg, ClientGoods cg, Client c
# WHERE c.Status LIKE 'кафе%' AND c.INNClient = cg.INNClient AND cg.ID = sg.ID

# 12
# SELECT COUNT(DISTINCT cg.INNClient) AS TotalClients
# FROM SallerGoods sg, ClientGoods cg, Client c
# WHERE c.INNClient = cg.INNClient AND cg.ID = sg.ID AND sg.Goods LIKE 'Перец черный%'

# 13
# SELECT COUNT(DISTINCT sg.Goods) AS CountDistGoods
# FROM SallerGoods sg, ClientGoods cg, Seller s
# WHERE cg.ID = sg.ID AND s.Status = 'посредник'

# 14
# SELECT MIN(cg.CostUnit) AS MinPrice
# FROM SallerGoods sg, ClientGoods cg
# WHERE cg.ID = sg.ID

# 15
# SELECT MIN(cg.CostUnit*cg.Count) AS MinPrice
# FROM SallerGoods sg, ClientGoods cg
# WHERE cg.ID = sg.ID

# 16
# SELECT MAX(cg.CostUnit*cg.Count) AS MinPrice
# FROM SallerGoods sg, ClientGoods cg, Client c
# WHERE cg.ID = sg.ID AND c.Status = 'магазин'

# 17
# SELECT COUNT(DISTINCT cg.INNClient) AS TotalFirms
# FROM ClientGoods cg, SallerGoods sg
# WHERE INNSeller = 1564 AND cg.ID = sg.ID

# 18
# SELECT MIN(cg.CostUnit*cg.Count) AS MinPrice
# FROM SallerGoods sg, ClientGoods cg, Seller s
# WHERE cg.ID = sg.ID AND s.Status = 'производитель'

# 19
# SELECT AVG(cg.CostUnit) AS AvgTeaPrice
# FROM SallerGoods sg, ClientGoods cg
# WHERE cg.ID = sg.ID AND sg.Goods LIKE 'Чай%'

# 20
# SELECT MAX(cg.CostUnit*cg.Count) AS MaxPrice
# FROM SallerGoods sg, ClientGoods cg, Client c
# WHERE cg.ID = sg.ID AND c.Status = 'посредник'

# 21
# SELECT MIN(cg.CostUnit*cg.Count) AS MaxPrice
# FROM SallerGoods sg, ClientGoods cg, Seller s
# WHERE cg.ID = sg.ID AND s.Status = 'посредник'

# 22
# SELECT COUNT(DISTINCT sg.Goods) AS TotalProducts
# FROM ClientGoods cg, SallerGoods sg
# WHERE cg.INNClient = 2054 AND cg.ID = sg.ID

# 23
# SELECT COUNT(DISTINCT Goods) AS TotalCookieTypes
# FROM SallerGoods
# WHERE Goods LIKE 'Печенье%'

# 24
# SELECT MAX(cg.CostUnit* cg.Count) AS MaxPurchasePrice
# FROM SallerGoods sg, ClientGoods cg
# WHERE sg.ID = cg.ID

# 25
# SELECT AVG(sg.CostUnit* sg.Count - cg.CostUnit*cg.Count) AS AvgIncome
# FROM SallerGoods sg, ClientGoods cg
# WHERE sg.ID = cg.ID AND sg.Goods LIKE 'Чай%'

# 26
# SELECT COUNT(DISTINCT cg.INNClient) AS TotalIntermediary
# FROM SallerGoods sg, ClientGoods cg, Seller s
# WHERE sg.ID = cg.ID AND s.Status = 'посредник' AND cg.INNClient = 2020

# Если честно, то очень много заданий не понимал и надеюсь, что сделал большинство правильно
