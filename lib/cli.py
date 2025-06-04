from lib.helpers import (
    add_menu_item,
    list_menu_items,
    create_order,
    add_item_to_order,
    get_order_items,
    get_order_details,
    exit_program
)
from tabulate import tabulate


def print_menu():
    # Display the main menu options to the user
    print("\n=== Menu Matrix CLI ===")
    print("1. Add a Menu Item")
    print("2. List Menu Items")
    print("3. Create New Order")
    print("4. Add Item to Order")
    print("5. View Order Items")
    print("6. Exit")


def main():
    # Main program loop to interact with the user until exit
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            # Add a new menu item to the system
            name = input("Enter menu item name: ").strip()
            try:
                price = float(input("Enter price: "))
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            description = input("Enter description (optional): ").strip() or None
            try:
                item = add_menu_item(name, price, description)
                print(f"Added MenuItem: {item}")
            except Exception as e:
                print(f"Error adding menu item: {e}")

        elif choice == "2":
            # List all existing menu items with formatted table output
            items = list_menu_items()
            if not items:
                print("No menu items found.")
            else:
                table = []
                for item in items:
                    table.append([
                        item.id,
                        item.name,
                        f"{item.price:.2f}",
                        item.description or ""
                    ])
                headers = ["ID", "Name", "Price ($)", "Description"]
                print("\nMenu Items:")
                print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

        elif choice == "3":
            # Create a new order record
            try:
                order = create_order()
                print(f"Created Order: {order}")
            except Exception as e:
                print(f"Error creating order: {e}")

        elif choice == "4":
            # Add items to an existing order
            try:
                order_id = int(input("Enter Order ID: "))
                menu_item_id = int(input("Enter Menu Item ID to add: "))
                quantity_input = input("Enter quantity (default 1): ").strip()
                quantity = int(quantity_input) if quantity_input else 1
                add_item_to_order(order_id, menu_item_id, quantity)
                print(f"Added item {menu_item_id} x{quantity} to order {order_id}")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "5":
            # View all items and totals for a specific order
            try:
                order_id = int(input("Enter Order ID to view: "))
                details = get_order_details(order_id)

                if not details:
                    print(f"No items found for order {order_id}")
                else:
                    table = []
                    grand_total = 0
                    for item in details:
                        subtotal = item['price'] * item['quantity']
                        table.append([
                            item['name'],
                            item['quantity'],
                            f"{item['price']:.2f}",
                            f"{subtotal:.2f}"
                        ])
                        grand_total += subtotal
                    headers = ["Item", "Quantity", "Price ($)", "Subtotal ($)"]
                    print(f"\nItems in Order {order_id}:")
                    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
                    print(f"\nGrand Total: {grand_total:.2f}")
            except ValueError:
                print("Invalid Order ID. Please enter a numeric value.")
            except Exception as e:
                print(f"Error retrieving order details: {e}")

        elif choice == "6":
            # Exit the program gracefully
            exit_program()

        else:
            # Invalid input handling
            print("Invalid choice, please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
