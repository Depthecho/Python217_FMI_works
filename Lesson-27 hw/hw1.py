# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип списка нужно
# выбрать в зависимости от поставленной ниже задачи). После чего нужно показать меню, в котором предложить пользователю
# набор пунктов...

class ListHandler:
    def __init__(self, lst):
        self.lst = lst

    def add_element(self, element):
        if element in self.lst:
            print("Such a number already exists in the list")
        else:
            self.lst.append(element)

    def remove_element(self, element):
        if element in self.lst:
            self.lst[:] = [el for el in self.lst if el != element]
            print(f"Number {element} removed from the list")
        else:
            print(f"Number {element} is not in the list")

    def show_list(self):
        print(self.lst)

    def check_value(self, element):
        if element in self.lst:
            print(f"Number {element} already exists in the list")
        else:
            print(f"Number {element} is not in the list")

    def replace_value(self, original_element, new_element):
        if original_element in self.lst:
            index = self.lst.index(original_element)
            self.lst[index] = new_element
        else:
            print(f"Number {original_element} is not in the list")


numbers = []

while True:
    handler = ListHandler(numbers)
    print("""Меню:
1. Add a new number to the list
2. Remove occurrences of a number from the list
3. Show the contents of the list
4. Check if there is a value in the list
5. Replace the value in the list
6. Exit""")

    choice = input("Enter your command: ")

    if choice == "1":
        element = int(input("Enter your number: "))
        handler.add_element(element)

    elif choice == "2":
        element = int(input("Enter the number to remove: "))
        handler.remove_element(element)

    elif choice == "3":
        handler.show_list()

    elif choice == "4":
        element = int(input("Enter a number to check: "))
        handler.check_value(element)

    elif choice == "5":
        original_element = int(input("Enter the number to replace: "))
        new_element = int(input("Enter new number: "))
        handler.replace_value(original_element, new_element)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Wrong command. Try again.")
