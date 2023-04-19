from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, first_name, second_name, age, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.gender = gender

    @abstractmethod
    def work(self):
        pass


class Builder(Human):
    def __init__(self, first_name, second_name, age, gender, classification):
        Human.__init__(self, first_name, second_name, age, gender)
        self.classification = classification

    def work(self):
        print("Lets build it !")

    @property
    def classification(self):
        return self._classification

    @classification.setter
    def classification(self, string):
        self._classification = string


class Sailor(Human):
    def __init__(self, first_name, second_name, age, gender, sea_rank):
        Human.__init__(self, first_name, second_name, age, gender)
        self.rank = sea_rank

    def work(self):
        print("Lets swim !")

    @property
    def sea_rank(self):
        return self._sea_rank

    @sea_rank.setter
    def rank(self, string):
        self._sea_rank = string


class Pilot(Human):
    def __init__(self, first_name, second_name, age, gender, rank):
        Human.__init__(self, first_name, second_name, age, gender)
        self.rank = rank

    def work(self):
        print("Lets fly !")

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, string):
        self._rank = string


builder = Builder("Ivan", "ivanov", 44, "Male", "joiner")
builder.work()
builder.classification = "carpenter"
print(builder.classification)
sailor = Sailor("Nikita", "Belov", 39, "Male", "captain of the second rank")
sailor.work()
pilot = Pilot("Mikhail", "Romashkin", 31, "Male", "admiral")
pilot.work()
