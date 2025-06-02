from lib.helpers import add_menu_item
import random

# Sample dish names served at Villa Rosa Kempinski
base_dishes = [
    "Grilled Nile Perch", "Roasted Lamb Shoulder", "Seafood Paella", "Tuscan Chicken",
    "Vegetarian Risotto", "Beef Wellington", "Prawn Curry", "Swahili Biryani",
    "Fillet Mignon", "Pan-Seared Salmon", "Braised Duck Breast", "Stuffed Bell Peppers",
    "Moroccan Tagine", "Sushi Platter", "Butter Chicken", "Masala Chips",
    "Spinach Lasagna", "Classic Caesar Salad", "Pumpkin Soup", "Goat Cheese Tart"
]

# Sample descriptions
descriptions = [
    "Signature dish from Villa Rosa Kempinski",
    "Prepared by top chefs using premium ingredients",
    "Inspired by traditional Kenyan and European cuisine",
    "Five-star dining experience at Villa Rosa Kempinski",
    "A rich, savory delight served with seasonal vegetables"
]

# Generate 100 unique menu items
def generate_villa_rosa_menu_items(count=100):
    for i in range(count):
        name = f"{random.choice(base_dishes)} #{i+1}"
        price = round(random.uniform(150.0, 1000.0), 2)
        description = random.choice(descriptions)
        add_menu_item(name, price, description)
    print(f"✅ Successfully added {count} Villa Rosa Kempinski menu items.")

if __name__ == "__main__":
    generate_villa_rosa_menu_items(100)
