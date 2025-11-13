from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.rol not in roles:
                flash('No tienes permiso para acceder a esta página', 'danger')
                return redirect(url_for('menu.list_dishes'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            flash('Ya has iniciado sesión', 'info')
            return redirect(url_for('menu.list_dishes'))
        return f(*args, **kwargs)
    return decorated_function