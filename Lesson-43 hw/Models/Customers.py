from sqlalchemy import Column, Integer, String
from .Database import Base


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(200))
    city = Column(String(100))

    def __repr__(self):
        return f'Customer ID: {self.id}, Name: {self.name}, Address: {self.address}, City: {self.city}'