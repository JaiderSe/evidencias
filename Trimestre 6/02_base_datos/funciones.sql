DELIMITER //
CREATE FUNCTION fn_verificar_disponibilidad_ingrediente(
    p_platillo_id INT,
    p_cantidad INT
) RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    DECLARE v_disponible BOOLEAN DEFAULT TRUE;
    DECLARE v_ingrediente_id INT;
    DECLARE v_cantidad_necesaria DECIMAL(10,2);
    DECLARE v_stock_actual DECIMAL(10,2);
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT ingrediente_id, cantidad 
        FROM platillo_ingredientes 
        WHERE platillo_id = p_platillo_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_ingrediente_id, v_cantidad_necesaria;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        SELECT stock_actual INTO v_stock_actual 
        FROM ingredientes 
        WHERE ingrediente_id = v_ingrediente_id;
        
        IF (v_cantidad_necesaria * p_cantidad) > v_stock_actual THEN
            SET v_disponible = FALSE;
            LEAVE read_loop;
        END IF;
    END LOOP;
    CLOSE cur;
    
    RETURN v_disponible;
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION fn_tiempo_preparacion_pedido(
    p_pedido_id INT
) RETURNS INT
READS SQL DATA
BEGIN
    DECLARE v_tiempo_total INT DEFAULT 0;
    
    SELECT SUM(pl.tiempo_preparacion * dp.cantidad) INTO v_tiempo_total
    FROM detalles_pedido dp
    JOIN platillos pl ON dp.platillo_id = pl.platillo_id
    WHERE dp.pedido_id = p_pedido_id;
    
    RETURN IFNULL(v_tiempo_total, 0);
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION fn_platillo_mas_popular(
    p_dias INT
) RETURNS VARCHAR(100)
READS SQL DATA
BEGIN
    DECLARE v_nombre_platillo VARCHAR(100);
    
    SELECT pl.nombre INTO v_nombre_platillo
    FROM detalles_pedido dp
    JOIN platillos pl ON dp.platillo_id = pl.platillo_id
    JOIN pedidos p ON dp.pedido_id = p.pedido_id
    WHERE p.fecha_hora >= DATE_SUB(CURRENT_DATE(), INTERVAL p_dias DAY)
    GROUP BY dp.platillo_id, pl.nombre
    ORDER BY SUM(dp.cantidad) DESC
    LIMIT 1;
    
    RETURN IFNULL(v_nombre_platillo, 'No hay datos');
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION fn_ingredientes_caducando(
    p_dias INT
) RETURNS INT
READS SQL DATA
BEGIN
    DECLARE v_count INT;
    
    SELECT COUNT(*) INTO v_count
    FROM ingredientes
    WHERE caduca = TRUE 
    AND dias_caducidad <= p_dias
    AND stock_actual > 0;
    
    RETURN v_count;
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION fn_calcular_propina(
    p_pedido_id INT,
    p_porcentaje DECIMAL(5,2)
) RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN
    DECLARE v_total DECIMAL(10,2);
    
    SELECT total INTO v_total FROM pedidos WHERE pedido_id = p_pedido_id;
    
    RETURN ROUND(v_total * (p_porcentaje / 100), 2);
END //
DELIMITER ;

