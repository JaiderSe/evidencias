DELIMITER $$

CREATE PROCEDURE alquilar_pelicula(
    IN p_customer_id INT,
    IN p_inventory_id INT,
    IN p_staff_id INT
)
BEGIN
    DECLARE rental_id INT;

    -- Insertar en tabla rental
    INSERT INTO rental (rental_date, inventory_id, customer_id, staff_id)
    VALUES (NOW(), p_inventory_id, p_customer_id, p_staff_id);

    SET rental_id = LAST_INSERT_ID();

    -- Insertar el pago
    INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date)
    VALUES (p_customer_id, p_staff_id, rental_id, 2.99, NOW()); -- Asumiendo monto fijo

END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE reporte_ventas()
BEGIN
    SELECT s.store_id, c.city, SUM(p.amount) AS total_ventas
    FROM payment p
    JOIN staff st ON p.staff_id = st.staff_id
    JOIN store s ON st.store_id = s.store_id
    JOIN address a ON s.address_id = a.address_id
    JOIN city c ON a.city_id = c.city_id
    GROUP BY s.store_id, c.city;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER actualizar_last_update
BEFORE UPDATE ON film
FOR EACH ROW
BEGIN
    SET NEW.last_update = NOW();
END$$

DELIMITER ;

DELIMITER $$

CREATE TABLE cambios_pelicula (
    cambio_id INT AUTO_INCREMENT PRIMARY KEY,
    film_id INT,
    titulo_viejo VARCHAR(255),
    titulo_nuevo VARCHAR(255),
    fecha_cambio DATETIME
);

CREATE TRIGGER registrar_cambio_pelicula
BEFORE UPDATE ON film
FOR EACH ROW
BEGIN
    IF OLD.title <> NEW.title THEN
        INSERT INTO cambios_pelicula (film_id, titulo_viejo, titulo_nuevo, fecha_cambio)
        VALUES (OLD.film_id, OLD.title, NEW.title, NOW());
    END IF;
END$$

DELIMITER ;


DELIMITER $$

CREATE FUNCTION calcular_multa(return_date DATETIME, due_date DATETIME)
RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    DECLARE dias_retraso INT;
    SET dias_retraso = DATEDIFF(return_date, due_date);
    RETURN IF(dias_retraso > 0, dias_retraso * 1.50, 0.00); -- Multa de $1.50 por día
END$$

DELIMITER ;
DELIMITER $$

CREATE FUNCTION pelicula_disponible(film_id INT)
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    DECLARE disponibles INT;
    SELECT COUNT(*) INTO disponibles
    FROM inventory i
    WHERE i.film_id = film_id
      AND i.inventory_id NOT IN (
          SELECT inventory_id FROM rental
          WHERE return_date IS NULL
      );
    RETURN disponibles > 0;
END$$

DELIMITER ;

DELIMITER $$

CREATE FUNCTION dias_alquiler_restantes(rental_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE rental_date DATETIME;
    DECLARE duration INT;
    
    SELECT r.rental_date, f.rental_duration
    INTO rental_date, duration
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    WHERE r.rental_id = rental_id;

    RETURN duration - DATEDIFF(NOW(), rental_date);
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE devolver_pelicula(
    IN p_rental_id INT
)
BEGIN
    UPDATE rental
    SET return_date = NOW()
    WHERE rental_id = p_rental_id;
END$$

DELIMITER ;

ALTER TABLE inventory ADD COLUMN disponible BOOLEAN DEFAULT TRUE;

DELIMITER $$

CREATE TRIGGER actualizar_disponibilidad_despues_alquilar
AFTER INSERT ON rental
FOR EACH ROW
BEGIN
    UPDATE inventory
    SET disponible = FALSE
    WHERE inventory_id = NEW.inventory_id;
END$$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER validar_pago_antes_devolucion
BEFORE UPDATE ON rental
FOR EACH ROW
BEGIN
    DECLARE pago_existente INT;
    
    IF NEW.return_date IS NOT NULL AND OLD.return_date IS NULL THEN
        SELECT COUNT(*) INTO pago_existente
        FROM payment
        WHERE rental_id = OLD.rental_id;

        IF pago_existente = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se puede devolver la película sin realizar el pago.';
        END IF;
    END IF;
END$$

DELIMITER ;
