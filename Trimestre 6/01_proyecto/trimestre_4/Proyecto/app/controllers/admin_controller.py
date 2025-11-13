from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app
from app.models.user import User
from app.models.pedido import Pedido
from app.models.platillo import Platillo
from app.models.mesa import Mesa
from datetime import datetime, timedelta

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection
    request.bcrypt = current_app.bcrypt

@admin_bp.before_request
def check_admin():
    """Verifica que el usuario sea administrador antes de cada solicitud"""
    if session.get('user_role') != 'administrador':
        flash('Acceso restringido a administradores', 'danger')
        return redirect(url_for('admin.dashboard'))

# --------------------------------------------------
# Dashboard Administrativo
# --------------------------------------------------
@admin_bp.route('/dashboard')
def dashboard():
    try:
        # Obtener estadísticas rápidas
        user_model = User(request.connection)
        pedido_model = Pedido(request.connection)
        mesa_model = Mesa(request.connection)
        
        total_usuarios = user_model.count()
        pedidos_hoy = pedido_model.count_pedidos_hoy()
        ingresos_hoy = pedido_model.ingresos_hoy()
        mesas_ocupadas = mesa_model.count_by_estado('ocupada')
        
        # Últimos 5 pedidos
        ultimos_pedidos = pedido_model.get_ultimos_pedidos(5)
        
        return render_template('admin/dashboard.html',
                            total_usuarios=total_usuarios,
                            pedidos_hoy=pedidos_hoy,
                            ingresos_hoy=ingresos_hoy,
                            mesas_ocupadas=mesas_ocupadas,
                            ultimos_pedidos=ultimos_pedidos)
    
    except Exception as e:
        flash(f'Error al cargar el dashboard: {str(e)}', 'danger')
        return redirect(url_for('admin.listar_usuarios'))


# Gestión de Usuarios

@admin_bp.route('/usuarios')
def listar_usuarios():
    try:
        user_model = User(request.connection)
        usuarios = user_model.get_all()
        return render_template('admin/usuarios/list.html', usuarios=usuarios)
    
    except Exception as e:
        flash(f'Error al obtener usuarios: {str(e)}', 'danger')
        return redirect(url_for('admin.dashboard'))

@admin_bp.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            email = request.form['email']
            password = request.form['password']
            rol = request.form['rol']
            
            user_model = User(request.connection)
            existing_user = user_model.get_user_by_email(email)
            
            # Verificar si el email ya existe
            if existing_user:
                flash('El correo electrónico ya está registrado', 'danger')
                return redirect(url_for('admin.crear_usuario'))
            
            # Crear usuario
            user_model.create_user(nombre, email, password, rol)
            flash('Usuario creado exitosamente', 'success')
            return redirect(url_for('admin.listar_usuarios'))
        
        except Exception as e:
            flash(f'Error al crear usuario: {str(e)}', 'danger')
    
    return render_template('admin/usuarios/form.html', accion='Crear')

@admin_bp.route('/usuarios/editar/<int:usuario_id>', methods=['GET', 'POST'])
def editar_usuario(usuario_id):
    try:
        user_model = User(request.connection)
        usuario = user_model.get_by_id(usuario_id)
        
        if not usuario:
            flash('Usuario no encontrado', 'danger')
            return redirect(url_for('admin.listar_usuarios'))
        
        if request.method == 'POST':
            nombre = request.form['nombre']
            email = request.form['email']
            rol = request.form['rol']
            activo = 'activo' in request.form
            
            # Actualizar usuario
            user_model.actualizar(usuario_id, nombre, email, rol, activo)
            flash('Usuario actualizado exitosamente', 'success')
            return redirect(url_for('admin.listar_usuarios'))
        
        return render_template('admin/usuarios/form.html', 
                            usuario=usuario,
                            accion='Editar')
    
    except Exception as e:
        flash(f'Error al editar usuario: {str(e)}', 'danger')
        return redirect(url_for('admin.listar_usuarios'))


# Reportes y Estadísticas

@admin_bp.route('/reportes/ventas')
def reporte_ventas():
    try:
        pedido_model = Pedido(request.connection)
        
        # Parámetros de fecha (últimos 30 días por defecto)
        fecha_inicio = request.args.get('fecha_inicio', 
                                      (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
        fecha_fin = request.args.get('fecha_fin', 
                                   datetime.now().strftime('%Y-%m-%d'))
        
        # Datos para gráficos
        ventas_por_dia = pedido_model.ventas_por_periodo(fecha_inicio, fecha_fin, 'dia')
        ventas_por_categoria = pedido_model.ventas_por_categoria(fecha_inicio, fecha_fin)
        total_ventas = pedido_model.total_ventas_periodo(fecha_inicio, fecha_fin)
        
        return render_template('admin/reportes/ventas.html',
                            ventas_por_dia=ventas_por_dia,
                            ventas_por_categoria=ventas_por_categoria,
                            total_ventas=total_ventas,
                            fecha_inicio=fecha_inicio,
                            fecha_fin=fecha_fin)
    
    except Exception as e:
        flash(f'Error al generar reporte: {str(e)}', 'danger')
        return redirect(url_for('admin.dashboard'))

# --------------------------------------------------
# Configuración del Sistema
# --------------------------------------------------
@admin_bp.route('/configuracion', methods=['GET', 'POST'])
def configuracion():
    if request.method == 'POST':
        try:
            # Aquí iría la lógica para guardar configuraciones
            flash('Configuración actualizada exitosamente', 'success')
            return redirect(url_for('admin.configuracion'))
        
        except Exception as e:
            flash(f'Error al guardar configuración: {str(e)}', 'danger')
    
    return render_template('admin/configuracion.html')

@admin_bp.route('/pedidos/<int:pedido_id>')
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