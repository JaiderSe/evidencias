-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS bogota_localidades_db;

-- Seleccionar la base de datos
USE bogota_localidades_db;

-- Tabla de Localidades
CREATE TABLE IF NOT EXISTS Localidades (
    id_localidad INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único de la localidad',
    nombre VARCHAR(100) NOT NULL UNIQUE COMMENT 'Nombre de la localidad',
    tipo VARCHAR(50) NOT NULL COMMENT 'Tipo de localidad (urbana o rural)',
    superficie DECIMAL(10,2) NOT NULL COMMENT 'Superficie en km²',
    poblacion_total INT NOT NULL COMMENT 'Población total de la localidad'
);

-- Tabla de Barrios
CREATE TABLE IF NOT EXISTS Barrios (
    id_barrio INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único del barrio',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombre del barrio',
    id_localidad INT NOT NULL COMMENT 'Clave foránea que referencia a la tabla Localidades',
    FOREIGN KEY (id_localidad) REFERENCES Localidades(id_localidad) ON DELETE CASCADE
);

-- Tabla de Población
CREATE TABLE IF NOT EXISTS Poblacion (
    id_poblacion INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único de la población registrada',
    id_localidad INT NOT NULL COMMENT 'Clave foránea que referencia a la tabla Localidades',
    anio INT NOT NULL COMMENT 'Año del registro poblacional',
    poblacion INT NOT NULL COMMENT 'Cantidad de habitantes en ese año',
    FOREIGN KEY (id_localidad) REFERENCES Localidades(id_localidad) ON DELETE CASCADE
);
