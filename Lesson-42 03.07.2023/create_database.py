from faker import Faker
from Models.Database import create_db, Session
from Models.Students import Student
from Models.Groups import Group
from Models.Lessons import Lesson


# Функция для создания бд:
def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    lessons = ['Математика', 'Физика', 'Информатика', 'Философия', 'Линейная алгебра', 'Мат.анализ', 'Физ.культура']
    group1 = Group(group_name='Гриффиндор')
    group2 = Group(group_name='Слизерин')
    session.add(group1)
    session.add(group2)

    for key, les in enumerate(lessons):
        lesson = Lesson(lesson_title=les)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.append(group2)
        session.add(lesson)

    session.commit()
    faker = Faker('ru_RU')
    groups = [group1, group2]

    for _ in range(50):
        full_name = faker.name().split()
        age = faker.random.randint(18, 25)
        group = faker.random.choice(groups)
        student = Student(full_name, age, group.id)
        session.add(student)

    session.commit()
    session.close()


if __name__ == "__main__":
    create_database()