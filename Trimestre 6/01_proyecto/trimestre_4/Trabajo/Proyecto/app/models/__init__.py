# app/models/__init__.py

from .user import User
from .category import Category
from .dish import Dish
from .ingredient import Ingredient
from .table import Table
from .customer import Customer
from .order import Order
from .order_detail import OrderDetail
from .inventory_movement import InventoryMovement

# Importar tablas de relación
from app.utils.db import dish_ingredient, customer_favorite

__all__ = [
    'User', 
    'Category', 
    'Dish', 
    'Ingredient', 
    'Table', 
    'Customer',
    'Order', 
    'OrderDetail', 
    'InventoryMovement',
    'dish_ingredient',
    'customer_favorite'
]