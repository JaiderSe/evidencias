SELECT c.first_name, c.last_name, a.address FROM customer c INNER JOIN address a ON c.address_id = a.address_id;
SELECT c1.city AS ciudad1, c2.city AS ciudad2, co.country FROM city c1 JOIN city c2 ON c1.country_id = c2.country_id AND c1.city_id < c2.city_id JOIN country co ON c1.country_id = co.country_id;
SELECT first_name, last_name FROM actor UNION SELECT first_name, last_name FROM staff;

SELECT c.first_name, r.rental_date FROM customer c LEFT JOIN rental r ON c.customer_id = r.customer_id;
SELECT f.title, c.name AS categoria FROM film f LEFT JOIN film_category fc ON f.film_id = fc.film_id LEFT JOIN category c ON fc.category_id = c.category_id;

SELECT f.title, c.name AS categoria FROM film f RIGHT JOIN film_category fc ON f.film_id = fc.film_id RIGHT JOIN category c ON fc.category_id = c.category_id;
SELECT c.first_name, a.address FROM customer c RIGHT JOIN address a ON c.address_id = a.address_id;

SELECT l.name AS idioma, c.name AS categoria FROM language l CROSS JOIN category c LIMIT 10;
SELECT a.first_name, f.title FROM actor a CROSS JOIN film f LIMIT 10;

SELECT first_name, last_name, (SELECT COUNT(*) FROM actor) AS total_actores FROM actor LIMIT 5;
SELECT a.first_name, a.last_name, (SELECT COUNT(*) FROM film_actor fa WHERE fa.actor_id = a.actor_id) AS total_peliculas FROM actor a LIMIT 5;

SELECT *FROM ( SELECT title, release_year FROM film WHERE release_year >= 2005 ) AS peliculas_recientes;
SELECT avg_length.promedio FROM (SELECT AVG(length) AS promedio FROM film) AS avg_length;

SELECT first_name, last_name FROM customer WHERE customer_id IN (SELECT customer_id FROM rental);
SELECT title, length FROM film WHERE length > (SELECT AVG(length) FROM film);

show tables;
SELECT COUNT(*) AS total_ciudades FROM city;
SELECT COUNT(*) AS total_paises FROM country;
SELECT c.first_name, c.last_name, c.email, a.address, a.phone FROM customer c JOIN address a ON c.address_id = a.address_id;
SELECT SUM(amount) AS total_pagado FROM payment;
SELECT CONCAT(first_name, ' ', last_name) AS nombre_completo FROM customer;
SELECT MAX(amount) AS pago_maximo FROM payment;
SELECT ROUND(AVG(amount), 2) AS promedio_pago FROM payment;
SELECT title, rental_duration FROM film WHERE rental_duration BETWEEN 3 AND 5;
SELECT COUNT(*) AS peliculas_adultos FROM film WHERE rating IN ('R', 'NC-17');
SELECT DISTINCT f.title, f.rating FROM film f JOIN inventory i ON f.film_id = i.film_id WHERE f.rating IN ('R', 'NC-17');
SELECT FORMAT(AVG(rental_rate), 2) AS promedio_renta_infantil FROM film WHERE rating like 'G';
SELECT title, special_features FROM film WHERE special_features LIKE '%Behind the Scenes%';
SELECT title, special_features FROM film WHERE find_in_set('Behind the Scenes',special_features)>0;
SELECT title, special_features FROM film WHERE find_in_set('Deleted Scenes',special_features)>0;
SELECT count(*) FROM film WHERE find_in_set('Deleted Scenes',special_features)>0;
SELECT count(*) FROM film WHERE special_features LIKE '%Deleted Scenes%';
SELECT title FROM film WHERE title LIKE 'K%';
SELECT title FROM film WHERE title LIKE '%a';
SELECT city FROM city WHERE city like '%r%';
SELECT city FROM city WHERE city like '__o%';
SELECT city FROM city WHERE city like 'P_____';
SELECT city FROM city WHERE city like 'A%' and length(city)>3;

SELECT ci.city AS ciudad, COUNT(c.customer_id) AS total_clientes
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
GROUP BY ci.city
ORDER BY total_clientes DESC;

