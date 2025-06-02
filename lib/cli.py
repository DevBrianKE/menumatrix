from lib.helpers import (
    add_menu_item,
    list_menu_items,
    create_order,
    add_item_to_order,
    get_order_items,
    get_order_details,
    exit_program
)

def print_menu():
    print("\n=== Menu Matrix CLI ===")
    print("1. Add a Menu Item")
    print("2. List Menu Items")
    print("3. Create New Order")
    print("4. Add Item to Order")
    print("5. View Order Items")
    print("6. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter menu item name: ").strip()
            price = float(input("Enter price: "))
            description = input("Enter description (optional): ").strip() or None
            item = add_menu_item(name, price, description)
            print(f"Added MenuItem: {item}")

        elif choice == "2":
            items = list_menu_items()
            if not items:
                print("No menu items found.")
            else:
                print("Menu Items:")
                for item in items:
                    print(f"  ID: {item.id}, Name: {item.name}, Price: {item.price}, Description: {item.description}")

        elif choice == "3":
            order = create_order()
            print(f"Created Order: {order}")

        elif choice == "4":
            order_id = int(input("Enter Order ID: "))
            menu_item_id = int(input("Enter Menu Item ID to add: "))
            quantity = int(input("Enter quantity (default 1): ") or "1")
            try:
                add_item_to_order(order_id, menu_item_id, quantity)
                print(f"Added item {menu_item_id} x{quantity} to order {order_id}")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif choice == "5":
            order_id = int(input("Enter Order ID to view: "))
            details = get_order_details(order_id)

            if not details:
                print(f"No items found for order {order_id}")
            else:
                print(f"\nItems in Order {order_id}:")
                grand_total = 0
                for item in details:
                    print(f"- {item['name']} | Qty: {item['quantity']} | Price: {item['price']:.2f} | Subtotal: {item['subtotal']:.2f}")
                    grand_total += item["subtotal"]
                print(f"\nGrand Total: {grand_total:.2f}")

        elif choice == "6":
            exit_program()

        else:
            print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
