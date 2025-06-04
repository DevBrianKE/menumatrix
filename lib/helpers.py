from typing import List
from lib.db.session import get_session
from lib.models.models import MenuItem, Order, OrderItem
from sqlalchemy.exc import NoResultFound

def add_menu_item(name: str, price: float, description: str = None) -> MenuItem:
    session = get_session()
    try:
        # Create a new menu item instance
        menu_item = MenuItem(name=name, price=price, description=description)
        # Add the new item to the session and commit to the database
        session.add(menu_item)
        session.commit()
        return menu_item
    except Exception as e:
        # Rollback changes on any error
        session.rollback()
        raise e
    finally:
        # Always close the session to release resources
        session.close()

def list_menu_items() -> List[MenuItem]:
    session = get_session()
    try:
        # Retrieve all menu items from the database
        return session.query(MenuItem).all()
    finally:
        session.close()

def create_order() -> Order:
    session = get_session()
    try:
        # Create a new order instance with default status and timestamp
        order = Order()
        session.add(order)
        session.commit()
        return order
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def add_item_to_order(order_id: int, menu_item_id: int, quantity: int = 1):
    session = get_session()
    try:
        # Confirm the order exists
        order = session.query(Order).filter(Order.id == order_id).one()

        # Check if this menu item is already added to the order
        existing_order_item = session.query(OrderItem).filter(
            OrderItem.order_id == order_id,
            OrderItem.menu_item_id == menu_item_id
        ).one_or_none()

        if existing_order_item:
            # If exists, increase quantity
            existing_order_item.quantity += quantity
        else:
            # Otherwise, create a new order item entry
            new_order_item = OrderItem(order_id=order_id, menu_item_id=menu_item_id, quantity=quantity)
            session.add(new_order_item)
        
        session.commit()
    except NoResultFound:
        # If order or menu item is missing, raise a clear error
        raise ValueError(f"Order with id {order_id} or MenuItem with id {menu_item_id} does not exist.")
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_order_items(order_id: int) -> List[OrderItem]:
    session = get_session()
    try:
        # Fetch all order items associated with a specific order
        return session.query(OrderItem).filter(OrderItem.order_id == order_id).all()
    finally:
        session.close()

def get_order_details(order_id: int) -> List[dict]:
    #Retrieve detailed info about items in an order including subtotals.
    session = get_session()
    try:
        order_items = session.query(OrderItem).filter(OrderItem.order_id == order_id).all()
        details = []
        for item in order_items:
            name = item.menu_item.name
            price = item.menu_item.price
            quantity = item.quantity
            total = price * quantity
            details.append({
                "name": name,
                "price": price,
                "quantity": quantity,
                "subtotal": total
            })
        return details
    finally:
        session.close()

def exit_program():
    print("Goodbye!")
    exit()
