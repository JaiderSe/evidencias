-- Consultas para el modelo Platillo
INSERT INTO platillos (
    nombre, categoria_id, descripcion, precio, 
    tiempo_preparacion, activo, es_vegano, 
    es_vegetariano, tiene_gluten, nivel_picante, imagen_url
) VALUES (
    %(nombre)s, %(categoria_id)s, %(descripcion)s, %(precio)s,
    %(tiempo_preparacion)s, %(activo)s, %(es_vegano)s,
    %(es_vegetariano)s, %(tiene_gluten)s, %(nivel_picante)s, %(imagen_url)s
);

SELECT p.*, c.nombre as categoria_nombre 
FROM platillos p
LEFT JOIN categorias c ON p.categoria_id = c.categoria_id
WHERE p.activo = TRUE
ORDER BY p.nombre;

SELECT p.*, c.nombre as categoria_nombre 
FROM platillos p
LEFT JOIN categorias c ON p.categoria_id = c.categoria_id
WHERE p.platillo_id = %s;

UPDATE platillos 
SET {columna1} = %({columna1})s, {columna2} = %({columna2})s, ...
WHERE platillo_id = %(platillo_id)s;

UPDATE platillos 
SET activo = FALSE
WHERE platillo_id = %s;

SELECT * FROM platillos 
WHERE categoria_id = %s AND activo = TRUE
ORDER BY nombre;

SELECT * FROM platillos 
WHERE (nombre LIKE %s OR descripcion LIKE %s) 
AND activo = TRUE
ORDER BY nombre;

SELECT * FROM platillos 
WHERE activo = TRUE
ORDER BY nombre;

-- Consultas para el modelo Pedido
INSERT INTO pedidos (
    mesa_id, cliente_id, usuario_id, estado, notas
) VALUES (
    %(mesa_id)s, %(cliente_id)s, %(usuario_id)s, 'recibido', %(notas)s
);

INSERT INTO detalles_pedido (
    pedido_id, platillo_id, cantidad, precio_unitario, estado
) VALUES (
    %s, %s, %s, %s, 'pendiente'
);

UPDATE pedidos 
SET total = (
    SELECT SUM(cantidad * precio_unitario) 
    FROM detalles_pedido 
    WHERE pedido_id = %s
)
WHERE pedido_id = %s;

SELECT p.*, 
    m.numero_mesa, 
    u.nombre as mesero_nombre,
    c.nombre as cliente_nombre
FROM pedidos p
LEFT JOIN mesas m ON p.mesa_id = m.mesa_id
LEFT JOIN usuarios u ON p.usuario_id = u.usuario_id
LEFT JOIN clientes c ON p.cliente_id = c.cliente_id
WHERE p.pedido_id = %s;

SELECT d.*, pl.nombre as platillo_nombre
FROM detalles_pedido d
JOIN platillos pl ON d.platillo_id = pl.platillo_id
WHERE d.pedido_id = %s
ORDER BY d.detalle_id;

SELECT p.*, 
    m.numero_mesa, 
    u.nombre as mesero_nombre,
    c.nombre as cliente_nombre
FROM pedidos p
LEFT JOIN mesas m ON p.mesa_id = m.mesa_id
LEFT JOIN usuarios u ON p.usuario_id = u.usuario_id
LEFT JOIN clientes c ON p.cliente_id = c.cliente_id
ORDER BY p.fecha_hora DESC;

SELECT DISTINCT p.*, m.numero_mesa
FROM pedidos p
JOIN mesas m ON p.mesa_id = m.mesa_id
JOIN detalles_pedido d ON p.pedido_id = d.pedido_id
WHERE p.estado NOT IN ('cancelado', 'pagado')
AND d.estado IN ('pendiente', 'en preparacion')
ORDER BY p.fecha_hora ASC;

SELECT * FROM pedidos 
WHERE mesa_id = %s 
AND estado NOT IN ('pagado', 'cancelado')
ORDER BY fecha_hora DESC
LIMIT 1;

UPDATE pedidos SET estado = %s WHERE pedido_id = %s;

UPDATE detalles_pedido 
SET estado = %s, notas_chef = %s
WHERE detalle_id = %s;

UPDATE detalles_pedido 
SET estado = %s
WHERE detalle_id = %s;

SELECT COUNT(*) as pendientes
FROM detalles_pedido
WHERE pedido_id = (
    SELECT pedido_id FROM detalles_pedido WHERE detalle_id = %s
)
AND estado != 'listo';

UPDATE pedidos
SET estado = 'listo'
WHERE pedido_id = (
    SELECT pedido_id FROM detalles_pedido WHERE detalle_id = %s
);

SELECT 
    {group_by} as periodo,
    DATE_FORMAT(MIN(p.fecha_hora), '%Y-%m-%d') as periodo_formateado,
    COUNT(*) as total_pedidos,
    SUM(p.total) as total_ventas
FROM pedidos p
WHERE p.estado = 'pagado'
AND DATE(p.fecha_hora) BETWEEN %s AND %s
GROUP BY {group_by}
ORDER BY periodo;

SELECT SUM(total) as total
FROM pedidos
WHERE estado = 'pagado'
AND DATE(fecha_hora) BETWEEN %s AND %s;

SELECT COUNT(*) as total
FROM pedidos
WHERE DATE(fecha_hora) = %s;

SELECT SUM(total) as total
FROM pedidos
WHERE estado = 'pagado'
AND DATE(fecha_hora) = %s;

SELECT p.*, m.numero_mesa
FROM pedidos p
JOIN mesas m ON p.mesa_id = m.mesa_id
ORDER BY p.fecha_hora DESC
LIMIT %s;

-- Consultas para el modelo User
INSERT INTO usuarios (nombre, email, contraseña_hash, rol)
VALUES (%s, %s, %s, %s);

SELECT * FROM usuarios WHERE email = %s;

SELECT * FROM usuarios ORDER BY usuario_id ASC;

SELECT * FROM usuarios WHERE usuario_id = %s;

SELECT COUNT(*) as total FROM usuarios;

UPDATE usuarios 
SET nombre = %s, email = %s, rol = %s, activo = %s
WHERE usuario_id = %s;

-- Consultas para el modelo Inventario
INSERT INTO inventario (
    ingrediente_id, usuario_id, cantidad, tipo_movimiento,
    motivo, costo_total
) VALUES (
    %s, %s, %s, %s, %s, %s
);

UPDATE ingredientes 
SET stock_actual = stock_actual + %s
WHERE ingrediente_id = %s;

UPDATE ingredientes 
SET stock_actual = stock_actual - %s
WHERE ingrediente_id = %s;

SELECT iv.*, i.nombre as ingrediente_nombre,
       u.nombre as usuario_nombre
FROM inventario iv
JOIN ingredientes i ON iv.ingrediente_id = i.ingrediente_id
JOIN usuarios u ON iv.usuario_id = u.usuario_id
{WHERE clauses}
ORDER BY iv.fecha DESC;

SELECT iv.*, u.nombre as usuario_nombre
FROM inventario iv
JOIN usuarios u ON iv.usuario_id = u.usuario_id
WHERE iv.ingrediente_id = %s
ORDER BY iv.fecha DESC
LIMIT %s;

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
ORDER BY i.nombre;

-- Consultas para el modelo Categoria
INSERT INTO categorias (nombre, descripcion, orden_menu)
VALUES (%s, %s, %s);

SELECT * FROM categorias 
ORDER BY orden_menu IS NULL, orden_menu, nombre;

SELECT * FROM categorias WHERE categoria_id = %s;

UPDATE categorias 
SET nombre = %s, descripcion = %s, orden_menu = %s
WHERE categoria_id = %s;

SELECT COUNT(*) as total 
FROM platillos 
WHERE categoria_id = %s;

DELETE FROM categorias WHERE categoria_id = %s;

SELECT * FROM platillos 
WHERE categoria_id = %s AND activo = TRUE
ORDER BY nombre;

-- Consultas para el modelo Ingrediente
INSERT INTO ingredientes (
    nombre, unidad_medida, stock_actual, stock_minimo,
    proveedor_principal, costo_por_unidad, caduca, dias_caducidad
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s
);

SELECT * FROM ingredientes ORDER BY ingrediente_id ASC;

SELECT * FROM ingredientes WHERE ingrediente_id = %s;

UPDATE ingredientes SET {columna1} = %s, {columna2} = %s, ... WHERE ingrediente_id = %s;

SELECT * FROM ingredientes
WHERE stock_actual < stock_minimo
ORDER BY (stock_actual/stock_minimo) ASC;

SELECT i.*, pi.cantidad, pi.notas
FROM platillo_ingredientes pi
JOIN ingredientes i ON pi.ingrediente_id = i.ingrediente_id
WHERE pi.platillo_id = %s
ORDER BY i.nombre;

-- Consultas para el modelo Cliente
INSERT INTO clientes (nombre, telefono, email, preferencias)
VALUES (%s, %s, %s, %s);

SELECT * FROM clientes 
ORDER BY fecha_registro DESC;

SELECT * FROM clientes WHERE cliente_id = %s;

SELECT * FROM clientes 
WHERE nombre LIKE %s 
OR telefono LIKE %s 
OR email LIKE %s
ORDER BY nombre;

UPDATE clientes SET {columna1} = %s, {columna2} = %s, ... WHERE cliente_id = %s;

SELECT p.* 
FROM favoritos_clientes f
JOIN platillos p ON f.platillo_id = p.platillo_id
WHERE f.cliente_id = %s
AND p.activo = TRUE
ORDER BY p.nombre;

INSERT INTO favoritos_clientes (cliente_id, platillo_id)
VALUES (%s, %s);

DELETE FROM favoritos_clientes
WHERE cliente_id = %s AND platillo_id = %s;

-- Consultas para el modelo Mesa
INSERT INTO mesas (numero_mesa, capacidad, ubicacion, estado)
VALUES (%(numero_mesa)s, %(capacidad)s, %(ubicacion)s, 'disponible');

SELECT * FROM mesas WHERE mesa_id = %s;

SELECT * FROM mesas ORDER BY numero_mesa;

UPDATE mesas 
SET numero_mesa = %(numero_mesa)s, 
    capacidad = %(capacidad)s, 
    ubicacion = %(ubicacion)s
WHERE mesa_id = %(mesa_id)s;

UPDATE mesas SET estado = %s WHERE mesa_id = %s;

SELECT * FROM mesas WHERE estado = %s ORDER BY numero_mesa;

SELECT COUNT(*) as total FROM mesas WHERE estado = %s;

SELECT * FROM pedidos 
WHERE mesa_id = %s 
AND estado NOT IN ('pagado', 'cancelado')
ORDER BY fecha_hora DESC;

-- Consultas para el modelo DetallePedido
SELECT d.*, p.nombre as platillo_nombre
FROM detalles_pedido d
JOIN platillos p ON d.platillo_id = p.platillo_id
WHERE d.pedido_id = %s
ORDER BY d.detalle_id;

UPDATE detalles_pedido
SET estado = %s, notas_chef = %s
WHERE detalle_id = %s;

UPDATE detalles_pedido
SET estado = %s
WHERE detalle_id = %s;

SELECT d.*, p.nombre as platillo_nombre, 
       m.numero_mesa, pe.fecha_hora
FROM detalles_pedido d
JOIN platillos p ON d.platillo_id = p.platillo_id
JOIN pedidos pe ON d.pedido_id = pe.pedido_id
JOIN mesas m ON pe.mesa_id = m.mesa_id
WHERE d.estado IN ('pendiente', 'en preparacion')
ORDER BY pe.fecha_hora ASC, d.detalle_id ASC;

SELECT d.*, p.nombre as platillo_nombre,
       m.numero_mesa, pe.pedido_id
FROM detalles_pedido d
JOIN platillos p ON d.platillo_id = p.platillo_id
JOIN pedidos pe ON d.pedido_id = pe.pedido_id
JOIN mesas m ON pe.mesa_id = m.mesa_id
WHERE d.detalle_id = %s;