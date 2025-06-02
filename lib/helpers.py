from lib.db.session import get_session
from lib.models.models import MenuItem, Order, OrderItem
from sqlalchemy.exc import NoResultFound

def add_menu_item(name: str, price: float, description: str = None) -> MenuItem:
    """
    Create and add a new MenuItem to the database.
    """
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

def list_menu_items() -> list[MenuItem]:
    """
    Retrieve all menu items from the database.
    """
    session = get_session()
    try:
        items = session.query(MenuItem).all()
        return items
    finally:
        session.close()

def create_order() -> Order:
    """
    Create a new Order with status 'pending'.
    """
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
    """
    Add an OrderItem linking an order and a menu item.
    If the item already exists in the order, increase quantity.
    """
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

def get_order_items(order_id: int) -> list[OrderItem]:
    """
    Retrieve all OrderItems for a specific order.
    """
    session = get_session()
    try:
        items = session.query(OrderItem).filter(OrderItem.order_id == order_id).all()
        return items
    finally:
        session.close()

def exit_program():
    print("Goodbye!")
    exit()
