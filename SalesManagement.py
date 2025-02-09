class SalesManagement:
    def __init__(self):
        """Initialize the sales management system."""
        self.dish_sales = {}  # Stores the number of times each dish has been ordered
    
    def record_order(self, ordered_dishes: list):
        """
        Record the dishes from an order to track sales.
        
        Args:
        - ordered_dishes (list): A list of dishes in the order.
        """
        for dish in ordered_dishes:
            if dish in self.dish_sales:
                self.dish_sales[dish] += 1
            else:
                self.dish_sales[dish] = 1
    
    def generate_sales_report(self):
        """
        Generate a sales report indicating the most popular dishes.
        """
        if not self.dish_sales:
            print("No sales data available.")
            return
        
        print("### Sales Report ###")
        sorted_sales = sorted(self.dish_sales.items(), key=lambda x: x[1], reverse=True)
        for dish, count in sorted_sales:
            print(f"{dish}: {count} orders")
        print("####################")