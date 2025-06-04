from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from lib.models import Base  

class MenuItem(Base):
    __tablename__ = 'menu_items'

    # Unique identifier for each menu item
    id = Column(Integer, primary_key=True)

    # Name of the menu item, required field
    name = Column(String(100), nullable=False)

    # Price of the menu item, required field
    price = Column(Float, nullable=False)

    # Optional description for the menu item
    description = Column(String(250), nullable=True)

    def __repr__(self):
        # String representation for debugging
        return f"<MenuItem(id={self.id}, name='{self.name}', price={self.price})>"


class Order(Base):
    __tablename__ = 'orders'

    # Unique identifier for each order
    id = Column(Integer, primary_key=True)

    # Timestamp when the order was created, defaults to current UTC time
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Status of the order (e.g., pending, completed), default is 'pending'
    status = Column(String(50), default='pending')

    # Relationship to the associated order items
    order_items = relationship('OrderItem', back_populates='order')

    def __repr__(self):
        # String representation for debugging
        return f"<Order(id={self.id}, status='{self.status}', timestamp={self.timestamp})>"


class OrderItem(Base):
    __tablename__ = 'order_items'

    # Unique identifier for each order item record
    id = Column(Integer, primary_key=True)

    # Foreign key linking to the related order
    order_id = Column(Integer, ForeignKey('orders.id'))

    # Foreign key linking to the menu item included in the order
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))

    # Quantity of the menu item in this order item, defaults to 1
    quantity = Column(Integer, default=1)

    # Back-reference to the Order this item belongs to
    order = relationship('Order', back_populates='order_items')

    # Reference to the MenuItem instance
    menu_item = relationship('MenuItem')

    def __repr__(self):
        # String representation for debugging
        return f"<OrderItem(order_id={self.order_id}, menu_item_id={self.menu_item_id}, quantity={self.quantity})>"
