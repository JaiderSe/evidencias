from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from app.models.mesa import Mesa
from app.models.pedido import Pedido
from app.models.platillo import Platillo
from app.models.cliente import Cliente
from datetime import datetime

mesero_bp = Blueprint('mesero', __name__, url_prefix='/mesero')

@mesero_bp.before_request
def check_mesero():
    """Verifica que el usuario sea mesero antes de cada solicitud"""
    if session.get('user_role') != 'mesero':
        flash('Acceso restringido a meseros', 'danger')
        return redirect(url_for('main.dashboard'))
@mesero_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection
    request.bcrypt = current_app.bcrypt

@mesero_bp.route('/dashboard')
def dashboard():
    """Vista principal del mesero con mesas"""
    try:
        mesa_model = Mesa(request.connection)
        mesas = mesa_model.get_all()
        
        return render_template('mesero/dashboard.html', 
                            mesas=mesas,
                            user_role=session.get('user_role'))
    except Exception as e:
        flash(f'Error al cargar el dashboard: {str(e)}', 'danger')
        return redirect(url_for('main.home'))

@mesero_bp.route('/mesas')
def listar_mesas():
    """Lista todas las mesas con su estado actual"""
    try:
        mesa_model = Mesa(request.connection)
        mesas = mesa_model.get_all()
        
        pedido_model = Pedido(request.connection)
        for mesa in mesas:
            mesa['pedido_activo'] = pedido_model.get_pedido_activo(mesa['mesa_id'])
        
        return render_template('mesero/mesas/list.html', 
                            mesas=mesas)
    except Exception as e:
        flash(f'Error al obtener mesas: {str(e)}', 'danger')
        return redirect(url_for('main.home'))

@mesero_bp.route('/mesas/<int:mesa_id>')
def ver_mesa(mesa_id):
    """Muestra los detalles de una mesa específica"""
    try:
        mesa_model = Mesa(request.connection)
        mesa = mesa_model.get_by_id(mesa_id)
        
        if not mesa:
            flash('Mesa no encontrada', 'danger')
            return redirect(url_for('mesero.listar_mesas'))
        
        pedido_model = Pedido(request.connection)
        pedido_activo = pedido_model.get_pedido_activo(mesa_id)
        
        platillo_model = Platillo(request.connection)
        platillos = platillo_model.get_activos()
        
        cliente_model = Cliente(request.connection)
        clientes = cliente_model.get_all()
        
        return render_template('mesero/mesas/detalle.html',
                            mesa=mesa,
                            pedido=pedido_activo,
                            platillos=platillos,
                            clientes=clientes)
    except Exception as e:
        flash(f'Error al obtener mesa: {str(e)}', 'danger')
        return redirect(url_for('mesero.listar_mesas'))

# --------------------------------------------------
# Gestión de Pedidos
# --------------------------------------------------
@mesero_bp.route('/pedidos/nuevo', methods=['POST'])
def crear_pedido():
    """Crea un nuevo pedido para una mesa"""
    try:
        mesa_id = request.form['mesa_id']
        detalles = []
        
        # Procesar platillos seleccionados
        for key, value in request.form.items():
            if key.startswith('platillo_') and int(value) > 0:
                platillo_id = key.replace('platillo_', '')
                detalles.append({
                    'platillo_id': platillo_id,
                    'cantidad': int(value),
                    'precio_unitario': float(request.form[f'precio_{platillo_id}'])
                })
        
        if not detalles:
            flash('Debe agregar al menos un platillo al pedido', 'danger')
            return redirect(url_for('mesero.ver_mesa', mesa_id=mesa_id))
        
        # Crear datos del pedido
        pedido_data = {
            'mesa_id': mesa_id,
            'cliente_id': request.form.get('cliente_id') or None,
            'usuario_id': session['user_id'],
            'notas': request.form.get('notas', ''),
            'detalles': detalles
        }
        
        # Crear el pedido
        pedido_model = Pedido(request.connection)
        pedido_id = pedido_model.crear(pedido_data)
        
        if pedido_id:
            # Cambiar estado de la mesa a "ocupada"
            mesa_model = Mesa(request.connection)
            mesa_model.cambiar_estado(mesa_id, 'ocupada')
            
            flash(f'Pedido #{pedido_id} creado exitosamente!', 'success')
            return redirect(url_for('mesero.ver_pedido', pedido_id=pedido_id))
        else:
            flash('Error al crear el pedido', 'danger')
            return redirect(url_for('mesero.ver_mesa', mesa_id=mesa_id))
    
    except Exception as e:
        flash(f'Error al crear pedido: {str(e)}', 'danger')
        return redirect(url_for('mesero.listar_mesas'))

@mesero_bp.route('/pedidos/<int:pedido_id>')
def ver_pedido(pedido_id):
    """Muestra los detalles de un pedido específico"""
    try:
        pedido_model = Pedido(request.connection)
        pedido = pedido_model.get_by_id(pedido_id)
        
        if not pedido:
            flash('Pedido no encontrado', 'danger')
            return redirect(url_for('mesero.listar_mesas'))
        
        return render_template('mesero/pedidos/detalle.html',
                            pedido=pedido)
    except Exception as e:
        flash(f'Error al obtener pedido: {str(e)}', 'danger')
        return redirect(url_for('mesero.listar_mesas'))

@mesero_bp.route('/pedidos/cerrar/<int:pedido_id>', methods=['POST'])
def cerrar_pedido(pedido_id):
    """Marca un pedido como pagado y libera la mesa"""
    try:
        pedido_model = Pedido(request.connection)
        pedido = pedido_model.get_by_id(pedido_id)
        
        if not pedido:
            flash('Pedido no encontrado', 'danger')
            return redirect(url_for('mesero.listar_mesas'))
        
        # Actualizar estado del pedido
        pedido_model.actualizar_estado(pedido_id, 'pagado')
        
        # Liberar la mesa
        mesa_model = Mesa(request.connection)
        mesa_model.cambiar_estado(pedido['mesa_id'], 'disponible')
        
        flash(f'Pedido #{pedido_id} cerrado exitosamente', 'success')
        return redirect(url_for('mesero.listar_mesas'))
    
    except Exception as e:
        flash(f'Error al cerrar pedido: {str(e)}', 'danger')
        return redirect(url_for('mesero.listar_mesas'))


@mesero_bp.route('/clientes/registrar', methods=['POST'])
def registrar_cliente():
    """Registra un nuevo cliente desde la vista del mesero"""
    try:
        nombre = request.form['nombre']
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        
        cliente_model = Cliente(request.connection)
        cliente_id = cliente_model.crear(nombre, telefono, email)
        
        if cliente_id:
            flash('Cliente registrado exitosamente', 'success')
            return redirect(url_for('mesero.ver_mesa', mesa_id=request.form['mesa_id']))
        else:
            flash('Error al registrar cliente', 'danger')
            return redirect(url_for('mesero.ver_mesa', mesa_id=request.form['mesa_id']))
    
    except Exception as e:
        flash(f'Error al registrar cliente: {str(e)}', 'danger')
        return redirect(url_for('mesero.listar_mesas'))