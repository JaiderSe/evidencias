from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.models.ingrediente import Ingrediente
from app.models.inventario import Inventario
from datetime import datetime

inventario_bp = Blueprint('inventario', __name__, url_prefix='/inventario')

@inventario_bp.before_request
def check_inventario():
    """Verifica que el usuario sea de inventario antes de cada solicitud"""
    if session.get('user_role') != 'inventario':
        flash('Acceso restringido a personal de inventario', 'danger')
        return redirect(url_for('main.dashboard'))

@inventario_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection
    request.bcrypt = current_app.bcrypt

@inventario_bp.route('/dashboard')
def dashboard():
    """Vista principal de inventario con alertas"""
    try:
        ingrediente_model = Ingrediente(request.connection)
        ingredientes_bajo_stock = ingrediente_model.get_bajo_stock()
        
        return render_template('inventario/dashboard.html', 
                            ingredientes=ingredientes_bajo_stock)
    except Exception as e:
        flash(f'Error al cargar el dashboard: {str(e)}', 'danger')
        return redirect(url_for('main.dashboard'))


@inventario_bp.route('/ingredientes')
def listar_ingredientes():
    """Lista todos los ingredientes"""
    try:
        ingrediente_model = Ingrediente(request.connection)
        ingredientes = ingrediente_model.get_all()
        
        return render_template('inventario/ingredientes/list.html', 
                            ingredientes=ingredientes)
    except Exception as e:
        flash(f'Error al obtener ingredientes: {str(e)}', 'danger')
        return redirect(url_for('inventario.dashboard'))

@inventario_bp.route('/ingredientes/<int:ingrediente_id>')
def ver_ingrediente(ingrediente_id):
    """Muestra los detalles de un ingrediente"""    
    try:
        ingrediente_model = Ingrediente(request.connection)
        inventario_model = Inventario(request.connection)
        
        ingrediente = ingrediente_model.get_by_id(ingrediente_id)
        if not ingrediente:
            flash('Ingrediente no encontrado', 'danger')
            return redirect(url_for('inventario.listar_ingredientes'))
        
        historial = inventario_model.get_historial_ingrediente(ingrediente_id)
        
        return render_template('inventario/ingredientes/detalle.html', 
                            ingrediente=ingrediente,
                            historial=historial)
    except Exception as e:
        flash(f'Error al obtener ingrediente: {str(e)}', 'danger')
        return redirect(url_for('inventario.listar_ingredientes'))

@inventario_bp.route('/movimientos/entrada', methods=['GET', 'POST'])
def registrar_entrada():
    """Registra una entrada de inventario"""
    try:
        ingrediente_model = Ingrediente(request.connection)
        
        if request.method == 'POST':
            ingrediente_id = request.form['ingrediente_id']
            cantidad = float(request.form['cantidad'])
            
            inventario_model = Inventario(request.connection)
            movimiento_id = inventario_model.registrar_movimiento(
                ingrediente_id=ingrediente_id,
                usuario_id=session['user_id'],
                cantidad=cantidad,
                tipo_movimiento='entrada',
                motivo=request.form.get('motivo'),
                costo_total=request.form.get('costo_total')
            )
            
            if movimiento_id:
                flash('Entrada de inventario registrada', 'success')
                return redirect(url_for('inventario.ver_ingrediente', ingrediente_id=ingrediente_id))
            else:
                flash('Error al registrar entrada', 'danger')
        
        ingredientes = ingrediente_model.get_all()
        return render_template('inventario/movimientos/entrada.html',
                            ingredientes=ingredientes)
    
    except Exception as e:
        flash(f'Error al registrar entrada: {str(e)}', 'danger')
        return redirect(url_for('inventario.dashboard'))

@inventario_bp.route('/movimientos/salida', methods=['GET', 'POST'])
def registrar_salida():
    """Registra una salida de inventario"""
    try:
        ingrediente_model = Ingrediente(request.connection)
        
        if request.method == 'POST':
            ingrediente_id = request.form['ingrediente_id']
            cantidad = float(request.form['cantidad'])
            
            # Verificar stock disponible
            ingrediente = ingrediente_model.get_by_id(ingrediente_id)
            if ingrediente['stock_actual'] < cantidad:
                flash('Stock insuficiente para esta salida', 'danger')
                return redirect(url_for('inventario.registrar_salida'))
            
            inventario_model = Inventario(request.connection)
            movimiento_id = inventario_model.registrar_movimiento(
                ingrediente_id=ingrediente_id,
                usuario_id=session['user_id'],
                cantidad=cantidad,
                tipo_movimiento='salida',
                motivo=request.form.get('motivo')
            )
            
            if movimiento_id:
                flash('Salida de inventario registrada', 'success')
                return redirect(url_for('inventario.ver_ingrediente', ingrediente_id=ingrediente_id))
            else:
                flash('Error al registrar salida', 'danger')
        
        ingredientes = ingrediente_model.get_all()
        return render_template('inventario/movimientos/salida.html',
                            ingredientes=ingredientes)
    
    except Exception as e:
        flash(f'Error al registrar salida: {str(e)}', 'danger')
        return redirect(url_for('inventario.dashboard'))

@inventario_bp.route('/movimientos/ajuste', methods=['GET', 'POST'])
def registrar_ajuste():
    """Registra un ajuste de inventario"""
    try:
        ingrediente_model = Ingrediente(request.connection)
        
        if request.method == 'POST':
            ingrediente_id = request.form['ingrediente_id']
            cantidad = float(request.form['cantidad'])
            tipo_ajuste = request.form['tipo_ajuste']  # 'incremento' o 'decremento'
            
            if tipo_ajuste == 'decremento':
                # Verificar stock disponible para decrementos
                ingrediente = ingrediente_model.get_by_id(ingrediente_id)
                if ingrediente['stock_actual'] < cantidad:
                    flash('Stock insuficiente para este ajuste', 'danger')
                    return redirect(url_for('inventario.registrar_ajuste'))
            
            inventario_model = Inventario(request.connection)
            movimiento_id = inventario_model.registrar_movimiento(
                ingrediente_id=ingrediente_id,
                usuario_id=session['user_id'],
                cantidad=cantidad,
                tipo_movimiento='ajuste',
                motivo=f"Ajuste de inventario ({tipo_ajuste}): {request.form.get('motivo')}"
            )
            
            if movimiento_id:
                flash('Ajuste de inventario registrado', 'success')
                return redirect(url_for('inventario.ver_ingrediente', ingrediente_id=ingrediente_id))
            else:
                flash('Error al registrar ajuste', 'danger')
        
        ingredientes = ingrediente_model.get_all()
        return render_template('inventario/movimientos/ajuste.html',
                            ingredientes=ingredientes)
    
    except Exception as e:
        flash(f'Error al registrar ajuste: {str(e)}', 'danger')
        return redirect(url_for('inventario.dashboard'))

# --------------------------------------------------
# Reportes de Inventario
# --------------------------------------------------
@inventario_bp.route('/reportes/mensual')
def reporte_mensual():
    """Genera un reporte mensual de movimientos"""
    try:
        año = request.args.get('año', datetime.now().year, type=int)
        mes = request.args.get('mes', datetime.now().month, type=int)
        
        inventario_model = Inventario(request.connection)
        resumen = inventario_model.get_resumen_mensual(año, mes)
        
        return render_template('inventario/reportes/mensual.html',
                            resumen=resumen,
                            año=año,
                            mes=mes)
    except Exception as e:
        flash(f'Error al generar reporte: {str(e)}', 'danger')
        return redirect(url_for('inventario.dashboard'))
    
@inventario_bp.route('/ingredientes/nuevo', methods=['GET', 'POST'])
def editar_ingrediente(ingrediente_id):
    """Edita un ingrediente existente"""
    try:
        ingrediente_model = Ingrediente(request.connection)
        
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            stock_minimo = float(request.form['stock_minimo'])
            stock_maximo = float(request.form['stock_maximo'])
            
            if ingrediente_model.update_ingrediente(ingrediente_id, nombre, descripcion, stock_minimo, stock_maximo):
                flash('Ingrediente actualizado correctamente', 'success')
                return redirect(url_for('inventario.ver_ingrediente', ingrediente_id=ingrediente_id))
            else:
                flash('Error al actualizar ingrediente', 'danger')
        
        ingrediente = ingrediente_model.get_by_id(ingrediente_id)
        if not ingrediente:
            flash('Ingrediente no encontrado', 'danger')
            return redirect(url_for('inventario.listar_ingredientes'))
        
        return render_template('inventario/ingredientes/editar.html', 
                            ingrediente=ingrediente)
    
    except Exception as e:
        flash(f'Error al editar ingrediente: {str(e)}', 'danger')
        return redirect(url_for('inventario.listar_ingredientes'))
    
def crear_ingrediente():
    """Crea un nuevo ingrediente"""
    try:
        ingrediente_model = Ingrediente(request.connection)
        
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            stock_minimo = float(request.form['stock_minimo'])
            stock_maximo = float(request.form['stock_maximo'])
            
            if ingrediente_model.create_ingrediente(nombre, descripcion, stock_minimo, stock_maximo):
                flash('Ingrediente creado correctamente', 'success')
                return redirect(url_for('inventario.listar_ingredientes'))
            else:
                flash('Error al crear ingrediente', 'danger')
        
        return render_template('inventario/ingredientes/nuevo.html')
    
    except Exception as e:
        flash(f'Error al crear ingrediente: {str(e)}', 'danger')
        return redirect(url_for('inventario.listar_ingredientes'))