from MenuManagement import MenuManagement
from OrderManagement import OrderManagement
from PayementManagement import PaymentManagement
from SalesManagement import SalesManagement

def main():
    # Initialize components
    menu = MenuManagement({})
    sales_mgmt = SalesManagement()
    payment_mgmt = PaymentManagement()
    orders_mgmt = OrderManagement(menu.menu)  # Utilisation correcte de OrderManagement

    print("Welcome to the Restaurant Management System!")

    while True:
        print("\nMain Menu:")
        print("1. Manage Menu")
        print("2. Manage Orders")
        print("3. Manage Payments")
        print("4. View Sales Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Menu Management
            while True:
                print("\nMenu Management:")
                print("1. Add Dish")
                print("2. Remove Dish")
                print("3. Display Menu")
                print("4. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ").strip()
                
                if sub_choice == "1":
                    name = input("Enter the dish name: ").strip()
                    price = float(input("Enter the price: ").strip())
                    menu.add(name, price)
                elif sub_choice == "2":
                    name = input("Enter the dish name to remove: ").strip()
                    menu.remove(name)
                elif sub_choice == "3":
                    menu.display()
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            # Order Management
            while True:
                print("\nOrder Management:")
                print("1. Create Order")
                print("2. Check Order")
                print("3. Display All Orders")
                print("4. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ").strip()
                
                if sub_choice == "1":
                    customer_name = input("Enter customer name: ").strip()
                    ordered_dishes = input("Enter ordered dishes (comma-separated): ").strip().split(",")
                    try:
                        menu_items = [dish.strip() for dish in ordered_dishes]
                        orders_mgmt.create_order(customer_name, menu_items)
                        sales_mgmt.record_order(menu_items)
                    except ValueError as e:
                        print(e)
                
                elif sub_choice == "2":
                    customer_name = input("Enter customer name: ").strip()
                    ordered_dishes = input("Enter ordered dishes (comma-separated): ").strip().split(",")
                    menu_items = [dish.strip() for dish in ordered_dishes]

                    if orders_mgmt.order_exists(customer_name, menu_items):
                        print(f"Order exists for {customer_name}: {menu_items}")
                    else:
                        print("Order not found.")

                elif sub_choice == "3":
                    orders_mgmt.display_orders()

                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            # Payment Management
            while True:
                print("\nPayment Management:")
                print("1. Record Payment")
                print("2. Check Payment Status")
                print("3. Display All Payments")
                print("4. Back to Main Menu")
                
                sub_choice = input("Enter your choice: ").strip()
                
                if sub_choice == "1":
                    order_id = int(input("Enter Order ID to record payment for: ").strip())
                    amount = float(input("Enter payment amount: ").strip())
                    method = input("Enter payment method (cash/credit card): ").strip()
                    try:
                        payment_mgmt.record_payment(order_id, amount, method)
                    except ValueError as e:
                        print(e)

                elif sub_choice == "2":
                    order_id = int(input("Enter Order ID to check payment status: ").strip())
                    if payment_mgmt.check_payment_status(order_id):
                        print(f"Order {order_id} has been paid.")
                    else:
                        print(f"Order {order_id} has not been paid.")
                elif sub_choice == "3":
                    payment_mgmt.display_all_payments()
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            # Sales Report
            sales_mgmt.generate_sales_report()

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
