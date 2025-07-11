CREATE DATABASE Biblioteca;
use Biblioteca;

create table libros(
codigo int auto_increment,
titulo varchar(40),
autor varchar(30),
editorial varchar(20),
precio decimal (5,2),
stock int,
primary key (codigo)
);                         

insert into libros(titulo,autor,editorial,precio,stock) 
  values('Alicia en el pais de las maravillas','Lewis Carroll','Emece',20.00, 9);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('Alicia en el pais de las maravillas','Lewis Carroll','Plaza',35.00, 50);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('Aprenda PHP','Mario Molina','Siglo XXI',40.00, 3);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('El aleph','Borges','Emece',10.00, 18);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('Ilusiones','Richard Bach','Planeta',15.00, 22);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('Java en 10 minutos','Mario Molina','Siglo XXI',50.00, 7);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('Martin Fierro','Jose Hernandez','Planeta',20.00, 3);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('Martin Fierro','Jose Hernandez','Emece',30.00, 70);
 insert into libros(titulo,autor,editorial,precio,stock)
  values('Uno','Richard Bach','Planeta',10.00, 120);
  
  
  DELIMITER //
	CREATE PROCEDURE Libros_limite_stock()
	BEGIN 
		SELECT * FROM libros
		WHERE stock <= 10;
	END//
  DELIMITER ;
  
  CALL libros_limite_stock();
  /************************************************/
  
   DELIMITER //
  CREATE PROCEDURE Libros_autor_editorial(
  IN p_autor varchar(30),
  IN p_editorial varchar (20))
	BEGIN 
		SELECT titulo,precio FROM libros
		WHERE autor = p_autor AND editorial= p_editorial;
	END//
  DELIMITER ;
  
  CALL Libros_autor_editorial('Richard Bach' ,'Planeta');
  CALL Libros_autor_editorial('Borges' ,'Emece');
  
  /************************************************/
   DELIMITER //
  CREATE PROCEDURE autor_sumaypromedio(
  IN p_autor varchar(30),
  OUT Suma decimal(6,2),
  OUT Promedio decimal(6,2))
	BEGIN 
		SELECT titulo, editorial, precio FROM libros
		WHERE autor = p_autor;
        
        SELECT	sum(precio) INTO Suma FROM libros
        WHERE autor = p_autor;
        
        SELECT avg(precio) INTO Promedio FROM libros
        WHERE autor = p_autor;
	END//
  DELIMITER ;  
  
  CALL autor_sumaypromedio('Richard Bach',@s, @p);
  
  SELECT @s, @p;