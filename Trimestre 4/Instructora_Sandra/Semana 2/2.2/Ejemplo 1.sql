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
 
 -- DDL
 Create database EjemploMayoDB;
 show databases;
 
 USE EjemploMayoDB;
 
 CREATE TABLE Persona
 (
    id varchar(10),  
    nombre varchar(30),
    salario float 
 );
 
  CREATE TABLE Persona  ( id varchar(10),   nombre varchar(30), salario float  );
  
  show tables;
  
  describe persona;