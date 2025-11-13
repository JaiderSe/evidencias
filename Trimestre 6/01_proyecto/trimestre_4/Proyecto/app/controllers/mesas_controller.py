from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from app.models.mesa import Mesa

mesas_bp = Blueprint('mesa', __name__)

@mesas_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection
    request.bcrypt = current_app.bcrypt

@mesas_bp.route('/')
def listar_mesas():
    """Lista todas las mesas del restaurante"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'mesero']:
            flash('No tienes permisos para esta sección', 'danger')
            return redirect(url_for('main.dashboard'))
        
        mesa_model = Mesa(request.connection)
        mesas = mesa_model.get_all()
        
        return render_template('mesas/list.html',
                            mesas=mesas,
                            user_role=session.get('user_role'))
    
    except Exception as e:
        flash(f'Error al obtener mesas: {str(e)}', 'danger')
        return redirect(url_for('main.home'))

@mesas_bp.route('/crear', methods=['GET', 'POST'])
def crear_mesa():
    """Crea una nueva mesa"""
    try:
        # Verificar permisos
        if session.get('user_role') != 'administrador':
            flash('Solo los administradores pueden crear mesas', 'danger')
            return redirect(url_for('mesas.listar_mesas'))
        
        if request.method == 'POST':
            # Validación básica
            required_fields = ['numero_mesa', 'capacidad', 'ubicacion']
            if not all(field in request.form for field in required_fields):
                flash('Todos los campos obligatorios deben estar completos', 'danger')
                return redirect(url_for('mesas.crear_mesa'))
            
            mesa_data = {
                'numero_mesa': request.form['numero_mesa'],
                'capacidad': int(request.form['capacidad']),
                'ubicacion': request.form['ubicacion'],
                'estado': 'disponible'
            }
            
            mesa_model = Mesa(request.connection)
            mesa_id = mesa_model.crear(mesa_data)
            
            flash(f'Mesa {mesa_data["numero_mesa"]} creada exitosamente!', 'success')
            return redirect(url_for('mesas.listar_mesas'))
        
        return render_template('mesas/form.html',
                            mesa=None,
                            accion='Crear')
    
    except Exception as e:
        flash(f'Error al crear mesa: {str(e)}', 'danger')
        return redirect(url_for('mesas.listar_mesas'))

@mesas_bp.route('/editar/<int:mesa_id>', methods=['GET', 'POST'])
def editar_mesa(mesa_id):
    """Edita una mesa existente"""
    try:
        # Verificar permisos
        if session.get('user_role') != 'administrador':
            flash('Solo los administradores pueden editar mesas', 'danger')
            return redirect(url_for('mesas.listar_mesas'))
        
        mesa_model = Mesa(request.connection)
        mesa = mesa_model.get_by_id(mesa_id)
        
        if not mesa:
            flash('Mesa no encontrada', 'danger')
            return redirect(url_for('mesas.listar_mesas'))
        
        if request.method == 'POST':
            # Validación básica
            required_fields = ['numero_mesa', 'capacidad', 'ubicacion']
            if not all(field in request.form for field in required_fields):
                flash('Todos los campos obligatorios deben estar completos', 'danger')
                return redirect(url_for('mesas.editar_mesa', mesa_id=mesa_id))
            
            mesa_data = {
                'numero_mesa': request.form['numero_mesa'],
                'capacidad': int(request.form['capacidad']),
                'ubicacion': request.form['ubicacion']
            }
            
            mesa_model.actualizar(mesa_id, mesa_data)
            
            flash(f'Mesa {mesa_data["numero_mesa"]} actualizada exitosamente!', 'success')
            return redirect(url_for('mesas.listar_mesas'))
        
        return render_template('mesas/form.html',
                            mesa=mesa,
                            accion='Editar')
    
    except Exception as e:
        flash(f'Error al editar mesa: {str(e)}', 'danger')
        return redirect(url_for('mesas.listar_mesas'))

@mesas_bp.route('/cambiar-estado/<int:mesa_id>', methods=['POST'])
def cambiar_estado(mesa_id):
    """Cambia el estado de una mesa (AJAX)"""
    try:
        if not request.is_json:
            return jsonify({'error': 'Solicitud no válida'}), 400
            
        data = request.get_json()
        nuevo_estado = data.get('estado')
        
        if not nuevo_estado:
            return jsonify({'error': 'Estado no proporcionado'}), 400
        
        mesa_model = Mesa(request.connection)
        if mesa_model.cambiar_estado(mesa_id, nuevo_estado):
            return jsonify({
                'success': True,
                'nuevo_estado': nuevo_estado,
                'badge_class': get_badge_class(nuevo_estado)
            })
        else:
            return jsonify({'error': 'Error al actualizar'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_badge_class(estado):
    """Devuelve la clase CSS según el estado de la mesa"""
    classes = {
        'disponible': 'bg-success',
        'ocupada': 'bg-danger',
        'reservada': 'bg-warning',
        'mantenimiento': 'bg-secondary'
    }
    return classes.get(estado, 'bg-primary')