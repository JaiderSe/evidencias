-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS paises_iso3166_db;

-- Seleccionar la base de datos
USE paises_iso3166_db;

-- Tabla de Países
CREATE TABLE IF NOT EXISTS Paises (
    id_pais INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificador único para cada país',
    nombre VARCHAR(100) NOT NULL UNIQUE COMMENT 'Nombre oficial del país',
    iso_alpha_2 CHAR(2) NOT NULL UNIQUE COMMENT 'Código de país de dos letras según ISO 3166-1 alfa-2',
    iso_alpha_3 CHAR(3) NOT NULL UNIQUE COMMENT 'Código de país de tres letras según ISO 3166-1 alfa-3',
    iso_numerico INT NOT NULL UNIQUE COMMENT 'Código numérico de tres dígitos según ISO 3166-1 numérico',
    continente VARCHAR(50) NOT NULL COMMENT 'Continente al que pertenece el país'
);
