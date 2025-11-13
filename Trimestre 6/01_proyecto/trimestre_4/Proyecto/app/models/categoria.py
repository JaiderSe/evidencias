import pymysql.cursors

class Categoria:
    def __init__(self, connection):
        self.connection = connection

    def crear(self, nombre, descripcion=None, orden_menu=None):
        """Crea una nueva categoría de platillos"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO categorias (nombre, descripcion, orden_menu)
                VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (nombre, descripcion, orden_menu))
                self.connection.commit()
                return cursor.lastrowid
        except pymysql.Error as e:
            print(f"Error al crear categoría: {e}")
            self.connection.rollback()
            return None

    def get_all(self):
        """Obtiene todas las categorías ordenadas"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM categorias 
                ORDER BY orden_menu IS NULL, orden_menu, nombre
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener categorías: {e}")
            return []

    def get_by_id(self, categoria_id):
        """Obtiene una categoría por su ID"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM categorias WHERE categoria_id = %s"
                cursor.execute(sql, (categoria_id,))
                return cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error al obtener categoría {categoria_id}: {e}")
            return None

    def actualizar(self, categoria_id, nombre, descripcion=None, orden_menu=None):
        """Actualiza una categoría existente"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                UPDATE categorias 
                SET nombre = %s, descripcion = %s, orden_menu = %s
                WHERE categoria_id = %s
                """
                cursor.execute(sql, (nombre, descripcion, orden_menu, categoria_id))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar categoría {categoria_id}: {e}")
            self.connection.rollback()
            return False

    def eliminar(self, categoria_id):
        """Elimina una categoría (si no tiene platillos asociados)"""
        try:
            with self.connection.cursor() as cursor:
                # Verificar si hay platillos asociados
                sql_check = """
                SELECT COUNT(*) as total 
                FROM platillos 
                WHERE categoria_id = %s
                """
                cursor.execute(sql_check, (categoria_id,))
                result = cursor.fetchone()
                
                if result['total'] > 0:
                    return False
                
                # Eliminar la categoría
                sql_delete = "DELETE FROM categorias WHERE categoria_id = %s"
                cursor.execute(sql_delete, (categoria_id,))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al eliminar categoría {categoria_id}: {e}")
            self.connection.rollback()
            return False

    def get_platillos(self, categoria_id):
        """Obtiene todos los platillos de una categoría"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM platillos 
                WHERE categoria_id = %s AND activo = TRUE
                ORDER BY nombre
                """
                cursor.execute(sql, (categoria_id,))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener platillos de categoría {categoria_id}: {e}")
            return []