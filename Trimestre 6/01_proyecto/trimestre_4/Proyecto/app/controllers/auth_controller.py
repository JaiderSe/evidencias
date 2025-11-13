from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.before_request
def before_request():
    # Ahora podemos acceder a la conexión y bcrypt a través de current_app
    from flask import current_app
    request.connection = current_app.connection
    request.bcrypt = current_app.bcrypt

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':    
        email = request.form['email']
        password = request.form['password']
        user_model = User(request.connection)
        user_model.bcrypt = request.bcrypt  # Asignar bcrypt al modelo
        user = user_model.get_user_by_email(email)
        
        if user and user_model.verify_password(user, password):
            session['user_id'] = user['usuario_id']
            session['user_name'] = user['nombre']
            session['user_role'] = user['rol']
            flash('Inicio de sesión exitoso!', 'success')
            # Redirigir o renderizar según el rol del usuario
            if user['rol'] == 'administrador':
                return redirect(url_for('admin.dashboard'))
            elif user['rol'] == 'chef':
                return redirect(url_for('chef.dashboard'))
            elif user['rol'] == 'mesero':
                return redirect(url_for('mesero.dashboard'))
            elif user['rol'] == 'inventario':
                return redirect(url_for('inventario.dashboard'))
            
            else:
                return render_template('main/index.html')
        else:
            flash('Correo o contraseña incorrectos', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        rol = 'mesero'  
        
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'danger')
            return redirect(url_for('auth.register'))
        
        user_model = User(request.connection)
        existing_user = user_model.get_user_by_email(email)
        
        if existing_user:
            flash('El correo ya está registrado', 'danger')
            return redirect(url_for('auth.register'))
        
        try:
            user_model.create_user(nombre, email, password, rol)
            flash('Registro exitoso! Por favor inicia sesión', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('Error al registrar el usuario', 'danger')
    
    return render_template('auth/register.html')

@auth_bp.route('/dashboard')
def redirect_to_dashboard():
        user_role = session.get('user_role')
        if user_role == 'administrador':
            return redirect(url_for('admin.dashboard'))
        elif user_role == 'chef':
            return redirect(url_for('chef.dashboard'))
        elif user_role == 'mesero':
            return redirect(url_for('mesero.dashboard'))
        elif user_role == 'inventario':
            return redirect(url_for('inventario.dashboard'))
        else:
            return redirect(url_for('main.home'))

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('auth.login'))