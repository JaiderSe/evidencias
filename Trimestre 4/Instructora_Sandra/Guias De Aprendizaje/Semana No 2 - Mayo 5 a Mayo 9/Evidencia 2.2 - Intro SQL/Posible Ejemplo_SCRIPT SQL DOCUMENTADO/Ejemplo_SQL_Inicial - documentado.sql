-- ==========================================
-- Ejemplo: SCRIPT SQL DOCUMENTADO
-- ==========================================

-- ==========================================
-- SQL: Lenguajes claves (DDL y DML)
-- ==========================================

-- DDL
 -- CREATE
 -- ALTER	
 -- DROP
 -- TRUNCATE

-- DML
 -- Select
 -- Insert
 -- Delete
 -- Update
 
-- ==========================================
-- DDL (Data Definition Language)
-- ==========================================

 -- DDL: CREATE DATABASE - Crea una nueva base de datos
 CREATE DATABASE Ejemplo;
 
 -- Mostrar las bases de datos disponibles
 SHOW DATABASES;
 
 -- Establacer o Seleccionar la base de datos que se va a usar
 USE Ejemplo;
 
 -- DDL: CREATE TABLE - Crea una tabla llamada <<Persona>> con tres campos básicos
 CREATE TABLE Persona
 (
    id varchar(10),  
    nombre varchar(30),
    salario float 
 );
 
 /* Mejor opción:  versión mejorada de la tabla con id autoincremental
 CREATE TABLE Persona
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    salario FLOAT
);
*/

-- Mostrar las tablas creadas en la base de datos
SHOW TABLES;

-- Mostrar la estructura de la tabla <<Persona>>
DESCRIBE persona;

-- ==========================================
-- DML (Data Manipulation Language)
-- ==========================================

-- DML: Insert - Insertar registros de prueba en la tabla <<Persona>>
INSERT INTO Persona(id,nombre,salario)VALUES(1,'Pepe',1000);
INSERT INTO Persona(id,nombre,salario)VALUES(2,'María',2500);
 
-- DML (DQL - Data Query Language): imprimir todos los registros de la tabla
SELECT * FROM persona;

-- DDL: Drop -  Eliminar completamente la tabla <<Persona>>, por lo que cualquier consulta SELECT posterior generará error si no se crea de nuevo.
DROP TABLE Persona ;



 
 