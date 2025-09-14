class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No items in order.")
            return
        print("\nYour order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")
        print(f"Total: ${self.total():.2f}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Order confirmed. Thank you!")
            self.items.clear()
        else:
            print("Order cancelled.")

def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Mocha", 4.0)
    ]

    user_order = Order()

    while True:
        print("\nMenu:")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Select an option (1-7): ").strip()
        if choice in map(str, range(1, 5)):
            user_order.add_item(menu[int(choice) - 1])
        elif choice == '5':
            user_order.show_order()
        elif choice == '6':
            user_order.checkout()
        elif choice == '7':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()