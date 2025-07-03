from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import os

from app.models.user_model import (
    get_all_users_with_roles,
    get_user_by_email_full,
    update_user,
    delete_user_by_email,
    insert_user
)

from app.models.role_model import get_all_roles  # ✅ separamos los roles en su modelo

user_management_bp = Blueprint('user_management_bp', __name__)
bcrypt = Bcrypt()

@user_management_bp.route('/manage_users')
def manage_users():
    connection = current_app.connection
    users = get_all_users_with_roles(connection)
    return render_template('manage_users.html', users=users)

@user_management_bp.route('/delete_user/<email>', methods=['POST'])
def delete_user(email):
    connection = current_app.connection
    try:
        delete_user_by_email(connection, email)
        flash('Usuario eliminado exitosamente', 'success')
    except Exception as e:
        flash('Error al eliminar el usuario: ' + str(e), 'danger')
    return redirect(url_for('user_management_bp.manage_users'))

@user_management_bp.route('/edit_user/<email>', methods=['GET', 'POST'])
def edit_user(email):
    connection = current_app.connection

    if request.method == 'POST':
        name = request.form['name']
        new_email = request.form['email']
        role_id = request.form['role']

        try:
            update_user(connection, name, new_email, role_id, email)
            flash('Usuario modificado exitosamente', 'success')
        except Exception as e:
            flash('Error al modificar el usuario: ' + str(e), 'danger')

        return redirect(url_for('user_management_bp.manage_users'))

    user = get_user_by_email_full(connection, email)
    roles = get_all_roles(connection)
    return render_template('edit_user.html', user=user, roles=roles)

@user_management_bp.route('/create_user', methods=['GET', 'POST'])
def create_user():
    connection = current_app.connection

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role_id = request.form['role']

        file_path = None
        photo = request.files.get('photo')

        if photo and photo.filename:
            images_dir = os.path.join(current_app.root_path, 'static/uploads/profile_pictures')
            os.makedirs(images_dir, exist_ok=True)

            filename = secure_filename(photo.filename)
            file_path = os.path.join('uploads/profile_pictures', filename).replace("\\", "/")
            photo.save(os.path.join(images_dir, filename))

        try:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            insert_user(connection, name, email, hashed_password, role_id, file_path)
            flash('Usuario creado exitosamente', 'success')
        except Exception as e:
            flash('Error al crear el usuario: ' + str(e), 'danger')

        return redirect(url_for('user_management_bp.manage_users'))

    roles = get_all_roles(connection)
    return render_template('create_user.html', roles=roles)
