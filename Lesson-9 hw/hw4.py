# Вам дана матричная сетка размера m x n, состоящая из положительных чисел
# Выполняйте следующую операцию, пока сетка не станет пустой
# Удалите элемент с наибольшим значением из каждой сетки
# Если существует несколько таких элементов, удалите любой из них.
# Добавьте к ответу максимальный из удаленных ответов.
# Обратите внимание, что количество столбцов уменьшается на 1 после каждой операции
# Верните ответ после выполнения операций, описанных выше:
import random

m = int(input('Введите количество строк: '))
n = int(input('Введите количество столбцов: '))

mas = [[random.randint(1, 100) for i in range(m)] for i in range(n)]

resultat = 0
Flag = True

while Flag:
    var = []
    for i in range(len(mas)):
        try:
            var.append(max(mas[i]))
            ind = mas[i].index(max(mas[i]))
            mas[i].pop(ind)
        except ValueError:
            mas.pop(i)
        except IndexError:
            Flag = False
    if var:
        resultat += max(var)

print(resultat)