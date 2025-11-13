import pymysql.cursors

class Ingrediente:
    def __init__(self, connection):
        self.connection = connection

    def crear(self, nombre, unidad_medida, stock_actual, stock_minimo, 
              proveedor_principal=None, costo_por_unidad=None, caduca=False, dias_caducidad=None):
        """Registra un nuevo ingrediente"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO ingredientes (
                    nombre, unidad_medida, stock_actual, stock_minimo,
                    proveedor_principal, costo_por_unidad, caduca, dias_caducidad
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s
                )
                """
                cursor.execute(sql, (
                    nombre, unidad_medida, stock_actual, stock_minimo,
                    proveedor_principal, costo_por_unidad, caduca, dias_caducidad
                ))
                self.connection.commit()
                return cursor.lastrowid
        except pymysql.Error as e:
            print(f"Error al crear ingrediente: {e}")
            self.connection.rollback()
            return None

    def get_all(self):
        """Obtiene todos los ingredientes"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM ingredientes ORDER BY ingrediente_id ASC"
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener ingredientes: {e}")
            return []

    def get_by_id(self, ingrediente_id):
        """Obtiene un ingrediente por su ID"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM ingredientes WHERE ingrediente_id = %s"
                cursor.execute(sql, (ingrediente_id,))
                return cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error al obtener ingrediente {ingrediente_id}: {e}")
            return None

    def actualizar(self, ingrediente_id, **kwargs):
        """Actualiza los datos de un ingrediente"""
        try:
            with self.connection.cursor() as cursor:
                # Construir la consulta dinámicamente
                updates = []
                params = []
                
                for key, value in kwargs.items():
                    updates.append(f"{key} = %s")
                    params.append(value)
                
                if not updates:
                    return False
                
                sql = f"UPDATE ingredientes SET {', '.join(updates)} WHERE ingrediente_id = %s"
                params.append(ingrediente_id)
                
                cursor.execute(sql, tuple(params))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar ingrediente {ingrediente_id}: {e}")
            self.connection.rollback()
            return False

    def get_bajo_stock(self):
        """Obtiene ingredientes con stock por debajo del mínimo"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM ingredientes
                WHERE stock_actual < stock_minimo
                ORDER BY (stock_actual/stock_minimo) ASC
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener ingredientes con bajo stock: {e}")
            return []

    def get_por_platillo(self, platillo_id):
        """Obtiene los ingredientes de un platillo (receta)"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT i.*, pi.cantidad, pi.notas
                FROM platillo_ingredientes pi
                JOIN ingredientes i ON pi.ingrediente_id = i.ingrediente_id
                WHERE pi.platillo_id = %s
                ORDER BY i.nombre
                """
                cursor.execute(sql, (platillo_id,))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener ingredientes del platillo {platillo_id}: {e}")
            return []