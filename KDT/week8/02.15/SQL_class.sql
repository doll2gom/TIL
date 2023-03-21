-- join
CREATE TABLE users(
	id INT AUTO_INCREMENT, 
	name VARCHAR(50) NOT NULL, 
    PRIMARY KEY (id)
);

DROP TABLE articles;
DROP TABLE users;

CREATE TABLE articles ( 
	id INT AUTO_INCREMENT, 
    title VARCHAR(50) NOT NULL, 
    content VARCHAR(100) NOT NULL, 
    userId INT NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO 
	users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');
    
INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1', '내용1', 1), 
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 4);

SELECT * FROM users;
SELECT * FROM articles;

SELECT articles.id title, content, name
FROM articles
INNER JOIN users
	ON articles.userId = users.id;

# 1
SELECT 
	productCode, 
    productName
FROM 
	products
INNER JOIN productlines
	ON products.productline = productlines.productline;

SELECT * FROM products;

SELECT productCode, productName
FROM products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;
    
    
# 2
SELECT 
	orders.orderNumber, status, priceEach
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;
    
# 3
SELECT 
	orders.orderNumber, 
    status, 
    SUM(priceEach * quantityOrdered) AS totalSales
FROM
	orders AS t1
INNER JOIN orderdetails AS t2
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY
	orderNumber;

# LEFT JOIN 1
SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber;
    
# LEFT JOIN 2
SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber IS NULL;
    
# RIGHT JOIN 1
SELECT employeeNumber, firstName, customerNumber, contactFirstName
FROM customers
RIGHT JOIN employees
	ON salesRepEmployeeNumber = employeeNumber;
-- WHERE orderNumber IS NULL;
    
    
    
    