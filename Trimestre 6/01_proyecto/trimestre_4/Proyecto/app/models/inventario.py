import pymysql.cursors
from datetime import datetime

class Inventario:
    def __init__(self, connection):
        self.connection = connection

    def registrar_movimiento(self, ingrediente_id, usuario_id, cantidad, 
                           tipo_movimiento, motivo=None, costo_total=None):
        """Registra un movimiento de inventario"""
        try:
            with self.connection.cursor() as cursor:
                # 1. Registrar el movimiento
                sql_movimiento = """
                INSERT INTO inventario (
                    ingrediente_id, usuario_id, cantidad, tipo_movimiento,
                    motivo, costo_total
                ) VALUES (
                    %s, %s, %s, %s, %s, %s
                )
                """
                cursor.execute(sql_movimiento, (
                    ingrediente_id, usuario_id, cantidad, tipo_movimiento,
                    motivo, costo_total
                ))
                
                # 2. Actualizar el stock del ingrediente
                if tipo_movimiento == 'entrada':
                    sql_update = """
                    UPDATE ingredientes 
                    SET stock_actual = stock_actual + %s
                    WHERE ingrediente_id = %s
                    """
                else:  # salida o ajuste
                    sql_update = """
                    UPDATE ingredientes 
                    SET stock_actual = stock_actual - %s
                    WHERE ingrediente_id = %s
                    """
                
                cursor.execute(sql_update, (cantidad, ingrediente_id))
                
                self.connection.commit()
                return cursor.lastrowid
        except pymysql.Error as e:
            print(f"Error al registrar movimiento de inventario: {e}")
            self.connection.rollback()
            return None

    def get_movimientos(self, ingrediente_id=None, fecha_inicio=None, fecha_fin=None):
        """Obtiene los movimientos de inventario con filtros opcionales"""
        try:
            with self.connection.cursor() as cursor:
                # Construir la consulta dinámicamente
                where_clauses = []
                params = []
                
                if ingrediente_id:
                    where_clauses.append("i.ingrediente_id = %s")
                    params.append(ingrediente_id)
                
                if fecha_inicio:
                    where_clauses.append("DATE(iv.fecha) >= %s")
                    params.append(fecha_inicio)
                
                if fecha_fin:
                    where_clauses.append("DATE(iv.fecha) <= %s")
                    params.append(fecha_fin)
                
                where = "WHERE " + " AND ".join(where_clauses) if where_clauses else ""
                
                sql = f"""
                SELECT iv.*, i.nombre as ingrediente_nombre,
                       u.nombre as usuario_nombre
                FROM inventario iv
                JOIN ingredientes i ON iv.ingrediente_id = i.ingrediente_id
                JOIN usuarios u ON iv.usuario_id = u.usuario_id
                {where}
                ORDER BY iv.fecha DESC
                """
                
                cursor.execute(sql, tuple(params))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener movimientos de inventario: {e}")
            return []

    def get_historial_ingrediente(self, ingrediente_id, limite=30):
        """Obtiene el historial de movimientos de un ingrediente"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                SELECT iv.*, u.nombre as usuario_nombre
                FROM inventario iv
                JOIN usuarios u ON iv.usuario_id = u.usuario_id
                WHERE iv.ingrediente_id = %s
                ORDER BY iv.fecha DESC
                LIMIT %s
                """
                cursor.execute(sql, (ingrediente_id, limite))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener historial del ingrediente {ingrediente_id}: {e}")
            return []

    def get_resumen_mensual(self, año=None, mes=None):
        """Genera un resumen de movimientos por mes"""
        try:
            with self.connection.cursor() as cursor:
                # Si no se especifica año/mes, usar el actual
                if año is None or mes is None:
                    hoy = datetime.now()
                    año = año or hoy.year
                    mes = mes or hoy.month
                
                sql = """
                SELECT 
                    i.ingrediente_id,
                    i.nombre as ingrediente_nombre,
                    i.unidad_medida,
                    SUM(CASE WHEN iv.tipo_movimiento = 'entrada' THEN iv.cantidad ELSE 0 END) as entradas,
                    SUM(CASE WHEN iv.tipo_movimiento = 'salida' THEN iv.cantidad ELSE 0 END) as salidas,
                    SUM(CASE WHEN iv.tipo_movimiento = 'ajuste' THEN iv.cantidad ELSE 0 END) as ajustes,
                    SUM(CASE WHEN iv.tipo_movimiento = 'entrada' THEN iv.costo_total ELSE 0 END) as costo_entradas
                FROM inventario iv
                JOIN ingredientes i ON iv.ingrediente_id = i.ingrediente_id
                WHERE YEAR(iv.fecha) = %s AND MONTH(iv.fecha) = %s
                GROUP BY i.ingrediente_id, i.nombre, i.unidad_medida
                ORDER BY i.nombre
                """
                cursor.execute(sql, (año, mes))
                return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al generar resumen mensual: {e}")
            return []