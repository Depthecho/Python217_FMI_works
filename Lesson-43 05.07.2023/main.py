from jinja2 import Template

# student_name = 'Иван'
# student_age = 20
# person = {
#     'name': 'Иван',
#     'age': 20
# }
# tm = Template('Меня зовут {{ p["name"] }} и мне {{ p.age }} лет')
# msg = tm.render(p=person)
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#
# person = Person('Иван', 20)
# tm = Template('Меня зовут {{ p.get_name() }} и мне {{ p.age }} лет')
# msg = tm.render(p=person)
# print(msg)
#
# data = """{% raw %} Модуль Jinja вместо
# определения {{name}}
# подставит соответствующее значение {% endraw %}"""
#
# tm = Template(data)
# msg = tm.render(name='Игорь')
# print(msg)
#
# link = """В HTML документе ссылка определяется как:
# <a href = '#'>Ссылка</a>"""
# tm = Template("{{ Link | e }}")
# msg = tm.render(Link=link)
# print(msg)
