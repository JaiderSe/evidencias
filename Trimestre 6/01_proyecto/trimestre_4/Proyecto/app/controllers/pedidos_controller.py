from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from app.models.pedido import Pedido
from app.models.mesa import Mesa
from app.models.platillo import Platillo
from app.models.cliente import Cliente
from datetime import datetime

pedidos_bp = Blueprint('pedidos', __name__, url_prefix='/pedidos')

@pedidos_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection

@pedidos_bp.route('/')
def listar_pedidos():
    """Lista todos los pedidos"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'mesero', 'chef']:
            flash('No tienes permisos para esta sección', 'danger')
            return redirect(url_for('main.home'))
        
        pedido_model = Pedido(request.connection)
        
        # Filtrar según rol
        if session.get('user_role') == 'chef':
            pedidos = pedido_model.get_pedidos_para_cocina()    
        else:
            pedidos = pedido_model.get_all()
        
        return render_template('pedidos/list.html',
                            pedidos=pedidos,
                            user_role=session.get('user_role'))
    
    except Exception as e:
        flash(f'Error al obtener pedidos: {str(e)}', 'danger')
        return redirect(url_for('main.home'))

@pedidos_bp.route('/nuevo', methods=['GET', 'POST'])
def crear_pedido():
    """Crea un nuevo pedido"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'mesero']:
            flash('No tienes permisos para crear pedidos', 'danger')
            return redirect(url_for('pedidos.listar_pedidos'))
        
        mesa_model = Mesa(request.connection)
        platillo_model = Platillo(request.connection)
        cliente_model = Cliente(request.connection)
        
        mesas_disponibles = mesa_model.get_by_estado('disponible')
        platillos_activos = platillo_model.get_activos()
        clientes = cliente_model.get_all()
        
        if request.method == 'POST':
            # Validación básica
            required_fields = ['mesa_id', 'cliente_id']
            if not all(field in request.form for field in required_fields):
                flash('Todos los campos obligatorios deben estar completos', 'danger')
                return redirect(url_for('pedidos.crear_pedido'))
            
            # Obtener detalles del pedido
            detalles = []
            for key, value in request.form.items():
                if key.startswith('platillo_') and int(value) > 0:
                    platillo_id = key.replace('platillo_', '')
                    detalles.append({
                        'platillo_id': platillo_id,
                        'cantidad': int(value),
                        'precio': float(request.form[f'precio_{platillo_id}'])
                    })
            
            if not detalles:
                flash('Debe agregar al menos un platillo al pedido', 'danger')
                return redirect(url_for('pedidos.crear_pedido'))
            
            # Crear datos del pedido
            pedido_data = {
                'mesa_id': request.form['mesa_id'],
                'cliente_id': request.form['cliente_id'] or None,
                'usuario_id': session['user_id'],
                'notas': request.form.get('notas', ''),
                'detalles': detalles
            }
            
            # Crear pedido
            pedido_model = Pedido(request.connection)
            pedido_id = pedido_model.crear(pedido_data)
            
            # Cambiar estado de la mesa
            mesa_model.cambiar_estado(pedido_data['mesa_id'], 'ocupada')
            
            flash(f'Pedido #{pedido_id} creado exitosamente!', 'success')
            return redirect(url_for('pedidos.detalle_pedido', pedido_id=pedido_id))
        
        return render_template('pedidos/form.html',
                            mesas=mesas_disponibles,
                            platillos=platillos_activos,
                            clientes=clientes)
    
    except Exception as e:
        flash(f'Error al crear pedido: {str(e)}', 'danger')
        return redirect(url_for('pedidos.listar_pedidos'))

@pedidos_bp.route('/<int:pedido_id>')
def detalle_pedido(pedido_id):
    """Muestra los detalles de un pedido específico"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'mesero', 'chef']:
            flash('No tienes permisos para ver este pedido', 'danger')
            return redirect(url_for('main.home'))
        
        pedido_model = Pedido(request.connection)
        pedido = pedido_model.get_by_id(pedido_id)
        
        if not pedido:
            flash('Pedido no encontrado', 'danger')
            return redirect(url_for('pedidos.listar_pedidos'))
        
        return render_template('pedidos/detalle.html',
                            pedido=pedido,
                            user_role=session.get('user_role'))
    
    except Exception as e:
        flash(f'Error al obtener pedido: {str(e)}', 'danger')
        return redirect(url_for('pedidos.listar_pedidos'))

@pedidos_bp.route('/actualizar-estado/<int:pedido_id>', methods=['POST'])
def actualizar_estado_pedido(pedido_id):
    """Actualiza el estado de un pedido (AJAX)"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'mesero', 'chef']:
            return jsonify({'error': 'No autorizado'}), 403
            
        if not request.is_json:
            return jsonify({'error': 'Solicitud no válida'}), 400
            
        data = request.get_json()
        nuevo_estado = data.get('estado')
        
        if not nuevo_estado:
            return jsonify({'error': 'Estado no proporcionado'}), 400
        
        pedido_model = Pedido(request.connection)
        if pedido_model.actualizar_estado(pedido_id, nuevo_estado):
            return jsonify({
                'success': True,
                'nuevo_estado': nuevo_estado,
                'badge_class': get_badge_class_pedido(nuevo_estado)
            })
        else:
            return jsonify({'error': 'Error al actualizar'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@pedidos_bp.route('/cerrar/<int:pedido_id>', methods=['POST'])
def cerrar_pedido(pedido_id):
    """Cierra un pedido y marca como pagado"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'mesero']:
            flash('No tienes permisos para cerrar pedidos', 'danger')
            return redirect(url_for('main.home'))
        
        pedido_model = Pedido(request.connection)
        pedido = pedido_model.get_by_id(pedido_id)
        
        if not pedido:
            flash('Pedido no encontrado', 'danger')
            return redirect(url_for('pedidos.listar_pedidos'))
        
        # Actualizar estado del pedido
        pedido_model.actualizar_estado(pedido_id, 'pagado')
        
        # Liberar mesa
        mesa_model = Mesa(request.connection)
        mesa_model.cambiar_estado(pedido['mesa_id'], 'disponible')
        
        flash(f'Pedido #{pedido_id} cerrado y marcado como pagado', 'success')
        return redirect(url_for('pedidos.listar_pedidos'))
    
    except Exception as e:
        flash(f'Error al cerrar pedido: {str(e)}', 'danger')
        return redirect(url_for('pedidos.listar_pedidos'))

def get_badge_class_pedido(estado):
    """Devuelve la clase CSS según el estado del pedido"""
    classes = {
        'recibido': 'bg-primary',
        'en preparacion': 'bg-warning',
        'listo': 'bg-info',
        'entregado': 'bg-success',
        'cancelado': 'bg-danger',
        'pagado': 'bg-secondary'
    }
    return classes.get(estado, 'bg-light text-dark')