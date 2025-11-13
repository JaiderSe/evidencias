use Restausync;

-- Insertar categorías
INSERT INTO categorias (nombre, descripcion, orden_menu) VALUES 
('Entradas', 'Aperitivos y entradas frías/calientes', 1),
('Platos Fuertes', 'Platos principales del menú', 2),
('Postres', 'Deliciosos postres caseros', 3),
('Bebidas', 'Refrescos, jugos y bebidas alcohólicas', 4);
USE Restausync;
 
-- Usuarios
INSERT INTO usuarios (nombre, email, contraseña_hash, rol) VALUES
('Ana Pérez', 'ana@restausync.com', 'hash1', 'administrador'),
('Luis Gómez', 'luis@restausync.com', 'hash2', 'chef'),
('Sofía Ramírez', 'sofia@restausync.com', 'hash3', 'mesero'),
('Carlos Méndez', 'carlos@restausync.com', 'hash4', 'inventario'),
('María López', 'maria@restausync.com', 'hash5', 'mesero'),
('Juan Torres', 'juan@restausync.com', 'hash6', 'chef'),
('Laura Niño', 'laura@restausync.com', 'hash7', 'inventario'),
('Pedro Rojas', 'pedro@restausync.com', 'hash8', 'administrador');

-- Insertar ingredientes
INSERT INTO ingredientes (nombre, unidad_medida, stock_actual, stock_minimo) VALUES
('Pechuga de pollo', 'kg', 15.0, 5.0),
('Arroz blanco', 'kg', 20.0, 8.0),
('Tomate', 'kg', 10.0, 3.0),
('Cebolla', 'kg', 8.0, 2.0);

-- Insertar platillo ejemplo
INSERT INTO platillos (nombre, categoria_id, descripcion, precio, tiempo_preparacion) VALUES
('Pollo a la Parrilla', 2, 'Pechuga de pollo marinada con hierbas y especias, asada a la parrilla', 18.99, 25);

-- Insertar receta (relación platillo-ingrediente)
INSERT INTO platillo_ingredientes (platillo_id, ingrediente_id, cantidad, notas) VALUES
(1, 1, 0.3, 'Marinado por 2 horas'),
(1, 2, 0.2, 'Arroz blanco al vapor'),
(1, 3, 0.1, 'En rodajas para acompañamiento'),
(1, 4, 0.05, 'Picada fina para marinado');