from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.services.order_service import OrderService
from app.services.menu_service import MenuService
from app.forms import OrderForm
from app.utils.decorators import role_required

order_bp = Blueprint('order', __name__, url_prefix='/orders')
order_service = OrderService()
menu_service = MenuService()

@order_bp.route('/')
@login_required
@role_required('mesero', 'administrador')
def list_orders():
    status = request.args.get('status', 'all')
    orders = order_service.get_orders_by_status(status) if status != 'all' else order_service.get_all_orders()
    return render_template('orders/list.html', orders=orders, current_status=status)

@order_bp.route('/new', methods=['GET', 'POST'])
@login_required
@role_required('mesero')
def new_order():
    form = OrderForm()
    form.mesa_id.choices = [(m.mesa_id, f"Mesa {m.numero_mesa}") for m in order_service.get_available_tables()]
    form.platillos.choices = [(p.platillo_id, f"{p.nombre} - ${p.precio:.2f}") 
                            for p in menu_service.get_active_dishes()]
    
    if form.validate_on_submit():
        order_data = {
            'mesa_id': form.mesa_id.data,
            'usuario_id': current_user.usuario_id,
            'notas': form.notas.data,
            'platillos': request.form.getlist('platillos'),
            'cantidades': request.form.getlist('cantidades'),
            'personalizaciones': request.form.getlist('personalizaciones')
        }
        new_order = order_service.create_order(order_data)
        flash(f'Pedido #{new_order.pedido_id} creado exitosamente', 'success')
        return redirect(url_for('order.detail_order', id=new_order.pedido_id))
    
    return render_template('orders/new.html', form=form)

@order_bp.route('/<int:id>')
@login_required
def detail_order(id):
    order = order_service.get_order_by_id(id)
    if not order:
        flash('Pedido no encontrado', 'danger')
        return redirect(url_for('order.list_orders'))
    return render_template('orders/detail.html', order=order)

@order_bp.route('/<int:id>/update-status', methods=['POST'])
@login_required
@role_required('chef', 'mesero', 'administrador')
def update_order_status(id):
    new_status = request.form.get('status')
    if not new_status:
        flash('Estado no válido', 'danger')
        return redirect(url_for('order.detail_order', id=id))
    
    order_service.update_order_status(id, new_status)
    flash('Estado del pedido actualizado', 'success')
    return redirect(url_for('order.detail_order', id=id))

@order_bp.route('/kitchen')
@login_required
@role_required('chef')
def kitchen_orders():
    pending_orders = order_service.get_orders_by_status('en preparacion')
    new_orders = order_service.get_orders_by_status('recibido')
    return render_template('orders/kitchen.html', 
                         pending_orders=pending_orders,
                         new_orders=new_orders)