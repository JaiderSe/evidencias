--store procedures
DELIMITER //
CREATE PROCEDURE sp_registrar_pedido(
    IN p_mesa_id INT,
    IN p_cliente_id INT,
    IN p_usuario_id INT,
    IN p_notas TEXT
)
BEGIN
    DECLARE v_pedido_id INT;
    
    INSERT INTO pedidos (mesa_id, cliente_id, usuario_id, notas, estado)
    VALUES (p_mesa_id, p_cliente_id, p_usuario_id, p_notas, 'recibido');
    
    SET v_pedido_id = LAST_INSERT_ID();
    
    -- Actualizar estado de la mesa
    UPDATE mesas SET estado = 'ocupada' WHERE mesa_id = p_mesa_id;
    
    SELECT v_pedido_id AS nuevo_pedido_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_agregar_platillo_pedido(
    IN p_pedido_id INT,
    IN p_platillo_id INT,
    IN p_cantidad INT,
    IN p_personalizaciones TEXT
)
BEGIN
    DECLARE v_precio DECIMAL(10,2);
    
    -- Obtener precio actual del platillo
    SELECT precio INTO v_precio FROM platillos WHERE platillo_id = p_platillo_id;
    
    -- Insertar detalle
    INSERT INTO detalles_pedido (pedido_id, platillo_id, cantidad, precio_unitario, personalizaciones)
    VALUES (p_pedido_id, p_platillo_id, p_cantidad, v_precio, p_personalizaciones);
    
    -- Actualizar total del pedido
    UPDATE pedidos 
    SET total = (SELECT SUM(cantidad * precio_unitario) FROM detalles_pedido WHERE pedido_id = p_pedido_id)
    WHERE pedido_id = p_pedido_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_ajustar_inventario(
    IN p_ingrediente_id INT,
    IN p_usuario_id INT,
    IN p_cantidad DECIMAL(10,2),
    IN p_tipo_movimiento ENUM('entrada', 'salida', 'ajuste'),
    IN p_motivo TEXT
)
BEGIN
    DECLARE v_costo DECIMAL(10,2);
    
    -- Obtener costo por unidad
    SELECT costo_por_unidad INTO v_costo FROM ingredientes WHERE ingrediente_id = p_ingrediente_id;
    
    -- Registrar movimiento
    INSERT INTO inventario (ingrediente_id, usuario_id, cantidad, tipo_movimiento, motivo, costo_total)
    VALUES (p_ingrediente_id, p_usuario_id, p_cantidad, p_tipo_movimiento, p_motivo, p_cantidad * v_costo);
    
    -- Actualizar stock
    IF p_tipo_movimiento = 'entrada' THEN
        UPDATE ingredientes 
        SET stock_actual = stock_actual + p_cantidad 
        WHERE ingrediente_id = p_ingrediente_id;
    ELSE
        UPDATE ingredientes 
        SET stock_actual = stock_actual - p_cantidad 
        WHERE ingrediente_id = p_ingrediente_id;
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_reporte_ventas(
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE
)
BEGIN
    SELECT 
        p.platillo_id,
        pl.nombre AS platillo_nombre,
        SUM(p.cantidad) AS total_vendido,
        SUM(p.cantidad * p.precio_unitario) AS total_ingresos,
        c.nombre AS categoria
    FROM 
        detalles_pedido p
        JOIN platillos pl ON p.platillo_id = pl.platillo_id
        JOIN categorias c ON pl.categoria_id = c.categoria_id
        JOIN pedidos pe ON p.pedido_id = pe.pedido_id
    WHERE 
        DATE(pe.fecha_hora) BETWEEN p_fecha_inicio AND p_fecha_fin
    GROUP BY 
        p.platillo_id, pl.nombre, c.nombre
    ORDER BY 
        total_vendido DESC;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_cambiar_estado_pedido(
    IN p_pedido_id INT,
    IN p_nuevo_estado ENUM('recibido', 'en preparacion', 'listo', 'entregado', 'cancelado', 'pagado')
)
BEGIN
    DECLARE v_mesa_id INT;
    
    -- Actualizar estado del pedido
    UPDATE pedidos SET estado = p_nuevo_estado WHERE pedido_id = p_pedido_id;
    
    -- Si el pedido se marca como pagado o cancelado, liberar la mesa
    IF p_nuevo_estado IN ('pagado', 'cancelado') THEN
        SELECT mesa_id INTO v_mesa_id FROM pedidos WHERE pedido_id = p_pedido_id;
        
        IF v_mesa_id IS NOT NULL THEN
            UPDATE mesas SET estado = 'disponible' WHERE mesa_id = v_mesa_id;
        END IF;
    END IF;
END //
DELIMITER ;
