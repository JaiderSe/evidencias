# app/models/user_model.py

def get_user_by_email(connection, email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, password, role_id FROM usuarios WHERE email=%s", (email,))
        return cursor.fetchone()

def get_user_by_id(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, profile_picture FROM usuarios WHERE id=%s", (user_id,))
        return cursor.fetchone()

def insert_user(connection, name, email, hashed_password, role_id, profile_picture):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO usuarios (name, email, password, role_id, profile_picture) VALUES (%s, %s, %s, %s, %s)",
            (name, email, hashed_password, role_id, profile_picture)
        )
        connection.commit()

def get_user_basic_profile(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, email, role_id FROM usuarios WHERE id=%s", (user_id,))
        return cursor.fetchone()

def get_all_users_with_roles(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.name, u.email, r.role_name
            FROM usuarios u
            JOIN roles r ON u.role_id = r.id
        """)
        return cursor.fetchall()

def get_user_by_email_full(connection, email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, email, role_id FROM usuarios WHERE email=%s", (email,))
        return cursor.fetchone()

def update_user(connection, name, new_email, role_id, old_email):
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE usuarios 
            SET name=%s, email=%s, role_id=%s 
            WHERE email=%s
        """, (name, new_email, role_id, old_email))
        connection.commit()

def delete_user_by_email(connection, email):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE email=%s", (email,))
        connection.commit()

