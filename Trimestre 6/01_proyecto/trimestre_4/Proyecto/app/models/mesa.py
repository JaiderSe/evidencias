import pymysql.cursors
from datetime import datetime

class Mesa:
    def __init__(self, connection):
        """
        Inicializa el modelo con la conexión a la base de datos
        :param connection: Conexión MySQL activa
        """
        self.connection = connection

    # --------------------------------------------------
    # Métodos CRUD Básicos
    # --------------------------------------------------
    def crear(self, mesa_data):
        """
        Crea una nueva mesa en la base de datos
        :param mesa_data: Diccionario con {numero_mesa, capacidad, ubicacion}
        :return: ID de la mesa creada o None en caso de error
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO mesas (numero_mesa, capacidad, ubicacion, estado)
                VALUES (%(numero_mesa)s, %(capacidad)s, %(ubicacion)s, 'disponible')
                """
                cursor.execute(sql, mesa_data)
                self.connection.commit()
                return cursor.lastrowid
        except pymysql.Error as e:
            print(f"Error al crear mesa: {e}")
            self.connection.rollback()
            return None

    def get_by_id(self, mesa_id):
        """
        Obtiene una mesa por su ID
        :param mesa_id: ID de la mesa a buscar
        :return: Diccionario con los datos de la mesa o None si no existe
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM mesas WHERE mesa_id = %s"
                cursor.execute(sql, (mesa_id,))
                return cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error al obtener mesa {mesa_id}: {e}")
            return None

    def get_all(self):
        """
        Obtiene todas las mesas
        :return: Lista de diccionarios con las mesas
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM mesas ORDER BY numero_mesa"
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener mesas: {e}")
            return []

    def actualizar(self, mesa_id, mesa_data):
        """
        Actualiza los datos de una mesa
        :param mesa_id: ID de la mesa a actualizar
        :param mesa_data: Diccionario con los nuevos datos
        :return: True si fue exitoso, False en caso contrario
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                UPDATE mesas 
                SET numero_mesa = %(numero_mesa)s, 
                    capacidad = %(capacidad)s, 
                    ubicacion = %(ubicacion)s
                WHERE mesa_id = %(mesa_id)s
                """
                mesa_data['mesa_id'] = mesa_id
                cursor.execute(sql, mesa_data)
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar mesa {mesa_id}: {e}")
            self.connection.rollback()
            return False

    # --------------------------------------------------
    # Métodos Específicos de Negocio
    # --------------------------------------------------
    def cambiar_estado(self, mesa_id, nuevo_estado):
        """
        Cambia el estado de una mesa
        :param mesa_id: ID de la mesa
        :param nuevo_estado: Nuevo estado (disponible, ocupada, reservada, mantenimiento)
        :return: True si fue exitoso, False en caso contrario
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE mesas SET estado = %s WHERE mesa_id = %s"
                cursor.execute(sql, (nuevo_estado, mesa_id))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al cambiar estado de mesa {mesa_id}: {e}")
            self.connection.rollback()
            return False

    def get_by_estado(self, estado):
        """
        Obtiene mesas por estado
        :param estado: Estado a filtrar
        :return: Lista de mesas en ese estado
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM mesas WHERE estado = %s ORDER BY numero_mesa"
                cursor.execute(sql, (estado,))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener mesas por estado {estado}: {e}")
            return []

    def count_by_estado(self, estado):
        """
        Cuenta cuántas mesas hay en un estado específico
        :param estado: Estado a contar
        :return: Número de mesas en ese estado
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT COUNT(*) as total FROM mesas WHERE estado = %s"
                cursor.execute(sql, (estado,))
                result = cursor.fetchone()
                return result['total'] if result else 0
        except pymysql.Error as e:
            print(f"Error al contar mesas por estado {estado}: {e}")
            return 0

    def get_disponibles(self):
        """Obtiene todas las mesas disponibles"""
        return self.get_by_estado('disponible')

    def get_ocupadas(self):
        """Obtiene todas las mesas ocupadas"""
        return self.get_by_estado('ocupada')

    # --------------------------------------------------
    # Métodos para Relaciones
    # --------------------------------------------------
    def get_pedidos_activos(self, mesa_id):
        """
        Obtiene los pedidos activos de una mesa
        :param mesa_id: ID de la mesa
        :return: Lista de pedidos no pagados/cancelados
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM pedidos 
                WHERE mesa_id = %s 
                AND estado NOT IN ('pagado', 'cancelado')
                ORDER BY fecha_hora DESC
                """
                cursor.execute(sql, (mesa_id,))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener pedidos activos de mesa {mesa_id}: {e}")
            return []