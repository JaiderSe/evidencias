CREATE DATABASE IF NOT EXISTS Restausync;
USE Restausync;

-- Tabla de Usuarios/Empleados
CREATE TABLE usuarios (
    usuario_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contraseña_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('administrador', 'chef', 'mesero', 'inventario')),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

-- Tabla de Categorías de Platillos
CREATE TABLE categorias (
    categoria_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    orden_menu INTEGER
);

-- Tabla de Ingredientes
CREATE TABLE ingredientes (
    ingrediente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    unidad_medida VARCHAR(20) NOT NULL,
    stock_actual DECIMAL(10,2) NOT NULL,
    stock_minimo DECIMAL(10,2) NOT NULL,
    proveedor_principal VARCHAR(100),
    costo_por_unidad DECIMAL(10,2),
    caduca BOOLEAN DEFAULT FALSE,
    dias_caducidad INTEGER
);

-- Tabla de Platillos
CREATE TABLE platillos (
    platillo_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria_id INTEGER REFERENCES categorias(categoria_id),
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    tiempo_preparacion INTEGER, -- en minutos
    activo BOOLEAN DEFAULT TRUE,
    es_vegano BOOLEAN DEFAULT FALSE,
    es_vegetariano BOOLEAN DEFAULT FALSE,
    tiene_gluten BOOLEAN DEFAULT TRUE,
    nivel_picante INTEGER CHECK (nivel_picante BETWEEN 0 AND 5) DEFAULT 0,
    imagen_url VARCHAR(255)
);

-- Tabla de relación Platillo-Ingrediente (Recetas)
CREATE TABLE platillo_ingredientes (
    platillo_id INTEGER REFERENCES platillos(platillo_id),
    ingrediente_id INTEGER REFERENCES ingredientes(ingrediente_id),
    cantidad DECIMAL(10,2) NOT NULL,
    notas TEXT, -- Ej: "picado fino", "al gusto", etc.
    PRIMARY KEY (platillo_id, ingrediente_id)
);

-- Tabla de Mesas
CREATE TABLE mesas (
    mesa_id SERIAL PRIMARY KEY,
    numero_mesa VARCHAR(10) UNIQUE NOT NULL,
    capacidad INTEGER NOT NULL,
    ubicacion VARCHAR(50),
    estado VARCHAR(20) DEFAULT 'disponible' CHECK (estado IN ('disponible', 'ocupada', 'reservada', 'mantenimiento'))
);

-- Tabla de Clientes (para historial)
CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100),
    preferencias TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Pedidos
CREATE TABLE pedidos (
    pedido_id SERIAL PRIMARY KEY,
    mesa_id INTEGER REFERENCES mesas(mesa_id),
    cliente_id INTEGER REFERENCES clientes(cliente_id),
    usuario_id INTEGER REFERENCES usuarios(usuario_id), -- Mesero que tomó el pedido
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) NOT NULL CHECK (estado IN ('recibido', 'en preparacion', 'listo', 'entregado', 'cancelado', 'pagado')),
    notas TEXT,
    total DECIMAL(10,2)
);

-- Tabla de Detalles de Pedido
CREATE TABLE detalles_pedido (
    detalle_id SERIAL PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedidos(pedido_id),
    platillo_id INTEGER REFERENCES platillos(platillo_id),
    cantidad INTEGER NOT NULL DEFAULT 1,
    precio_unitario DECIMAL(10,2) NOT NULL,
    personalizaciones TEXT, -- Ej: "sin cebolla", "bien cocido"
    estado VARCHAR(20) DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'en preparacion', 'listo', 'entregado')),
    notas_chef TEXT
);

-- Tabla de Inventario (Movimientos)
CREATE TABLE inventario (
    movimiento_id SERIAL PRIMARY KEY,
    ingrediente_id INTEGER REFERENCES ingredientes(ingrediente_id),
    usuario_id INTEGER REFERENCES usuarios(usuario_id),
    cantidad DECIMAL(10,2) NOT NULL,
    tipo_movimiento VARCHAR(10) CHECK (tipo_movimiento IN ('entrada', 'salida', 'ajuste')),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    motivo TEXT,
    costo_total DECIMAL(10,2)
);

-- Tabla de Favoritos de Clientes
CREATE TABLE favoritos_clientes (
    cliente_id INTEGER REFERENCES clientes(cliente_id),
    platillo_id INTEGER REFERENCES platillos(platillo_id),
    PRIMARY KEY (cliente_id, platillo_id)
);