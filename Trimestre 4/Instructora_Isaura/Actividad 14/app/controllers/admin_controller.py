# app/controllers/admin_controller.py
from flask import Blueprint, render_template, session, redirect, url_for, current_app
from app.models.user_model import get_user_by_id
from app.models.product_model import get_product_count
from app.models.category_model import get_category_count

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin/dashboard')
def admin_dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_bp.login'))

    connection = current_app.connection
    user = get_user_by_id(connection, user_id)
    if not user:
        return "Administrador no encontrado"

    # estadísticas del sistema
    product_count = get_product_count(connection)
    category_count = get_category_count(connection)

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS user_count FROM usuarios")
        user_count = cursor.fetchone()['user_count']

    return render_template('admin_dashboard.html', user=user,
                           user_count=user_count,
                           category_count=category_count,
                           product_count=product_count)
