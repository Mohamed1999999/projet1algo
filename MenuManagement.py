class MenuManagement:
    def __init__(self, dishes: dict = None):
        """Initialize the menu with a dictionary of dishes."""
        if dishes is None:
            dishes = {}
        if not isinstance(dishes, dict):
            raise ValueError("dishes must be a dictionary")
        self.dishes = dishes

    def add(self, name: str, price: float):
        """Add a dish to the menu."""
        if name in self.dishes:
            print(f"{name} already exists in the menu. Price updated.")
        self.dishes[name] = price
        print(f"{name} has been added/updated with a price of {price}.")
        self.display()

    def remove(self, name: str):
        """Remove a dish from the menu."""
        if name in self.dishes:
            while True:
                yes_or_no = input(f"Are you sure you want to delete {name}? [y/n]: ").strip().lower()
                if yes_or_no == "y":
                    del self.dishes[name]
                    print(f"{name} has been removed from the menu!")
                    break
                elif yes_or_no == "n":
                    print("No changes were made.")
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print(f"{name} does not exist in the menu.")

    def modify(self, menu: dict):
        """Replace the entire menu."""
        if not isinstance(menu, dict):
            raise ValueError("menu must be a dictionary")
        self.dishes = menu
        print("The menu has been updated.")
        self.display()

    def display(self):
        """Display the current menu."""
        print("#### Menu ####")
        if not self.dishes:
            print("The menu is empty.")
        else:
            for name, price in self.dishes.items():
                print(f"{name}: ${price:.2f}")
        print("###############")