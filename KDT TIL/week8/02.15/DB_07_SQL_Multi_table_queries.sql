# 1
-- 테이블 employees 과 테이블 offices 를 officeCode 기준으로 INNER JOIN 한 데이터를 조회하시오.
-- employeeNumber, lastName, firstName, city 필드만 조회하시오.
-- employeeNumber 기준 오름차순으로 정렬하세요.
SELECT 
	employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;
    
# 2
-- 테이블 customers 와 테이블 offices 를 city 기준으로 LEFT JOIN 한 데이터를 조회하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT 
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
# 3
-- 테이블 customers 와 테이블 offices 를 city 기준으로 RIGHT JOIN 한 데이터를 조회하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT 
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
# 4
-- 테이블 customers 와 테이블 offices 를 city 기준으로 INNER JOIN 한 데이터를 조회하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT 
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
# 5
-- 문제2, 문제3, 문제4 의 조회 결과가 다른 이유를 작성하시오.
# A와 B 두 테이블 속에 겹치는 A.c, B.c 필드가 각각 있을 때(A는 왼쪽, B는 오른쪽)

# 문제 4 INNER는 
-- A테이블을 기준으로 A.c필드와 B.c필드 동시에 들어있는 레코드만을 추출해 낸다. 
-- (B 테이블에서 A.c와 겹치지 않는 레코드 모두 제외)
-- A.c에는 있지만, B.c에는 없는 레코드 정보는 NULL로 가져온다.
-- A.c에 1개 있지만, B.c에 여러개인 경우, A.c필드의 레코드 정보를 여러개 표시하면서 B.c를 가져온다.

# 문제 2 LEFT는 
-- A테이블 전체를 항상 우선 가져오고,
-- INNER와 같이 A테이블을 기준으로 A.c필드와 B.c의 겹치는 정보를 가져온다.

# 문제 3 RIGHT는 A테이블을 기준
-- B테이블 전체를 항상 우선 가져오고,
-- INNER와 같이 A테이블을 기준으로 A.c필드와 B.c의 겹치는 정보를 가져온다.
-- 주의할 점은, INNER와 동일하게 A테이블을 기준으로 해야 한다.

# 6
-- 테이블 customers 와 테이블 offices 를 city 기준으로 FULL OUTER JOIN 한 데이터를 조회하시오.
-- MySQL에서 FULL OUTER JOIN 은 지원하지 않는 기능이므로 MySQL FULL OUTER JOIN 키워드를 검색하여 구현하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT 
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
UNION
SELECT 
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
# 7
-- 테이블 orderdetails 와 테이블 orders 를 INNER JOIN 한 데이터를 조회하시오.
-- orderNumber , orderDate 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.
SELECT 
	orderdetails.orderNumber,
    orderDate
FROM orderdetails
INNER JOIN orders
 ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;
    
# 7-2
SELECT 
	orderNumber,
    orderDate
FROM orderdetails
NATURAL JOIN orders
ORDER BY
	orderNumber;


# 8 
-- 테이블 orderdetails 와 테이블 products 을 INNER JOIN 한 데이터를 조회하시오.
-- orderNumber , productCode , productName 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.
SELECT 
	orderNumber, 
    orderdetails.productCode,
    productName
FROM 
	orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;

# 9
-- 테이블 orderdetails , 테이블 orders , 테이블 products 를 INNER JOIN 한 데이터를 조회하시오.
-- orderNumber , productCode , orderDate, productName 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.    
SELECT 
	orderNumber, 
    orderdetails.productCode,
    orderDate,
    productName
FROM orderdetails
NATURAL JOIN orders
NATURAL JOIN products
ORDER BY
	orderNumber;

# 테이블 3개 JOIN
SELECT *
FROM table1
INNER JOIN table2
ON table1.id = table2.id
INNER JOIN table3
ON table2.id = table3.id;
