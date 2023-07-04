from sqlalchemy import Column, Integer, String, ForeignKey
from .Database import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    patronymic = Column(String(100), nullable=False)
    age = Column(Integer)
    group = Column(Integer, ForeignKey("groups.id"))

    def __init__(self, full_name, age, group_id):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.group = group_id

    def __repr__(self):
        return f'Student: {self.surname} {self.name} {self.patronymic}, ' \
                f'Age: {self.age}, ' \
                f' Id of group: {self.group}'
