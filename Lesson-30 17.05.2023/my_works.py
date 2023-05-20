import json
from ast import literal_eval


class WorkWithArray:
    def __init__(self, array):
        self.array = array

    def show_array_on_screen(self):
        print(self.array)

    def show_array_reverse_on_screen(self):
        print(self.array[-1::-1])

    def show_array_in_file(self, filename, reverse=False):
        if reverse:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.array[-1::-1], f)
        else:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.array, f)

    def get_max(self):
        print(max(self.array))
        return max(self.array)

    def get_min(self):
        print(min(self.array))
        return min(self.array)


if input('Вы хотите вывести свой список на экран или в файл?\n').lower() == 'файл':
    my_file_name = input('Введите название файла: ')
    my_list = WorkWithArray(literal_eval(input('Введите массив чисел: ')))
    if input('Хотите ли вы перевернуть список?').lower() == 'да':
        my_list.show_array_in_file(my_file_name, reverse=True)
    else:
        my_list.show_array_in_file(my_file_name)
    my_list.get_max()
else:
    my_list = WorkWithArray(literal_eval(input('Введите числа массив: ')))
    if input('Хотите ли вы перевернуть список?').lower() == 'да':
        my_list.show_array_reverse_on_screen()
    else:
        my_list.show_array_on_screen()
        my_list.get_min()

print("================================================================================================")


class Student():
    def __init__(self, name, age, gender, group):
        self.name = name
        self.age = age
        self.gender = gender
        self.group = group

    def __str__(self):
        return f"Имя ученика:{self.name}, возраст: {self.age}, пол: {self.gender}, группа: {self.group}"


class Group:
    def __init__(self, group_id):
        self.group_id = group_id
        self.students = []

    def __iter__(self):
        return GroupIterator(self.students)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                print(student)
                return student

    def update_student(self, name, age=None, gender=None, group=None):
        student = self.get_student(name)
        if student:
            if age is not None:
                student.age = age
            if gender is not None:
                student.gender = gender
            if group is not None:
                student.group = group
        else:
            print(f"Student {name} not found")


class GroupIterator:
    def __init__(self, students):
        self.students = students
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index >= len(self.students):
            self.index = -1
            raise StopIteration()
        student = self.students[self.index]
        return student


student1 = Student("Миша", 20, "М", "Группа 1")
student2 = Student("Лёша", 21, "М", "Группа 1")
student3 = Student("Гриша", 22, "М", "Группа 2")
student4 = Student("Гоша", 23, "М", "Группа 2")
student5 = Student("Саша", 24, "М", "Группа 2")

group_one = Group(group_id=1)
group_one.add_student(student1)
group_one.add_student(student2)
for students in group_one:
    print(students)

print("----------------------")

group_two = Group(group_id=2)
group_two.add_student(student3)
group_two.add_student(student4)
group_two.add_student(student5)
for students in group_two:
    print(students)
print("----------------------")
group_two.get_student('Гоша')
print("----------------------")
group_two.remove_student(student5)
for students in group_two:
    print(students)