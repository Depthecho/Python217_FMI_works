# Определение словаря
my_dictionary = {'apple': 'a fruit', 'carrot': 'a vegetable', 'python': 'a programming language'}

# Определение функций для работы со словарём
def find_definition(word):
    if word in my_dictionary:
        return my_dictionary[word]
    else:
        return None

# Создание пользовательского интерфейса
from tkinter import *

root = Tk()

entry = Entry(root)
entry.pack()

text = Text(root)
text.pack()

def search():
    word = entry.get()
    definition = find_definition(word)
    if definition:
        text.delete(1.0, END)
        text.insert(END, definition)
    else:
        text.delete(1.0, END)
        text.insert(END, "Word not found.")

button = Button(root, text="Search", command=search)
button.pack()

root.mainloop()







choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(display_all_sales(), filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')

