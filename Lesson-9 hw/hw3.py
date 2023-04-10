# Вам дана сетка row X col, представляющая карту
# Где grid[i][j] = 1 представляет землю,
# a grid [i][j] = 0 представляет воду.
# Ячейки сетки соединены по горизонтали/вертикали ( не по диагонали).
# Сетка полностью окружена водой и на ней ровно один остров (т.е. одна или несколько соединённых ячеек суши)
# На острове нет озёр, т.е. вода внутри не связана с водой вокруг острова. Одна ячейка представляет собой квадрат
# со сторонами 1. Сетка прямоугольная, ширина и высота не превышают 100.
# Определить периметр острова:

import random

row = int(input('Введите количество строк: '))
col = int(input('Введите количество столбцов: '))

grid = [[random.randint(0, 1) for _ in range(col)] for _ in range(row)]

def islandPerimeter(grid):
    # Находим начальную ячейку суши
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                start_i, start_j = i, j
                break

    # Определяем соседние ячейки для текущей ячейки
    def get_neighbors(i, j):
        neighbors = []
        if i > 0 and grid[i - 1][j] == 1:
            neighbors.append((i - 1, j))
        if i < len(grid) - 1 and grid[i + 1][j] == 1:
            neighbors.append((i + 1, j))
        if j > 0 and grid[i][j - 1] == 1:
            neighbors.append((i, j - 1))
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
            neighbors.append((i, j + 1))
        return neighbors

    # Инициализируем список обрабатываемых ячеек
    queue = [(start_i, start_j)]
    processed = set(queue)

    # Инициализируем периметр острова
    perimeter = 0

    # Обрабатываем все ячейки в списке
    while queue:
        i, j = queue.pop(0)
        neighbors = get_neighbors(i, j)
        for neighbor in neighbors:
            if neighbor not in processed:
                queue.append(neighbor)
                processed.add(neighbor)
            else:
                # Если соседняя ячейка уже была обработана, то это значит, что
                # она находится внутри острова и не является граничной ячейкой
                continue
        # Добавляем длину граничных ячеек в периметр острова
        perimeter += 4 - len(neighbors)

    print(perimeter)
    return perimeter

islandPerimeter(grid)


# Задача оооочень сложная, чуть мозг не сломал, пока делал
# Да и кажется, что сделал будто неправильно))
