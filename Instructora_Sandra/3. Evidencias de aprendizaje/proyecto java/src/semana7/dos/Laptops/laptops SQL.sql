-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS laptops_db;

-- Seleccionar la base de datos
USE laptops_db;

-- Tabla principal: Laptops
CREATE TABLE IF NOT EXISTS Laptops (
    nro_serie VARCHAR(50) PRIMARY KEY COMMENT 'Número de serie único de la laptop',
    modelo VARCHAR(100) NOT NULL COMMENT 'Modelo de la laptop',
    color VARCHAR(50) COMMENT 'Color de la laptop',
    anio INT COMMENT 'Año de fabricación',
    pantalla VARCHAR(50) COMMENT 'Características de la pantalla',
    antiguedad INT COMMENT 'Años desde la fabricación'
);

-- Tabla para el atributo multivaluado: Disco Duro
CREATE TABLE IF NOT EXISTS Disco_Duro (
    id_disco INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador del disco duro',
    nro_serie_laptop VARCHAR(50) NOT NULL COMMENT 'Referencia a la laptop',
    capacidad VARCHAR(50) NOT NULL COMMENT 'Capacidad del disco duro',
    tipo VARCHAR(50) NOT NULL COMMENT 'Tipo de disco (SSD, HDD, etc.)',
    FOREIGN KEY (nro_serie_laptop) REFERENCES Laptops(nro_serie) ON DELETE CASCADE
);

-- Tabla para el atributo compuesto: Método de Entrada
CREATE TABLE IF NOT EXISTS Metodo_Entrada (
    id_metodo INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador del método de entrada',
    nro_serie_laptop VARCHAR(50) NOT NULL COMMENT 'Referencia a la laptop',
    tipo ENUM('Trackpad', 'Teclado') NOT NULL COMMENT 'Tipo de método de entrada',
    FOREIGN KEY (nro_serie_laptop) REFERENCES Laptops(nro_serie) ON DELETE CASCADE
);
