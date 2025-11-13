-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS coleccion_musical;
USE coleccion_musical;

-- Tabla para almacenar los usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contrasena VARCHAR(100) NOT NULL
);

-- Tabla para almacenar los álbumes
CREATE TABLE IF NOT EXISTS albums (
    id_album INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    titulo VARCHAR(200) NOT NULL,
    ano_produccion YEAR NOT NULL,
    descripcion TEXT,
    medio VARCHAR(50) NOT NULL,  -- Puede ser disco, casete, CD, etc.
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabla para almacenar los artistas
CREATE TABLE IF NOT EXISTS artistas (
    id_artista INT AUTO_INCREMENT PRIMARY KEY,
    nombre_artista VARCHAR(100) NOT NULL
);

-- Tabla para almacenar la relación de los artistas con los álbumes
CREATE TABLE IF NOT EXISTS album_artistas (
    id_album INT,
    id_artista INT,
    PRIMARY KEY (id_album, id_artista),
    FOREIGN KEY (id_album) REFERENCES albums(id_album) ON DELETE CASCADE,
    FOREIGN KEY (id_artista) REFERENCES artistas(id_artista) ON DELETE CASCADE
);

-- Tabla para almacenar las canciones
CREATE TABLE IF NOT EXISTS canciones (
    id_cancion INT AUTO_INCREMENT PRIMARY KEY,
    id_album INT,
    titulo_cancion VARCHAR(200) NOT NULL,
    duracion INT NOT NULL,  -- Duración en segundos
    interprete VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_album) REFERENCES albums(id_album) ON DELETE CASCADE
);

-- Tabla para almacenar la relación de los usuarios con sus álbumes
CREATE TABLE IF NOT EXISTS usuario_album (
    id_usuario INT,
    id_album INT,
    PRIMARY KEY (id_usuario, id_album),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_album) REFERENCES albums(id_album) ON DELETE CASCADE
);
