import pymysql.cursors
from datetime import datetime

class Cliente:
    def __init__(self, connection):
        self.connection = connection

    def crear(self, nombre, telefono=None, email=None, preferencias=None):
        """Registra un nuevo cliente"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO clientes (nombre, telefono, email, preferencias)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (nombre, telefono, email, preferencias))
                self.connection.commit()
                return cursor.lastrowid
        except pymysql.Error as e:
            print(f"Error al crear cliente: {e}")
            self.connection.rollback()
            return None

    def get_all(self):
        """Obtiene todos los clientes registrados"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM clientes 
                ORDER BY fecha_registro DESC
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener clientes: {e}")
            return []

    def get_by_id(self, cliente_id):
        """Obtiene un cliente por su ID"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM clientes WHERE cliente_id = %s"
                cursor.execute(sql, (cliente_id,))
                return cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error al obtener cliente {cliente_id}: {e}")
            return None

    def buscar(self, termino):
        """Busca clientes por nombre, teléfono o email"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM clientes 
                WHERE nombre LIKE %s 
                OR telefono LIKE %s 
                OR email LIKE %s
                ORDER BY nombre
                """
                termino = f"%{termino}%"
                cursor.execute(sql, (termino, termino, termino))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al buscar clientes: {e}")
            return []

    def actualizar(self, cliente_id, nombre=None, telefono=None, email=None, preferencias=None):
        """Actualiza los datos de un cliente"""
        try:
            with self.connection.cursor() as cursor:
                # Construir la consulta dinámicamente
                updates = []
                params = []
                
                if nombre is not None:
                    updates.append("nombre = %s")
                    params.append(nombre)
                if telefono is not None:
                    updates.append("telefono = %s")
                    params.append(telefono)
                if email is not None:
                    updates.append("email = %s")
                    params.append(email)
                if preferencias is not None:
                    updates.append("preferencias = %s")
                    params.append(preferencias)
                
                if not updates:
                    return False
                
                sql = f"UPDATE clientes SET {', '.join(updates)} WHERE cliente_id = %s"
                params.append(cliente_id)
                
                cursor.execute(sql, tuple(params))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar cliente {cliente_id}: {e}")
            self.connection.rollback()
            return False

    def get_favoritos(self, cliente_id):
        """Obtiene los platillos favoritos de un cliente"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT p.* 
                FROM favoritos_clientes f
                JOIN platillos p ON f.platillo_id = p.platillo_id
                WHERE f.cliente_id = %s
                AND p.activo = TRUE
                ORDER BY p.nombre
                """
                cursor.execute(sql, (cliente_id,))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener favoritos del cliente {cliente_id}: {e}")
            return []

    def agregar_favorito(self, cliente_id, platillo_id):
        """Agrega un platillo a los favoritos del cliente"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO favoritos_clientes (cliente_id, platillo_id)
                VALUES (%s, %s)
                """
                cursor.execute(sql, (cliente_id, platillo_id))
                self.connection.commit()
                return True
        except pymysql.Error as e:
            print(f"Error al agregar favorito: {e}")
            self.connection.rollback()
            return False

    def eliminar_favorito(self, cliente_id, platillo_id):
        """Elimina un platillo de los favoritos del cliente"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM favoritos_clientes
                WHERE cliente_id = %s AND platillo_id = %s
                """
                cursor.execute(sql, (cliente_id, platillo_id))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al eliminar favorito: {e}")
            self.connection.rollback()
            return False