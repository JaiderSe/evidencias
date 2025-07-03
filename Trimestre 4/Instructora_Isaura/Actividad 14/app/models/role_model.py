# app/models/role_model.py
def get_all_roles(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM roles")
        return cursor.fetchall()
