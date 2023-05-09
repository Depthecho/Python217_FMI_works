# Тот же стк из 2-го задания, только нефиксированный

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


stack = Stack()

while True:
    print("""Menu:
    1. Push a string into the stack
    2. Pop a string from the stack
    3. Count the number of strings in the stack
    4. Check if the stack is empty
    5. Clear the stack
    6. Peek the top string value of the stack
    7. Exit""")

    choice = input("Enter your commandr: ")

    if choice == "1":
        item = input("Enter the string to push: ")
        stack.push(item)

    elif choice == "2":
        item = stack.pop()
        if item is not None:
            print("Popped string:", item)
        else:
            print("Stack is empty, can't pop any string")

    elif choice == "3":
        count = stack.count()
        print(f"There are {count} strings in the stack")

    elif choice == "4":
        if stack.is_empty():
            print("The stack is empty")
        else:
            print("The stack is not empty")

    elif choice == "5":
        stack.clear()
        print("The stack is cleared")

    elif choice == "6":
        item = stack.peek()
        if item is not None:
            print("The top string value of the stack:", item)
        else:
            print("Stack is empty, no string on top")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Wrong command. Try again.")
