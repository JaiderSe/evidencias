create database SENA;
use SENA;
CREATE TABLE centros_formacion_sena (
    id SERIAL PRIMARY KEY,
    centro_formacion TEXT,
    codigo_centro INTEGER,
    latitud DOUBLE PRECISION,
    longitud DOUBLE PRECISION,
    nombre_regional TEXT,
    codigo_regional TEXT,
    nombre_departamento TEXT,
    codigo_departamento INTEGER,
    nombre_municipio TEXT,
    codigo_municipio INTEGER
);

