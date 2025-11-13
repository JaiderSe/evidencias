from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.platillo import Platillo
from app.models.categoria import Categoria
from werkzeug.utils import secure_filename
import os

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection
    request.bcrypt = current_app.bcrypt

@menu_bp.route('/')
def listar_platillos():
    """Lista todos los platillos del menú"""
    try:
        # Verificar rol de usuario
        if session.get('user_role') not in ['administrador', 'chef']:
            flash('No tienes permisos para esta sección', 'danger')
            return redirect(url_for('main.home'))
        
        # Obtener platillos y categorías
        platillo_model = Platillo(request.connection)
        categoria_model = Categoria(request.connection)
        
        platillos = platillo_model.get_all()
        categorias = categoria_model.get_all()
        
        return render_template('menu/list.html',
                            platillos=platillos,
                            categorias=categorias)
    
    except Exception as e:
        flash(f'Error al obtener el menú: {str(e)}', 'danger')
        return redirect(url_for('main.home'))

@menu_bp.route('/crear', methods=['GET', 'POST'])
def crear_platillo():
    """Crea un nuevo platillo en el menú"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'chef']:
            flash('No tienes permisos para esta acción', 'danger')
            return redirect(url_for('menu.listar_platillos'))
        
        categoria_model = Categoria(request.connection)
        categorias = categoria_model.get_all()
        
        if request.method == 'POST':
            # Validar datos del formulario
            nombre = request.form.get('nombre')
            categoria_id = request.form.get('categoria_id')
            precio = request.form.get('precio')
            
            if not all([nombre, categoria_id, precio]):
                flash('Todos los campos son requeridos', 'danger')
                return redirect(url_for('menu.crear_platillo'))
            
            # Procesar imagen
            imagen_url = None
            if 'imagen' in request.files:
                imagen = request.files['imagen']
                if imagen.filename != '':
                    filename = secure_filename(imagen.filename)
                    upload_folder = os.path.join(current_app.root_path, 'static/img/platillos')
                    os.makedirs(upload_folder, exist_ok=True)
                    filepath = os.path.join(upload_folder, filename)
                    imagen.save(filepath)
                    imagen_url = f'img/platillos/{filename}'
            
            # Crear platillo
            platillo_data = {
                'nombre': nombre,
                'categoria_id': categoria_id,
                'descripcion': request.form.get('descripcion'),
                'precio': float(precio),
                'tiempo_preparacion': request.form.get('tiempo_preparacion', 20),
                'es_vegano': bool(request.form.get('es_vegano')),
                'es_vegetariano': bool(request.form.get('es_vegetariano')),
                'tiene_gluten': bool(request.form.get('tiene_gluten', True)),
                'nivel_picante': int(request.form.get('nivel_picante', 0)),
                'imagen_url': imagen_url
            }
            
            platillo_model = Platillo(request.connection)
            platillo_id = platillo_model.crear(platillo_data)
            
            flash(f'Platillo {nombre} creado exitosamente!', 'success')
            return redirect(url_for('menu.listar_platillos'))
        
        return render_template('menu/form.html',
                            categorias=categorias,
                            platillo=None,
                            accion='Crear')
    
    except ValueError:
        flash('Datos inválidos en el formulario', 'danger')
        return redirect(url_for('menu.crear_platillo'))
    except Exception as e:
        flash(f'Error al crear platillo: {str(e)}', 'danger')
        return redirect(url_for('menu.listar_platillos'))