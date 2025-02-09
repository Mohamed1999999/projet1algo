class OrderManagement:
    def __init__(self, menu: dict):
        """Initialize the order management system with a menu."""
        if not isinstance(menu, dict):
            raise ValueError("menu must be a dictionary")
        self.menu = menu
        self.orders = set()

    def create_order(self, customer_name: str, ordered_dishes: list):
        """Create an order for a customer and add it to the set of orders, avoiding duplicates."""
        if not all(dish in self.menu for dish in ordered_dishes):
            missing_dishes = [dish for dish in ordered_dishes if dish not in self.menu]
            raise ValueError(f"The following dishes are not in the menu: {missing_dishes}")
        
        order = (customer_name, tuple(ordered_dishes))
        if order in self.orders:
            print(f"Order for {customer_name} with dishes {ordered_dishes} already exists.")
        else:
            self.orders.add(order)
            print(f"Order for {customer_name} added successfully!")

    def order_exists(self, customer_name: str, ordered_dishes: list) -> bool:
        """Check if a specific order exists in the set of orders."""
        return (customer_name, tuple(ordered_dishes)) in self.orders

    def calculate_total(self, ordered_dishes: list) -> float:
        """Calculate the total price of an order by adding the prices of the ordered dishes."""
        if not all(dish in self.menu for dish in ordered_dishes):
            missing_dishes = [dish for dish in ordered_dishes if dish not in self.menu]
            raise ValueError(f"The following dishes are not in the menu: {missing_dishes}")
        
        return sum(self.menu[dish] for dish in ordered_dishes)

    def display_orders(self):
        """Display all orders and their totals."""
        print("#### Orders ####")
        if not self.orders:
            print("No orders have been placed yet.")
        else:
            for customer_name, ordered_dishes in self.orders:
                total = self.calculate_total(list(ordered_dishes))
                print(f"Customer: {customer_name}, Dishes: {list(ordered_dishes)}, Total: ${total:.2f}")
        print("################")