use restausync;

CREATE TABLE IF NOT EXISTS logs_pedidos (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    estado_anterior VARCHAR(20),
    estado_nuevo VARCHAR(20),
    fecha_cambio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id)
);

DELIMITER //
CREATE TRIGGER tr_actualizar_stock_after_insert_detalle
AFTER INSERT ON detalles_pedido
FOR EACH ROW
BEGIN
    DECLARE v_ingrediente_id INT;
    DECLARE v_cantidad_necesaria DECIMAL(10,2);
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT ingrediente_id, cantidad 
        FROM platillo_ingredientes 
        WHERE platillo_id = NEW.platillo_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_ingrediente_id, v_cantidad_necesaria;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Actualizar stock (restar)
        UPDATE ingredientes 
        SET stock_actual = stock_actual - (v_cantidad_necesaria * NEW.cantidad)
        WHERE ingrediente_id = v_ingrediente_id;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER tr_verificar_stock_minimo
AFTER UPDATE ON ingredientes
FOR EACH ROW
BEGIN
    IF NEW.stock_actual < NEW.stock_minimo THEN
        INSERT INTO inventario (
            ingrediente_id, 
            usuario_id, 
            cantidad, 
            tipo_movimiento, 
            motivo, 
            costo_total
        )
        VALUES (
            NEW.ingrediente_id,
            1, -- Usuario sistema
            NEW.stock_minimo * 2, -- Cantidad sugerida para reabastecer
            'entrada',
            'Reabastecimiento automático por stock mínimo',
            NEW.costo_por_unidad * (NEW.stock_minimo * 2)
        );
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER tr_log_cambios_pedidos
AFTER UPDATE ON pedidos
FOR EACH ROW
BEGIN
    IF OLD.estado != NEW.estado THEN
        INSERT INTO logs_pedidos (
            pedido_id,
            estado_anterior,
            estado_nuevo,
            fecha_cambio
        )
        VALUES (
            NEW.pedido_id,
            OLD.estado,
            NEW.estado,
            NOW()
        );
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER tr_validar_email_usuario
BEFORE INSERT ON usuarios
FOR EACH ROW
BEGIN
    IF NEW.email NOT LIKE '%@%.%' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El formato del email no es válido';
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER tr_actualizar_disponibilidad_platillo
AFTER UPDATE ON ingredientes
FOR EACH ROW
BEGIN
    DECLARE v_platillo_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT DISTINCT platillo_id 
        FROM platillo_ingredientes 
        WHERE ingrediente_id = NEW.ingrediente_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_platillo_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Verificar disponibilidad de todos los ingredientes
        IF NOT fn_verificar_disponibilidad_ingrediente(v_platillo_id, 1) THEN
            UPDATE platillos SET activo = FALSE WHERE platillo_id = v_platillo_id;
        ELSE
            UPDATE platillos SET activo = TRUE WHERE platillo_id = v_platillo_id;
        END IF;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;

