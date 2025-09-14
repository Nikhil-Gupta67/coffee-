# ☕ Coffee Ordering System

A simple command-line Coffee Ordering System built with Python. This interactive script lets users browse a coffee menu, add items to their order, view the order summary, and proceed to checkout—all from the terminal.

---

## 📦 Features

- Browse a menu of coffee drinks
- Add items to your order
- View your current order with itemized pricing
- Calculate total cost
- Confirm or cancel checkout
- Exit the program gracefully

---

## 🧠 Class Overview
Menu:
1. Espresso     - $2.50
2. Latte        - $3.50
3. Cappuccino   - $3.00
4. Mocha        - $4.00
5. View Order
6. Checkout
7. Exit

### `Coffee`
Represents a coffee item.

- `name`: Name of the coffee (e.g., `"Latte"`)
- `price`: Price of the coffee (e.g., `3.5`)

### `Order`
Manages the user's order.

- `add_item(coffee)`: Adds a coffee item to the order
- `total()`: Returns the total price of the order
- `show_order()`: Displays all items in the order
- `checkout()`: Prompts user to confirm or cancel the order

---

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Save the script as `coffee_order.py`.
3. Run the script:

```bash
python coffee_order.py