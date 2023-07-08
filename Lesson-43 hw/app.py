from Models.Database import create_db, Session
from Models.Sales import Sale
from Models.Salesmen import Salesman
from Models.Customers import Customer
from sqlalchemy import func


def display_all_sales():
    session = Session()
    sales = session.query(Sale).all()
    for sale in sales:
        print(sale)
    session.close()
    return sales


def display_sales_by_salesman(salesman_id):
    session = Session()
    sales = session.query(Sale).filter(Sale.salesman_id == salesman_id).all()
    for sale in sales:
        print(sale)
    session.close()
    return sales


def display_max_sale_by_salesman(salesman_id):
    session = Session()
    max_sale = session.query(Sale).filter(Sale.salesman_id == salesman_id).order_by(Sale.amount.desc()).first()
    print(max_sale)
    session.close()
    return max_sale


def display_min_sale_by_salesman(salesman_id):
    session = Session()
    min_sale = session.query(Sale).filter(Sale.salesman_id == salesman_id).order_by(Sale.amount).first()
    print(min_sale)
    session.close()
    return min_sale


def display_max_sale_by_customer(customer_id):
    session = Session()
    max_sale = session.query(Sale).filter(Sale.customer_id == customer_id).order_by(Sale.amount.desc()).first()
    print(max_sale)
    session.close()
    return max_sale


def display_min_sale_by_customer(customer_id):
    session = Session()
    min_sale = session.query(Sale).filter(Sale.customer_id == customer_id).order_by(Sale.amount).first()
    print(min_sale)
    session.close()
    return min_sale


def display_salesman_with_max_sales():
    session = Session()
    salesman = session.query(Salesman).join(Sale).group_by(Salesman.id).order_by(func.sum(Sale.amount).desc()).first()
    print(salesman)
    session.close()
    return salesman


def display_salesman_with_min_sales():
    session = Session()
    salesman = session.query(Salesman).join(Sale).group_by(Salesman.id).order_by(func.sum(Sale.amount)).first()
    print(salesman)
    session.close()
    return salesman


def display_customer_with_max_purchases():
    session = Session()
    customer = session.query(Customer).join(Sale).group_by(Customer.id).order_by(func.sum(Sale.amount).desc()).first()
    print(customer)
    session.close()
    return customer


def display_avg_purchase_by_customer(customer_id):
    session = Session()
    avg_purchase = session.query(func.avg(Sale.amount)).filter(Sale.customer_id == customer_id).scalar()
    print(f'Average purchase for customer with ID {customer_id}: {avg_purchase}')
    session.close()
    return avg_purchase


def display_avg_purchase_by_salesman(salesman_id):
    session = Session()
    avg_purchase = session.query(func.avg(Sale.amount)).filter(Sale.salesman_id == salesman_id).scalar()
    print(f'Average purchase for salesman with ID {salesman_id}: {avg_purchase}')
    session.close()
    return avg_purchase


def insert_sale():
    session = Session()
    salesman_id = input("Enter Seller ID: ")
    customer_id = input("Enter Customer ID: ")
    amount = input("Enter Amount: ")
    sale_date = input("Enter Sale Date: ")
    payment_status = input("Enter Payment Status: ")
    sale = Sale(salesman_id=salesman_id, customer_id=customer_id, amount=amount, sale_date=sale_date,
                payment_status=payment_status)
    session.add(sale)
    session.commit()
    session.close()
    print("Sale inserted successfully!")


def update_sale():
    session = Session()
    sale_id = input("Enter Sale ID: ")
    sale = session.query(Sale).filter(Sale.id == sale_id).first()
    if sale:
        salesman_id = input(f"Enter new Seller ID (current value: {sale.salesman_id}): ")
        customer_id = input(f"Enter new Customer ID (current value: {sale.customer_id}): ")
        amount = input(f"Enter new Amount (current value: {sale.amount}): ")
        sale_date = input(f"Enter new Sale Date (current value: {sale.sale_date}): ")
        payment_status = input(f"Enter new Payment Status (current value: {sale.payment_status}): ")
        sale.salesman_id = salesman_id
        sale.customer_id = customer_id
        sale.amount = amount
        sale.sale_date = sale_date
        sale.payment_status = payment_status
        session.commit()
        print("Sale updated successfully!")
    else:
        print(f"Sale with ID {sale_id} not found.")
    session.close()


def delete_sale():
    session = Session()
    sale_id = input("Enter Sale ID: ")
    sale = session.query(Sale).filter(Sale.id == sale_id).first()
    if sale:
        session.delete(sale)
        session.commit()
        print("Sale deleted successfully!")
    else:
        print(f"Sale with ID {sale_id} not found.")
    session.close()


def save_results_to_file(results, filename):
    with open(filename, 'a') as file:
        for result in results:
            file.write(str(result) + '\n')
    print(f"Results saved to file: {filename}")


create_db()


while True:
    print("=== Menu ===")
    print("1. Display all deals")
    print("2. Display transactions of a specific seller")
    print("3. Display the maximum transaction amount for a specific seller")
    print("4. Display the minimum transaction amount for a particular seller")
    print("5. Display the maximum transaction amount for a specific buyer")
    print("6. Display the minimum transaction amount for a specific buyer")
    print("7. Display the seller with the maximum amount of sales across all transactions")
    print("8. Display the seller with the minimum amount of sales across all transactions")
    print("9. Display the buyer with the maximum amount of purchases across all transactions")
    print("10. Display the average purchase amount for a particular customer")
    print("11. Display the average purchase amount for a particular seller")
    print("12. Insert a new sale")
    print("13. Update a sale")
    print("14. Delete a sale")
    print("0. Exit")
    choice = input("Choose your command: ")

    if choice == "1":
        print("=== All deals ===")
        result = display_all_sales()
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "2":
        salesman_id = input("Enter Seller ID: ")
        print(f"=== Seller transactions with ID {salesman_id} ===")
        result = display_sales_by_salesman(salesman_id)
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "3":
        salesman_id = input("Enter Seller ID: ")
        print(f"=== Maximum transaction amount for a seller with an ID {salesman_id} ===")
        result = display_max_sale_by_salesman(salesman_id)
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "4":
        salesman_id = input("Enter Seller ID: ")
        print(f"=== Minimum transaction amount for a seller with an ID {salesman_id} ===")
        result = display_min_sale_by_salesman(salesman_id)
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "5":
        customer_id = input("Enter Customer ID: ")
        print(f"=== Maximum transaction amount for a customer with an ID {customer_id} ===")
        result = display_max_sale_by_customer(customer_id)
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "6":
        customer_id = input("Enter Customer ID: ")
        print(f"=== Minimum transaction amount for a customer with an ID {customer_id} ===")
        result = display_min_sale_by_customer(customer_id)
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "7":
        print("=== Seller with the highest amount of sales ===")
        result = display_salesman_with_max_sales()
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "8":
        print("=== Seller with the minimum amount of sales ===")
        result = display_salesman_with_min_sales()
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "9":
        print("=== The customer with the maximum amount of purchases ===")
        result = display_customer_with_max_purchases()
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "10":
        customer_id = input("Enter Customer ID: ")
        print(f"=== Average purchase amount for a customer with an ID {customer_id} ===")
        result = display_avg_purchase_by_customer(customer_id)
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "11":
        salesman_id = input("Enter Seller ID: ")
        print(f"=== Average purchase amount for seller with ID{salesman_id} ===")
        result = display_avg_purchase_by_salesman(salesman_id)
        choice = input('Do you want save your transaction ? (Y/N): ')
        if choice.lower() == "y":
            filename = input('Enter your filename: ')
            save_results_to_file(result, filename)
        elif choice == "n":
            print("Okay, we won't save your transaction")
        else:
            print('Wrong command')
    elif choice == "12":
        insert_sale()
    elif choice == "13":
        update_sale()
    elif choice == "14":
        delete_sale()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid command. Try again.")
