from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename
from app.models.platillo import Platillo
from app.models.categoria import Categoria
import os

platillos_bp = Blueprint('platillo', __name__, url_prefix='/platillos')

@platillos_bp.route('/')
def listar_platillos():
    """Lista todos los platillos del menú"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'chef']:
            flash('No tienes permisos para esta sección', 'danger')
            return redirect(url_for('main.home'))
        
        platillo_model = Platillo(request.connection)
        categoria_model = Categoria(request.connection)
        
        platillos = platillo_model.get_all()
        categorias = categoria_model.get_all()
        
        return render_template('platillos/list.html',
                            platillos=platillos,
                            categorias=categorias)
    
    except Exception as e:
        flash(f'Error al obtener platillos: {str(e)}', 'danger')
        return redirect(url_for('main.home'))

@platillos_bp.route('/crear', methods=['GET', 'POST'])
def crear_platillo():
    """Crea un nuevo platillo en el menú"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'chef']:
            flash('No tienes permisos para esta acción', 'danger')
            return redirect(url_for('platillos.listar_platillos'))
        
        categoria_model = Categoria(request.connection)
        categorias = categoria_model.get_all()
        
        if request.method == 'POST':
            # Validación básica
            required_fields = ['nombre', 'categoria_id', 'precio', 'tiempo_preparacion']
            if not all(field in request.form for field in required_fields):
                flash('Todos los campos obligatorios deben estar completos', 'danger')
                return redirect(url_for('platillos.crear_platillo'))
            
            # Procesar imagen
            imagen_url = None
            if 'imagen' in request.files:
                imagen = request.files['imagen']
                if imagen.filename != '':
                    # Validar y guardar imagen
                    if not allowed_file(imagen.filename):
                        flash('Tipo de archivo no permitido para imágenes', 'danger')
                        return redirect(url_for('platillos.crear_platillo'))
                    
                    filename = secure_filename(imagen.filename)
                    upload_folder = os.path.join(current_app.root_path, 'static/img/platillos')
                    os.makedirs(upload_folder, exist_ok=True)
                    filepath = os.path.join(upload_folder, filename)
                    imagen.save(filepath)
                    imagen_url = f'img/platillos/{filename}'
            
            # Preparar datos del platillo
            platillo_data = {
                'nombre': request.form['nombre'],
                'categoria_id': request.form['categoria_id'],
                'descripcion': request.form.get('descripcion', ''),
                'precio': float(request.form['precio']),
                'tiempo_preparacion': int(request.form['tiempo_preparacion']),
                'es_vegano': 'es_vegano' in request.form,
                'es_vegetariano': 'es_vegetariano' in request.form,
                'tiene_gluten': 'tiene_gluten' in request.form,
                'nivel_picante': int(request.form.get('nivel_picante', 0)),
                'imagen_url': imagen_url,
                'activo': 'activo' in request.form
            }
            
            # Crear platillo
            platillo_model = Platillo(request.connection)
            platillo_id = platillo_model.crear(platillo_data)
            
            flash(f'Platillo "{platillo_data["nombre"]}" creado exitosamente!', 'success')
            return redirect(url_for('platillos.listar_platillos'))
        
        return render_template('platillos/form.html',
                            categorias=categorias,
                            platillo=None,
                            accion='Crear')
    
    except Exception as e:
        flash(f'Error al crear platillo: {str(e)}', 'danger')
        return redirect(url_for('platillos.listar_platillos'))

@platillos_bp.route('/editar/<int:platillo_id>', methods=['GET', 'POST'])
def editar_platillo(platillo_id):
    """Edita un platillo existente"""
    try:
        # Verificar permisos
        if session.get('user_role') not in ['administrador', 'chef']:
            flash('No tienes permisos para esta acción', 'danger')
            return redirect(url_for('platillos.listar_platillos'))
        
        platillo_model = Platillo(request.connection)
        categoria_model = Categoria(request.connection)
        
        platillo = platillo_model.get_by_id(platillo_id)
        if not platillo:
            flash('Platillo no encontrado', 'danger')
            return redirect(url_for('platillos.listar_platillos'))
        
        if request.method == 'POST':
            # Validación básica
            required_fields = ['nombre', 'categoria_id', 'precio', 'tiempo_preparacion']
            if not all(field in request.form for field in required_fields):
                flash('Todos los campos obligatorios deben estar completos', 'danger')
                return redirect(url_for('platillos.editar_platillo', platillo_id=platillo_id))
            
            # Procesar imagen (si se subió una nueva)
            imagen_url = platillo['imagen_url']
            if 'imagen' in request.files:
                imagen = request.files['imagen']
                if imagen.filename != '':
                    if not allowed_file(imagen.filename):
                        flash('Tipo de archivo no permitido para imágenes', 'danger')
                        return redirect(url_for('platillos.editar_platillo', platillo_id=platillo_id))
                    
                    filename = secure_filename(imagen.filename)
                    upload_folder = os.path.join(current_app.root_path, 'static/img/platillos')
                    os.makedirs(upload_folder, exist_ok=True)
                    filepath = os.path.join(upload_folder, filename)
                    imagen.save(filepath)
                    imagen_url = f'img/platillos/{filename}'
            
            # Preparar datos actualizados
            platillo_data = {
                'nombre': request.form['nombre'],
                'categoria_id': request.form['categoria_id'],
                'descripcion': request.form.get('descripcion', ''),
                'precio': float(request.form['precio']),
                'tiempo_preparacion': int(request.form['tiempo_preparacion']),
                'es_vegano': 'es_vegano' in request.form,
                'es_vegetariano': 'es_vegetariano' in request.form,
                'tiene_gluten': 'tiene_gluten' in request.form,
                'nivel_picante': int(request.form.get('nivel_picante', 0)),
                'imagen_url': imagen_url,
                'activo': 'activo' in request.form
            }
            
            # Actualizar platillo
            platillo_model.actualizar(platillo_id, platillo_data)
            
            flash(f'Platillo "{platillo_data["nombre"]}" actualizado exitosamente!', 'success')
            return redirect(url_for('platillos.listar_platillos'))
        
        categorias = categoria_model.get_all()
        return render_template('platillos/form.html',
                            categorias=categorias,
                            platillo=platillo,
                            accion='Editar')
    
    except Exception as e:
        flash(f'Error al editar platillo: {str(e)}', 'danger')
        return redirect(url_for('platillos.listar_platillos'))

def allowed_file(filename):
    """Verifica que el archivo sea una imagen permitida"""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS