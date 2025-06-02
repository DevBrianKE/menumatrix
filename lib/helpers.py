from typing import List
from lib.db.session import get_session
from lib.models.models import MenuItem, Order, OrderItem
from sqlalchemy.exc import NoResultFound

def add_menu_item(name: str, price: float, description: str = None) -> MenuItem:
    session = get_session()
    try:
        menu_item = MenuItem(name=name, price=price, description=description)
        session.add(menu_item)
        session.commit()
        return menu_item
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def list_menu_items() -> List[MenuItem]:
    session = get_session()
    try:
        return session.query(MenuItem).all()
    finally:
        session.close()

def create_order() -> Order:
    session = get_session()
    try:
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
        order = session.query(Order).filter(Order.id == order_id).one()
        existing_order_item = session.query(OrderItem).filter(
            OrderItem.order_id == order_id,
            OrderItem.menu_item_id == menu_item_id
        ).one_or_none()

        if existing_order_item:
            existing_order_item.quantity += quantity
        else:
            new_order_item = OrderItem(order_id=order_id, menu_item_id=menu_item_id, quantity=quantity)
            session.add(new_order_item)
        session.commit()
    except NoResultFound:
        raise ValueError(f"Order with id {order_id} or MenuItem with id {menu_item_id} does not exist.")
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_order_items(order_id: int) -> List[OrderItem]:
    session = get_session()
    try:
        return session.query(OrderItem).filter(OrderItem.order_id == order_id).all()
    finally:
        session.close()

def get_order_details(order_id: int) -> List[dict]:
    """Fetch full order details: item name, price, quantity, and subtotal."""
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
