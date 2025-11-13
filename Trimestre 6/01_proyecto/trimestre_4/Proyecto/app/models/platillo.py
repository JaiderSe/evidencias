import pymysql.cursors

class Platillo:
    def __init__(self, connection):
        """
        Constructor que recibe la conexión a la base de datos
        :param connection: Conexión MySQL activa
        """
        self.connection = connection
        
    def crear(self, platillo_data):
        """
        Crea un nuevo platillo en la base de datos
        :param platillo_data: Diccionario con los datos del platillo
        :return: ID del platillo creado o None en caso de error
        """
        try:
            with self.connection.cursor() as cursor:
                # Consulta SQL parametrizada para evitar inyecciones
                sql = """
                INSERT INTO platillos (
                    nombre, categoria_id, descripcion, precio, 
                    tiempo_preparacion, activo, es_vegano, 
                    es_vegetariano, tiene_gluten, nivel_picante, imagen_url
                ) VALUES (
                    %(nombre)s, %(categoria_id)s, %(descripcion)s, %(precio)s,
                    %(tiempo_preparacion)s, %(activo)s, %(es_vegano)s,
                    %(es_vegetariano)s, %(tiene_gluten)s, %(nivel_picante)s, %(imagen_url)s
                )
                """
                # Ejecutar la consulta
                cursor.execute(sql, platillo_data)
                # Confirmar la transacción
                self.connection.commit()
                # Devolver el ID del nuevo platillo
                return cursor.lastrowid
        except pymysql.Error as e:
            print(f"Error al crear platillo: {e}")
            self.connection.rollback()
            return None
    def get_all(self):
        """
        Obtiene todos los platillos activos con información de categoría
        :return: Lista de diccionarios con los platillos o lista vacía en caso de error
        """
        try:
            with self.connection.cursor() as cursor:
                # Consulta que hace JOIN con categorías
                sql = """
                SELECT p.*, c.nombre as categoria_nombre 
                FROM platillos p
                LEFT JOIN categorias c ON p.categoria_id = c.categoria_id
                WHERE p.activo = TRUE
                ORDER BY p.nombre
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener platillos: {e}")
            return []
    def get_by_id(self, platillo_id):
        """
        Obtiene un platillo específico por su ID
        :param platillo_id: ID del platillo a buscar
        :return: Diccionario con los datos del platillo o None si no existe
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT p.*, c.nombre as categoria_nombre 
                FROM platillos p
                LEFT JOIN categorias c ON p.categoria_id = c.categoria_id
                WHERE p.platillo_id = %s
                """
                cursor.execute(sql, (platillo_id,))
                return cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error al obtener platillo {platillo_id}: {e}")
            return None
    def actualizar(self, platillo_id, platillo_data):
        """
        Actualiza los datos de un platillo existente
        :param platillo_id: ID del platillo a actualizar
        :param platillo_data: Diccionario con los nuevos datos
        :return: True si fue exitoso, False en caso contrario
        """
        try:
            with self.connection.cursor() as cursor:
                # Construir la consulta dinámicamente
                set_clause = ", ".join([f"{key} = %({key})s" for key in platillo_data.keys()])
                sql = f"""
                UPDATE platillos 
                SET {set_clause}
                WHERE platillo_id = %(platillo_id)s
                """
                
                # Agregar el ID a los datos
                platillo_data['platillo_id'] = platillo_id
                
                cursor.execute(sql, platillo_data)
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar platillo {platillo_id}: {e}")
            self.connection.rollback()
            return False
    def desactivar(self, platillo_id):
        """
        Desactiva un platillo (borrado lógico)
        :param platillo_id: ID del platillo a desactivar
        :return: True si fue exitoso, False en caso contrario
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                UPDATE platillos 
                SET activo = FALSE
                WHERE platillo_id = %s
                """
                cursor.execute(sql, (platillo_id,))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al desactivar platillo {platillo_id}: {e}")
            self.connection.rollback()
            return False
    def get_por_categoria(self, categoria_id):
        """Obtiene platillos por categoría"""
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
            print(f"Error al obtener platillos por categoría {categoria_id}: {e}")
            return []

    def buscar(self, termino):
        """Busca platillos por término"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM platillos 
                WHERE (nombre LIKE %s OR descripcion LIKE %s) 
                AND activo = TRUE
                ORDER BY nombre
                """
                termino_busqueda = f"%{termino}%"
                cursor.execute(sql, (termino_busqueda, termino_busqueda))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al buscar platillos: {e}")
            return []
        
    def get_activos(self):
        """Obtiene todos los platillos activos"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM platillos 
                WHERE activo = TRUE
                ORDER BY nombre
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener platillos activos: {e}")
            return []
