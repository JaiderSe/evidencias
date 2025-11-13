from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from app.services.auth_service import AuthService
from app.forms import LoginForm, RegistrationForm
from app.utils.decorators import logout_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
service = AuthService()

@auth_bp.route('/login', methods=['GET', 'POST'])
@logout_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = service.authenticate_user(form.email.data, form.password.data)
        if user:
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            next_page = request.args.get('next') or url_for('menu.list_dishes')
            return redirect(next_page)
        else:
            flash('Email o contraseña incorrectos', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
@logout_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user_data = {
            'nombre': form.nombre.data,
            'email': form.email.data,
            'password': hashed_password,
            'rol': form.rol.data
        }
        service.create_user(user_data)
        flash('Registro exitoso. Por favor inicie sesión.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('auth.login'))