from models.menu_item import MenuItem
import sqlite3

class MenuController:

    def add_menu_item(self, name, price, quantity):
        item = MenuItem(name, price, quantity)
        item.save()
        print(f"✅ '{name}' added to menu.")

    def view_all_items(self):
        connection = sqlite3.connect("database/menu.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM menu")
        items = cursor.fetchall()
        connection.close()
        if items:
            print("📋 All Menu Items:")
            for item in items:
                print(f"ID: {item[0]} | Name: {item[1]} | Price: ${item[2]:.2f} | Quantity: {item[3]}")
        else:
            print("😶 Menu is empty.")

    def update_item(self, item_id, new_name=None, new_price=None, new_quantity=None):
        connection = sqlite3.connect("database/menu.db")
        cursor = connection.cursor()
        if new_name:
            cursor.execute("UPDATE menu SET name = ? WHERE id = ?", (new_name, item_id))
        if new_price:
            cursor.execute("UPDATE menu SET price = ? WHERE id = ?", (new_price, item_id))
        if new_quantity:
            cursor.execute("UPDATE menu SET quantity = ? WHERE id = ?", (new_quantity, item_id))
        connection.commit()
        connection.close()
        print("✏️ Item updated.")

    def delete_item(self, item_id):
        connection = sqlite3.connect("database/menu.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM menu WHERE id = ?", (item_id,))
        connection.commit()
        connection.close()
        print("🗑️ Item deleted.")
