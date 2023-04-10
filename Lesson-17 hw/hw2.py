# Написать программу «успеваемость». Пользователь вводит 10 оценок студента. Оценки от 1 до 12. Реализовать меню
# для пользователя

import random

grades = [random.randint(1, 12) for i in range(10)]
print(grades)

while True:
    print(f"\nMenu:")
    print(f"1. Display the score.")
    print(f"2. Retake the exam.")
    print(f"3. Scholarship Verification.")
    print(f"4. Sort the list.")
    print(f"5. Exit.")
    choice = int(input("Select a menu item: "))

    if choice == 1:
        print(f"Student's grades: {grades}")
    elif choice == 2:
        index = int(input("Enter number of grade: "))
        grade = int(input("Enter new grade: "))
        grades[index - 1] = grade
        print(f"Grade {index} changed to {grade}")
    elif choice == 3:
        average = sum(grades) / len(grades)
        if average >= 10.7:
            print(f"The student will receive a scholarship.")
        else:
            print(f"the student will not receive a scholarship.")
    elif choice == 4:
        sort_order = input(f"Enter \"1\" to sort the list in ascending order or \"2\" to sort in descending order: ")
        if sort_order == "1":
            grades.sort()
            print(f"Sorted grades: {grades}.")
        elif sort_order == "2":
            grades.sort(reverse=True)
            print(f"Sorted grades: {grades}.")
        else:
            print(f"Wrong sort order: {sort_order}.")
    elif choice == 5:
        print(f"Exit.")
        break
    else:
        print(f"Wrong input!")