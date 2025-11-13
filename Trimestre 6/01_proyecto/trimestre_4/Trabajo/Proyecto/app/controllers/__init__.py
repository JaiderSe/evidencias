# app/controllers/__init__.py

from .auth_controller import auth_bp
from .menu_controller import menu_bp
from .order_controller import order_bp
from .inventory_controller import inventory_bp

__all__ = ['auth_bp', 'menu_bp', 'order_bp', 'inventory_bp']