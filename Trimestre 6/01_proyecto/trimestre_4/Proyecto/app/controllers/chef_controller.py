from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from app.models.pedido import Pedido
from app.models.detalle_pedido import DetallePedido
from datetime import datetime

chef_bp = Blueprint('chef', __name__, url_prefix='/chef')

@chef_bp.before_request
def check_chef():
    """Verifica que el usuario sea chef antes de cada solicitud"""
    if session.get('user_role') != 'chef':
        flash('Acceso restringido a chefs', 'danger')
        return redirect(url_for('main.dashboard'))

@chef_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection
    request.bcrypt = current_app.bcrypt

@chef_bp.route('/dashboard')
def dashboard():
    """Vista principal del chef con pedidos pendientes"""
    try:
        pedido_model = Pedido(request.connection)
        pedidos_pendientes = pedido_model.get_pedidos_para_cocina()
        
        return render_template('chef/dashboard.html', 
                            pedidos=pedidos_pendientes,
                            ahora=datetime.now())
    except Exception as e:
        flash(f'Error al cargar el dashboard: {str(e)}', 'danger')
        return redirect(url_for('main.dashboard'))

# --------------------------------------------------
# Gestión de Pedidos
# --------------------------------------------------
@chef_bp.route('/pedidos/pendientes')
def pedidos_pendientes():
    """Lista todos los detalles de pedidos pendientes para cocina"""
    try:
        detalle_model = DetallePedido(request.connection)
        detalles = detalle_model.get_pendientes_cocina()
        
        return render_template('chef/pedidos_pendientes.html', 
                            detalles=detalles)
    except Exception as e:
        flash(f'Error al obtener pedidos pendientes: {str(e)}', 'danger')
        return redirect(url_for('chef.dashboard'))

@chef_bp.route('/detalle/<int:detalle_id>')
def ver_detalle(detalle_id):
    """Muestra los detalles de un ítem específico"""
    try:
        detalle_model = DetallePedido(request.connection)
        detalle = detalle_model.get_by_id(detalle_id)
        
        if not detalle:
            flash('Detalle de pedido no encontrado', 'danger')
            return redirect(url_for('chef.pedidos_pendientes'))
        
        return render_template('chef/detalle_pedido.html', 
                            detalle=detalle)
    except Exception as e:
        flash(f'Error al obtener detalle: {str(e)}', 'danger')
        return redirect(url_for('chef.pedidos_pendientes'))

@chef_bp.route('/actualizar-estado/<int:detalle_id>', methods=['POST'])
def actualizar_estado(detalle_id):
    """Actualiza el estado de un ítem de pedido (AJAX)"""
    try:
        if not request.is_json:
            return jsonify({'error': 'Solicitud no válida'}), 400
            
        data = request.get_json()
        nuevo_estado = data.get('estado')
        notas_chef = data.get('notas_chef', None)
        
        if not nuevo_estado:
            return jsonify({'error': 'Estado no proporcionado'}), 400
        
        detalle_model = DetallePedido(request.connection)
        if detalle_model.actualizar_estado(detalle_id, nuevo_estado, notas_chef):
            return jsonify({
                'success': True,
                'nuevo_estado': nuevo_estado,
                'badge_class': get_badge_class_estado(nuevo_estado)
            })
        else:
            return jsonify({'error': 'Error al actualizar'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_badge_class_estado(estado):
    """Devuelve la clase CSS según el estado"""
    classes = {
        'pendiente': 'bg-secondary',
        'en preparacion': 'bg-warning text-dark',
        'listo': 'bg-success',
        'entregado': 'bg-info text-dark'
    }
    return classes.get(estado, 'bg-light text-dark')

# --------------------------------------------------
# Gestión de Recetas
# --------------------------------------------------
@chef_bp.route('/recetas')
def listar_recetas():
    """Lista todas las recetas disponibles"""
    try:
        platillo_model = platillos(request.connection)
        platillos = platillo_model.get_all()
        
        return render_template('chef/recetas/list.html', 
                            platillos=platillos)
    except Exception as e:
        flash(f'Error al obtener recetas: {str(e)}', 'danger')
        return redirect(url_for('chef.dashboard'))

@chef_bp.route('/recetas/<int:platillo_id>')
def ver_receta(platillo_id):
    """Muestra los detalles de una receta específica"""
    try:
        platillo_model = platillos(request.connection)
        platillos = platillo_model.get_by_id(platillo_id)
        
        if not platillos:
            flash('Receta no encontrada', 'danger')
            return redirect(url_for('chef.listar_recetas'))
        
        ingredientes = platillo_model.get_ingredientes(platillo_id)
        
        return render_template('chef/recetas/detalle.html', 
                            platillo=platillos,
                            ingredientes=ingredientes)
    except Exception as e:
        flash(f'Error al obtener receta: {str(e)}', 'danger')
        return redirect(url_for('chef.listar_recetas'))