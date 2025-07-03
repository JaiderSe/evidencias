# app/models/category_model.py
def get_category_count(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS category_count FROM categories")
        return cursor.fetchone()['category_count']
