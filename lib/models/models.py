from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from lib.models import Base  

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(250), nullable=True)

    def __repr__(self):
        return f"<MenuItem(id={self.id}, name='{self.name}', price={self.price})>"


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default='pending')

    order_items = relationship('OrderItem', back_populates='order')

    def __repr__(self):
        return f"<Order(id={self.id}, status='{self.status}', timestamp={self.timestamp})>"


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    quantity = Column(Integer, default=1)

    order = relationship('Order', back_populates='order_items')
    menu_item = relationship('MenuItem')

    def __repr__(self):
        return f"<OrderItem(order_id={self.order_id}, menu_item_id={self.menu_item_id}, quantity={self.quantity})>"
