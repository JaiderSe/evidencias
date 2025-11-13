from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.services.inventory_service import InventoryService
from app.forms import InventoryMovementForm
from app.utils.decorators import role_required

inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')
service = InventoryService()

@inventory_bp.route('/')
@login_required
@role_required('inventario', 'administrador')
def list_inventory():
    low_stock = request.args.get('low_stock', 'false') == 'true'
    ingredients = service.get_low_stock_ingredients() if low_stock else service.get_all_ingredients()
    return render_template('inventory/list.html', 
                         ingredients=ingredients,
                         low_stock=low_stock)

@inventory_bp.route('/movements')
@login_required
@role_required('inventario', 'administrador')
def list_movements():
    ingredient_id = request.args.get('ingredient_id')
    movements = service.get_movements_by_ingredient(ingredient_id) if ingredient_id else service.get_all_movements()
    return render_template('inventory/movements.html', movements=movements)

@inventory_bp.route('/add-movement', methods=['GET', 'POST'])
@login_required
@role_required('inventario')
def add_movement():
    form = InventoryMovementForm()
    form.ingredient_id.choices = [(i.ingrediente_id, i.nombre) for i in service.get_all_ingredients()]
    
    if form.validate_on_submit():
        movement_data = {
            'ingredient_id': form.ingredient_id.data,
            'cantidad': form.cantidad.data,
            'tipo_movimiento': form.tipo_movimiento.data,
            'motivo': form.motivo.data,
            'costo_total': form.costo_total.data,
            'usuario_id': current_user.usuario_id
        }
        service.add_movement(movement_data)
        flash('Movimiento de inventario registrado', 'success')
        return redirect(url_for('inventory.list_movements'))
    
    return render_template('inventory/add_movement.html', form=form)

@inventory_bp.route('/ingredient/<int:id>')
@login_required
@role_required('inventario', 'administrador')
def ingredient_detail(id):
    ingredient = service.get_ingredient_by_id(id)
    if not ingredient:
        flash('Ingrediente no encontrado', 'danger')
        return redirect(url_for('inventory.list_inventory'))
    
    movements = service.get_movements_by_ingredient(id)
    return render_template('inventory/ingredient_detail.html', 
                         ingredient=ingredient,
                         movements=movements)