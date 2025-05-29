from models.menu_item import MenuItem

# Step 1: Create the database table
MenuItem.create_table()

# Step 2: Add a new menu item
burger = MenuItem("Burger", 7.99, 10)
burger.save()

print("Burger added successfully!")
