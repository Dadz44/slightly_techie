CREATE TABLE product(
    id SERIAL NOT NULL PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price INT NOT NULL
);

INSERT INTO product(product_name, category, price)
VALUES
    ('Jasmine Rice', 'Grains', 120),
    ('Ceres', 'Fruit Juice', 45),
    ('Ideal Milk', 'Dairy', 200),
    ('Yam', 'Tuber', 35),
    ('Toilet Roll', 'Toiletries', 60);

CREATE TABLE sales(
    id SERIAL NOT NULL PRIMARY KEY,
    product_id VARCHAR(255),
    quantity_sold INT NOT NULL,
    sale_date DATE NOT NULL,
    total_price INT NOT NULL
);

INSERT INTO sales(product_id,quantity_sold, sale_date, total_price)
VALUES
    ('GR001',1000,'2025-03-06',34000),
    ('FJ002',500,'2025-03-06',25000),
    ('D001',1500,'2025-03-06',250000),
    ('T002',2000,'2025-03-06',70000),
    ('TT001',10000,'2025-03-06',50000);

SELECT * FROM product;

SELECT product_name,price FROM product;

SELECT * FROM sales LIMIT 2;

SELECT * FROM sales
WHERE total_price > 100;

SELECT DISTINCT category FROM product;

SELECT COUNT(product_name) FROM product;

SELECT * FROM sales;

SELECT SUM(total_price) FROM sales;

SELECT AVG(price) FROM product;