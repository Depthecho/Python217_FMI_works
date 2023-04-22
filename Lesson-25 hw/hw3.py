# Вам необходимо создать класс Airplane (самолет). С помощью перегрузки операторов реализовать:
# Проверка на равенство типов самолетов (операция = =);
# Увеличение и уменьшениепа ссажиров в салоне самолета (операции +, -, +=, -=)
# Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >, <, <=, >=).

class Airplane:
    def __init__(self, type_of_plane, max_passengers, current_passengers):
        self.type_of_plane = type_of_plane
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.type_of_plane == other.type_of_plane

    def __add__(self, num_passengers):
        if self.current_passengers + num_passengers > self.max_passengers:
            print("Не хватает мест для пассажиров !!")
        else:
            self.current_passengers += num_passengers
        return self

    def __sub__(self, num_passengers):
        if self.current_passengers - num_passengers < 0:
            print("Количество пассажиров не может быть меньше 0!")
        else:
            self.current_passengers -= num_passengers
        return self

    def __iadd__(self, num_passengers):
        return self.__add__(num_passengers)

    def __isub__(self, num_passengers):
        return self.__sub__(num_passengers)

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers


ap1 = Airplane("1", 500, 100)
ap2 = Airplane("2", 200, 0)
print(ap1 == ap2)

ap1 += 100
print(ap1.current_passengers)

ap2 -= 50
print(ap2.current_passengers)

ap1 += 150
print(ap1 > ap2)
print(ap1 <= ap2)