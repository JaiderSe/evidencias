import pymysql.cursors
from datetime import datetime

class Pedido:
    def __init__(self, connection):
        """
        Inicializa el modelo con la conexión a la base de datos
        :param connection: Conexión MySQL activa
        """
        self.connection = connection

    # --------------------------------------------------
    # Métodos CRUD Básicos
    # --------------------------------------------------
    def crear(self, pedido_data):
        """
        Crea un nuevo pedido y sus detalles
        :param pedido_data: Diccionario con {
            mesa_id, 
            cliente_id, 
            usuario_id, 
            notas, 
            detalles: [{platillo_id, cantidad, precio_unitario}]
        }
        :return: ID del pedido creado o None en caso de error
        """
        try:
            with self.connection.cursor() as cursor:
                # 1. Crear el pedido principal
                sql_pedido = """
                INSERT INTO pedidos (
                    mesa_id, cliente_id, usuario_id, estado, notas
                ) VALUES (
                    %(mesa_id)s, %(cliente_id)s, %(usuario_id)s, 'recibido', %(notas)s
                )
                """
                cursor.execute(sql_pedido, {
                    'mesa_id': pedido_data['mesa_id'],
                    'cliente_id': pedido_data.get('cliente_id'),
                    'usuario_id': pedido_data['usuario_id'],
                    'notas': pedido_data.get('notas', '')
                })
                pedido_id = cursor.lastrowid

                # 2. Agregar los detalles del pedido
                for detalle in pedido_data['detalles']:
                    sql_detalle = """
                    INSERT INTO detalles_pedido (
                        pedido_id, platillo_id, cantidad, precio_unitario, estado
                    ) VALUES (
                        %s, %s, %s, %s, 'pendiente'
                    )
                    """
                    cursor.execute(sql_detalle, (
                        pedido_id,
                        detalle['platillo_id'],
                        detalle['cantidad'],
                        detalle['precio_unitario']
                    ))

                # 3. Actualizar el total del pedido
                sql_total = """
                UPDATE pedidos 
                SET total = (
                    SELECT SUM(cantidad * precio_unitario) 
                    FROM detalles_pedido 
                    WHERE pedido_id = %s
                )
                WHERE pedido_id = %s
                """
                cursor.execute(sql_total, (pedido_id, pedido_id))

                self.connection.commit()
                return pedido_id

        except pymysql.Error as e:
            print(f"Error al crear pedido: {e}")
            self.connection.rollback()
            return None

    def get_by_id(self, pedido_id):
        """
        Obtiene un pedido por su ID con todos sus detalles
        :param pedido_id: ID del pedido a buscar
        :return: Diccionario con los datos del pedido y sus detalles
        """
        try:
            with self.connection.cursor() as cursor:
                # 1. Obtener información básica del pedido
                sql_pedido = """
                SELECT p.*, 
                    m.numero_mesa, 
                    u.nombre as mesero_nombre,
                    c.nombre as cliente_nombre
                FROM pedidos p
                LEFT JOIN mesas m ON p.mesa_id = m.mesa_id
                LEFT JOIN usuarios u ON p.usuario_id = u.usuario_id
                LEFT JOIN clientes c ON p.cliente_id = c.cliente_id
                WHERE p.pedido_id = %s
                """
                cursor.execute(sql_pedido, (pedido_id,))
                pedido = cursor.fetchone()

                if not pedido:
                    return None

                # 2. Obtener detalles del pedido
                sql_detalles = """
                SELECT d.*, pl.nombre as platillo_nombre
                FROM detalles_pedido d
                JOIN platillos pl ON d.platillo_id = pl.platillo_id
                WHERE d.pedido_id = %s
                ORDER BY d.detalle_id
                """
                cursor.execute(sql_detalles, (pedido_id,))
                detalles = cursor.fetchall()

                # 3. Combinar resultados
                pedido['detalles'] = detalles
                return pedido

        except pymysql.Error as e:
            print(f"Error al obtener pedido {pedido_id}: {e}")
            return None

    # --------------------------------------------------
    # Métodos de Consulta
    # --------------------------------------------------
    def get_all(self):
        """Obtiene todos los pedidos con información básica"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT p.*, 
                    m.numero_mesa, 
                    u.nombre as mesero_nombre,
                    c.nombre as cliente_nombre
                FROM pedidos p
                LEFT JOIN mesas m ON p.mesa_id = m.mesa_id
                LEFT JOIN usuarios u ON p.usuario_id = u.usuario_id
                LEFT JOIN clientes c ON p.cliente_id = c.cliente_id
                ORDER BY p.fecha_hora DESC
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener pedidos: {e}")
            return []

    def get_pedidos_para_cocina(self):
        """Obtiene pedidos con detalles pendientes para la cocina"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT DISTINCT p.*, m.numero_mesa
                FROM pedidos p
                JOIN mesas m ON p.mesa_id = m.mesa_id
                JOIN detalles_pedido d ON p.pedido_id = d.pedido_id
                WHERE p.estado NOT IN ('cancelado', 'pagado')
                AND d.estado IN ('pendiente', 'en preparacion')
                ORDER BY p.fecha_hora ASC
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener pedidos para cocina: {e}")
            return []

    def get_pedido_activo(self, mesa_id):
        """
        Obtiene el pedido activo de una mesa (no pagado/cancelado)
        :param mesa_id: ID de la mesa
        :return: Pedido activo o None si no existe
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT * FROM pedidos 
                WHERE mesa_id = %s 
                AND estado NOT IN ('pagado', 'cancelado')
                ORDER BY fecha_hora DESC
                LIMIT 1
                """
                cursor.execute(sql, (mesa_id,))
                return cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error al obtener pedido activo de mesa {mesa_id}: {e}")
            return None

    # --------------------------------------------------
    # Métodos de Actualización
    # --------------------------------------------------
    def actualizar_estado(self, pedido_id, nuevo_estado):
        """
        Actualiza el estado de un pedido
        :param pedido_id: ID del pedido
        :param nuevo_estado: Nuevo estado del pedido
        :return: True si fue exitoso, False en caso contrario
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE pedidos SET estado = %s WHERE pedido_id = %s"
                cursor.execute(sql, (nuevo_estado, pedido_id))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar estado de pedido {pedido_id}: {e}")
            self.connection.rollback()
            return False

    def actualizar_detalle_estado(self, detalle_id, nuevo_estado, notas_chef=None):
        """
        Actualiza el estado de un detalle de pedido
        :param detalle_id: ID del detalle
        :param nuevo_estado: Nuevo estado
        :param notas_chef: Notas opcionales del chef
        :return: True si fue exitoso, False en caso contrario
        """
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
                
                # Verificar si todos los detalles están listos
                if nuevo_estado == 'listo':
                    sql_check = """
                    SELECT COUNT(*) as pendientes
                    FROM detalles_pedido
                    WHERE pedido_id = (
                        SELECT pedido_id FROM detalles_pedido WHERE detalle_id = %s
                    )
                    AND estado != 'listo'
                    """
                    cursor.execute(sql_check, (detalle_id,))
                    result = cursor.fetchone()
                    if result['pendientes'] == 0:
                        # Actualizar estado del pedido principal
                        sql_update_pedido = """
                        UPDATE pedidos
                        SET estado = 'listo'
                        WHERE pedido_id = (
                            SELECT pedido_id FROM detalles_pedido WHERE detalle_id = %s
                        )
                        """
                        cursor.execute(sql_update_pedido, (detalle_id,))
                        self.connection.commit()
                
                return True
        except pymysql.Error as e:
            print(f"Error al actualizar detalle {detalle_id}: {e}")
            self.connection.rollback()
            return False

    # --------------------------------------------------
    # Métodos de Reportes
    # --------------------------------------------------
    def ventas_por_periodo(self, fecha_inicio, fecha_fin, agrupacion='dia'):
        """
        Obtiene ventas agrupadas por periodo
        :param fecha_inicio: Fecha de inicio (YYYY-MM-DD)
        :param fecha_fin: Fecha de fin (YYYY-MM-DD)
        :param agrupacion: 'dia', 'semana' o 'mes'
        :return: Lista de ventas por periodo
        """
        try:
            with self.connection.cursor() as cursor:
                if agrupacion == 'dia':
                    group_by = "DATE(p.fecha_hora)"
                    formato = "%Y-%m-%d"
                elif agrupacion == 'semana':
                    group_by = "YEARWEEK(p.fecha_hora, 3)"  # 3: Lunes como primer día de semana
                    formato = "%x-W%v"  # Formato ISO para año-semana
                else:  # mes
                    group_by = "DATE_FORMAT(p.fecha_hora, '%Y-%m')"
                    formato = "%Y-%m"

                sql = f"""
                SELECT 
                    {group_by} as periodo,
                    DATE_FORMAT(MIN(p.fecha_hora), '{formato}') as periodo_formateado,
                    COUNT(*) as total_pedidos,
                    SUM(p.total) as total_ventas
                FROM pedidos p
                WHERE p.estado = 'pagado'
                AND DATE(p.fecha_hora) BETWEEN %s AND %s
                GROUP BY {group_by}
                ORDER BY periodo
                """
                cursor.execute(sql, (fecha_inicio, fecha_fin))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener ventas por periodo: {e}")
            return []

    def total_ventas_periodo(self, fecha_inicio, fecha_fin):
        """
        Calcula el total de ventas en un periodo
        :param fecha_inicio: Fecha de inicio (YYYY-MM-DD)
        :param fecha_fin: Fecha de fin (YYYY-MM-DD)
        :return: Total de ventas
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT SUM(total) as total
                FROM pedidos
                WHERE estado = 'pagado'
                AND DATE(fecha_hora) BETWEEN %s AND %s
                """
                cursor.execute(sql, (fecha_inicio, fecha_fin))
                result = cursor.fetchone()
                return result['total'] if result['total'] else 0
        except pymysql.Error as e:
            print(f"Error al calcular total de ventas: {e}")
            return 0

    def count_pedidos_hoy(self):
        """Cuenta los pedidos realizados hoy"""
        hoy = datetime.now().strftime('%Y-%m-%d')
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT COUNT(*) as total
                FROM pedidos
                WHERE DATE(fecha_hora) = %s
                """
                cursor.execute(sql, (hoy,))
                result = cursor.fetchone()
                return result['total'] if result else 0
        except pymysql.Error as e:
            print(f"Error al contar pedidos hoy: {e}")
            return 0

    def ingresos_hoy(self):
        """Calcula los ingresos de pedidos pagados hoy"""
        hoy = datetime.now().strftime('%Y-%m-%d')
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT SUM(total) as total
                FROM pedidos
                WHERE estado = 'pagado'
                AND DATE(fecha_hora) = %s
                """
                cursor.execute(sql, (hoy,))
                result = cursor.fetchone()
                return result['total'] if result['total'] else 0
        except pymysql.Error as e:
            print(f"Error al calcular ingresos hoy: {e}")
            return 0

    def get_ultimos_pedidos(self, limite=5):
        """
        Obtiene los últimos pedidos
        :param limite: Número máximo de pedidos a obtener
        :return: Lista de los últimos pedidos
        """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT p.*, m.numero_mesa
                FROM pedidos p
                JOIN mesas m ON p.mesa_id = m.mesa_id
                ORDER BY p.fecha_hora DESC
                LIMIT %s
                """
                cursor.execute(sql, (limite,))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener últimos pedidos: {e}")
            return []