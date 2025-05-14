-- Crear base de datos
CREATE DATABASE ;
USE TurismoRisaralda;

-- Tabla de municipios
CREATE TABLE Municipio (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de encargados de turismo
CREATE TABLE EncargadoTurismo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(20),
    cargo VARCHAR(100),
    municipio_id INT,
    FOREIGN KEY (municipio_id) REFERENCES Municipio(id)
);

-- Tabla de entidades turísticas
CREATE TABLE EntidadTuristica (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50), -- ejemplo: hotel, agencia, operador, etc.
    direccion VARCHAR(150),
    telefono VARCHAR(20),
    municipio_id INT,
    FOREIGN KEY (municipio_id) REFERENCES Municipio(id)
);

-- Insertar municipios
INSERT INTO Municipio (nombre) VALUES 
('Pereira'), ('Dosquebradas'), ('Santa Rosa de Cabal');

-- Insertar encargados de turismo
INSERT INTO EncargadoTurismo (nombre, correo, telefono, cargo, municipio_id) VALUES
('Laura Mejía', 'laura@turismo.gov.co', '3124567890', 'Coordinadora de Turismo', 1),
('Carlos Ruiz', 'carlos@turismo.gov.co', '3109876543', 'Promotor Turístico', 2);

-- Insertar entidades turísticas
INSERT INTO EntidadTuristica (nombre, tipo, direccion, telefono, municipio_id) VALUES
('Hotel Boutique Pereira', 'Hotel', 'Cra 10 #12-34', '6067891234', 1),
('Agencia Andes Tours', 'Agencia', 'Calle 5 #8-12', '6061234567', 3);

select*from Municipio;
select*from EncargadoTurismo where id=1;
select*from EntidadTuristica;

select*from 
