# app/controllers/user_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, current_app, session
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import os

from app.models.user_model import get_user_by_email, insert_user, get_user_basic_profile
from app.models.role_model import get_all_roles

user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = current_app.connection
        user = get_user_by_email(connection, email)
        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_role'] = user['role_id']
            return redirect(url_for('user_bp.dashboard'))
        else:
            return "Login Failed"

    return render_template('login.html')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    connection = current_app.connection

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        role = request.form['role']

        photo = request.files.get('photo')
        file_path = None
        if photo and photo.filename:
            images_dir = os.path.join(current_app.root_path, 'static/uploads/profile_pictures')
            os.makedirs(images_dir, exist_ok=True)
            filename = secure_filename(photo.filename)
            file_path = os.path.join('uploads/profile_pictures', filename).replace("\\", "/")
            photo.save(os.path.join(images_dir, filename))

        insert_user(connection, name, email, password, role, file_path)
        return redirect(url_for('user_bp.login'))

    roles = get_all_roles(connection)
    return render_template('register.html', roles=roles)

@user_bp.route('/dashboard')
def dashboard():
    role_id = session.get('user_role')
    if role_id == 1:
        return redirect(url_for('admin_bp.admin_dashboard'))
    elif role_id == 2:
        return redirect(url_for('seller_bp.seller_dashboard'))
    elif role_id == 3:
        return redirect(url_for('baker_bp.baker_dashboard'))
    return "Invalid Role"

@user_bp.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_bp.login'))

    user = get_user_basic_profile(current_app.connection, user_id)
    return render_template('profile.html', user=user)

@user_bp.route('/logout')
def logout():
    session.clear()
    return render_template('home.html')
