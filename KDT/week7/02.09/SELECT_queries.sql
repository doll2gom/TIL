SELECT 
	lastName
FROM 
	employees;
SELECT 
	lastName, firstName 
FROM 
	employees;
SELECT 
	*
FROM 
	employees;
SELECT 
	FirstName 이름
FROM 
	employees;
SELECT 
	FirstName As '이름'
FROM 
	employees;
SELECT 
	productCode, 
    quantityOrdered * priceEach as '주문총액'
FROM 
	orderdetails;
SELECT 
	firstName
FROM 
	employees
ORDER BY
	firstName ASC;
SELECT 
	firstName
FROM 
	employees
ORDER BY
	firstName DESC;
SELECT 
	lastName, firstName
FROM 
	employees
ORDER BY
	lastName DESC, firstName ASC;
SELECT 
	productCode, 
	quantityOrdered * priceEach as 		totalSales
FROM 
	orderdetails
ORDER BY
	totalSales DESC;