from sqlalchemy import Column, Integer, String
from .Database import Base


class Salesman(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    contact_number = Column(String(20))
    email = Column(String(100))

    def __repr__(self):
        return f'Salesman ID: {self.id}, Name: {self.name}, Contact Number: {self.contact_number}, Email: {self.email}'