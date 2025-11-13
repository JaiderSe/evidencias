import pymysql.cursors

class DetallePedido:
    def __init__(self, connection):
        self.connection = connection

    def get_by_pedido(self, pedido_id):
        """Obtiene todos los detalles de un pedido"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT d.*, p.nombre as platillo_nombre
                FROM detalles_pedido d
                JOIN platillos p ON d.platillo_id = p.platillo_id
                WHERE d.pedido_id = %s
                ORDER BY d.detalle_id
                """
                cursor.execute(sql, (pedido_id,))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener detalles del pedido {pedido_id}: {e}")
            return []

    def actualizar_estado(self, detalle_id, nuevo_estado, notas_chef=None):
        """Actualiza el estado de un detalle de pedido"""
        try:
            with self.connection.cursor() as cursor:
                if notas_chef:
                    sql = """
                    UPDATE detalles_pedido
                    SET estado = %s, notas_chef = %s
                    WHERE detalle_id = %s
                    """
                    cursor.execute(sql, (nuevo_estado, notas_chef, detalle_id))
                else:
                    sql = """
                    UPDATE detalles_pedido
                    SET estado = %s
                    WHERE detalle_id = %s
                    """
                    cursor.execute(sql, (nuevo_estado, detalle_id))
                
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar detalle {detalle_id}: {e}")
            self.connection.rollback()
            return False

    def get_pendientes_cocina(self):
        """Obtiene todos los detalles pendientes para la cocina"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT d.*, p.nombre as platillo_nombre, 
                       m.numero_mesa, pe.fecha_hora
                FROM detalles_pedido d
                JOIN platillos p ON d.platillo_id = p.platillo_id
                JOIN pedidos pe ON d.pedido_id = pe.pedido_id
                JOIN mesas m ON pe.mesa_id = m.mesa_id
                WHERE d.estado IN ('pendiente', 'en preparacion')
                ORDER BY pe.fecha_hora ASC, d.detalle_id ASC
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener detalles pendientes: {e}")
            return []

    def get_by_id(self, detalle_id):
        """Obtiene un detalle específico por su ID"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT d.*, p.nombre as platillo_nombre,
                       m.numero_mesa, pe.pedido_id
                FROM detalles_pedido d
                JOIN platillos p ON d.platillo_id = p.platillo_id
                JOIN pedidos pe ON d.pedido_id = pe.pedido_id
                JOIN mesas m ON pe.mesa_id = m.mesa_id
                WHERE d.detalle_id = %s
                """
                cursor.execute(sql, (detalle_id,))
                return cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error al obtener detalle {detalle_id}: {e}")
            return None