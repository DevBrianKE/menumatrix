from sqlalchemy.orm import declarative_base

Base = declarative_base()
from .models import MenuItem, Order, OrderItem 