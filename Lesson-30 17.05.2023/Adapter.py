# Представим, что у нас есть телевизор,
# картинку с которого мы хотим пускать
# на экран. И к нему подключены два устройства:
# игровая консоль и антенна. Но у обоих устройств
# разные функции для получения картинки.
# Таким образом, вариантом решения такой задачи
# может быть добавление классов адаптеров,
# которые бы "адаптировали" разные интерфейсы
# взаимодействия к одному стандарту.

# Игровая консоль
class GameConsole:
    def create_game_picture(self):
        return 'picture from console'


# Антенна
class Antenna:
    def create_wave_picture(self):
        return 'picture from wave'


# Адаптер игровой консоли
class SourceGameConsole(GameConsole):
    def get_picture(self):
        return self.create_game_picture()


# Адаптер антенны
class SourceAntenna(Antenna):
    def get_picture(self):
        return self.create_wave_picture()


# Адаптеры в свою очередь берут на себя перевод
# разных интерфейсов: create_game_picture и
# create_wave_picture и приводят их к одному:
# get_picture.

# Наш телевизор, который просто принимает источник
# в виде адаптера и спокойно вызывает теперь уже общий
# интерфейс в виде get_picture()
class TV:
    def __init__(self, source):
        self.source = source

    def set_source(self, new_source):
        self.source = new_source

    def show_picture(self):
        return self.source.get_picture()


g = SourceGameConsole()
a = SourceAntenna()
tv = TV(g)
print(tv.show_picture())
tv.set_source(a)
print(tv.show_picture())
