from sqlalchemy import Column, Integer, String, ForeignKey
from .Database import Base


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Integer)
    sale_date = Column(String(50))
    payment_status = Column(String(20))

    def __repr__(self):
        return f'Sale ID: {self.id}, Salesman ID: {self.salesman_id}, Customer ID: {self.customer_id}, Amount:' \
               f' {self.amount}, Sale Date: {self.sale_date}, Payment Status: {self.payment_status}'