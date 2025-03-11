CREATE TABLE books(
	id SERIAL NOT NULL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	author VARCHAR(255) NOT NULL,
	year_pub INT NOT NULL
);

INSERT INTO books(title, author, year_pub)
VALUES
	('Home Going', 'Yaa Gyasi', 2016),
	('Deception Point','Dan Brown', 2002),
	('Over My Dead Body','Jeffrey Archer',2021),
	('No Longer At Ease','Chinua Achebe', 1960),
	('A Spell of Good Things', 'Ayobami Adebayo', 2023),
	('Stay With Me', 'Ayobami Adebayo', 2017),
	('The Bourne Identity', 'Robert Ludlum',1980),
	('The Bourne Supremacy', 'Robert Ludlum', 1986),
	('The Bourne Ultimatum', 'Robert Ludlum', 1990),
	('Americanah', 'Chimamanda Ngozi Adichie', 2013),
	('Dream Count','Chimamanda Ngozi Adichie', 2025),
	('The Pelican Brief', 'John Grisham', 1992),
	('The Rainmaker', 'John Grisham', 1995),
	('Harry Potter and the Prisoner of Azkaban','J. K. Rowling', 2002);

SELECT * FROM books;

SELECT * FROM books
WHERE author = 'John Grisham';

UPDATE books
SET year_pub = 2025
WHERE id = 1;

SELECT * FROM books;

DELETE FROM books
WHERE title = 'The Bourne Ultimatum';

SELECT * FROM books;

CREATE TABLE borrower(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	phone VARCHAR(255) NOT NULL,
	book_id INT,
	date_borrowed DATE,
	date_returned DATE,
	FOREIGN KEY (book_id) REFERENCES books(id)	
);

INSERT INTO borrower(name,phone,book_id,date_borrowed,date_returned)
VALUES
	('Kwame Appiah','0241234567',3,'2025-02-14',NULL),
	('Benedict Nuertey','0207778881',10, '2025-03-14',NULL),
	('Jeanette Marina Sallah','0245671111',11,'2025-03-10',NULL);

SELECT books.title,books.author, borrower.name,borrower.phone
FROM books
JOIN borrower ON books.id = borrower.book_id;