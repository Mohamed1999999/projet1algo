class PaymentManagement:
    def __init__(self):
        """Initialize the payment management system."""
        self.payments = {}  # Stores payments as {order_id: (amount, method)}
        self.total_revenue = 0  # Tracks the total revenue
    
    def record_payment(self, order_id: int, amount: float, method: str):
        """
        Record a payment for a specific order.
        
        Args:
        - order_id (int): The unique ID of the order being paid.
        - amount (float): The payment amount.
        - method (str): The payment method (e.g., 'cash', 'credit card').
        
        Raises:
        - ValueError: If the order ID has already been paid.
        """
        if order_id in self.payments:
            raise ValueError(f"Order ID {order_id} has already been paid.")
        
        self.payments[order_id] = (amount, method)
        self.total_revenue += amount
        print(f"Payment recorded for Order ID {order_id}: ${amount} via {method}.")

    def check_payment_status(self, order_id: int) -> bool:
        """
        Check if a specific order has been paid for.

        Args:
        - order_id (int): The unique ID of the order.

        Returns:
        - bool: True if the order has been paid, False otherwise.
        """
        return order_id in self.payments
    
    def display_all_payments(self):
        """Display a detailed list of all completed payments."""
        if not self.payments:
            print("No payments have been recorded yet.")
            return
        
        print("### Payments ###")
        for order_id, (amount, method) in self.payments.items():
            print(f"Order ID {order_id}: ${amount} via {method}")
        print("###############")
        print(f"Total Revenue: ${self.total_revenue}")
    
    def get_total_revenue(self) -> float:
        """
        Get the total revenue from all payments.

        Returns:
        - float: The total revenue.
        """
        return self.total_revenue