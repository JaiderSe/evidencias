-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS especialidades_db;

-- Seleccionar la base de datos
USE especialidades_db;

-- Tabla de Categorías (Nivel 1)
CREATE TABLE IF NOT EXISTS Categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único de la categoría',
    nombre VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nombre de la categoría principal'
);

-- Tabla de Subcategorías (Nivel 2)
CREATE TABLE IF NOT EXISTS Subcategorias (
    id_subcategoria INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único de la subcategoría',
    nombre VARCHAR(255) NOT NULL COMMENT 'Nombre de la subcategoría',
    id_categoria INT NOT NULL COMMENT 'Clave foránea que referencia a la tabla Categorias',
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria) ON DELETE CASCADE
);

-- Tabla de Sub-subcategorías (Nivel 3)
CREATE TABLE IF NOT EXISTS SubSubcategorias (
    id_subsubcategoria INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único de la sub-subcategoría',
    nombre VARCHAR(255) NOT NULL COMMENT 'Nombre de la sub-subcategoría',
    id_subcategoria INT NOT NULL COMMENT 'Clave foránea que referencia a la tabla Subcategorias',
    FOREIGN KEY (id_subcategoria) REFERENCES Subcategorias(id_subcategoria) ON DELETE CASCADE
);
