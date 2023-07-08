from faker import Faker
from Models.Database import create_db, Session
from Models.Sales import Sale
from Models.Salesmen import Salesman
from Models.Customers import Customer
from random import randint


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    faker = Faker()

    for _ in range(10):
        name = faker.name()
        contact_number = faker.phone_number()
        email = faker.email()
        salesman = Salesman(name=name, contact_number=contact_number, email=email)
        session.add(salesman)

    for _ in range(20):
        name = faker.name()
        address = faker.address()
        city = faker.city()
        customer = Customer(name=name, address=address, city=city)
        session.add(customer)

    salesmen = session.query(Salesman).all()
    customers = session.query(Customer).all()
    for _ in range(50):
        salesman = faker.random.choice(salesmen)
        customer = faker.random.choice(customers)
        amount = randint(100, 1000)
        sale = Sale(salesman_id=salesman.id, customer_id=customer.id, amount=amount)
        session.add(sale)

    session.commit()
    session.close()


if __name__ == "__main__":
    create_database()