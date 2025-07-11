# app/models/product_model.py
def get_product_count(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS product_count FROM products")
        return cursor.fetchone()['product_count']
