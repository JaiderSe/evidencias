-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS ciudades_colombia_db;

-- Seleccionar la base de datos
USE ciudades_colombia_db;

-- Desactivar temporalmente las restricciones de clave foránea
SET FOREIGN_KEY_CHECKS = 0;

-- Tabla de Departamentos
CREATE TABLE IF NOT EXISTS Departamentos (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único para cada departamento',
    nombre VARCHAR(100) NOT NULL UNIQUE COMMENT 'Nombre del departamento',
    region VARCHAR(100) NOT NULL COMMENT 'Región a la que pertenece el departamento'
);

-- Tabla de Ciudades
CREATE TABLE IF NOT EXISTS Ciudades (
    id_ciudad INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único para cada ciudad',
    nombre VARCHAR(100) NOT NULL COMMENT 'Nombre de la ciudad',
    id_departamento INT NOT NULL COMMENT 'Clave foránea que referencia a la tabla Departamentos',
    poblacion INT NOT NULL COMMENT 'Población de la ciudad',
    superficie DECIMAL(10,2) NOT NULL COMMENT 'Superficie en kilómetros cuadrados',
    altitud INT NOT NULL COMMENT 'Altitud sobre el nivel del mar en metros',
    FOREIGN KEY (id_departamento) REFERENCES Departamentos(id_departamento)
);

-- Tabla de Indicadores Socioeconómicos
CREATE TABLE IF NOT EXISTS Indicadores_Socioeconomicos (
    id_indicador INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único del indicador',
    id_ciudad INT NOT NULL COMMENT 'Clave foránea que referencia a la tabla Ciudades',
    pib_per_capita DECIMAL(12,2) COMMENT 'Producto Interno Bruto per cápita en la ciudad',
    tasa_desempleo DECIMAL(5,2) COMMENT 'Porcentaje de desempleo en la ciudad',
    indice_pobreza DECIMAL(5,2) COMMENT 'Índice de pobreza de la ciudad',
    FOREIGN KEY (id_ciudad) REFERENCES Ciudades(id_ciudad)
);

-- Tabla de Cultura y Turismo
CREATE TABLE IF NOT EXISTS Cultura_Turismo (
    id_cultura INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único del registro cultural',
    id_ciudad INT NOT NULL COMMENT 'Clave foránea que referencia a la tabla Ciudades',
    patrimonio_cultural TEXT COMMENT 'Información sobre el patrimonio cultural de la ciudad',
    festividades TEXT COMMENT 'Festividades destacadas de la ciudad',
    sitios_turisticos TEXT COMMENT 'Lugares turísticos importantes de la ciudad',
    FOREIGN KEY (id_ciudad) REFERENCES Ciudades(id_ciudad)
);

-- Reactivar las restricciones de clave foránea
SET FOREIGN_KEY_CHECKS = 1;