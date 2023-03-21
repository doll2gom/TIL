# 문제 1
-- 테이블 products 에서 평균 MSRP 보다 큰 product 의 productCode , productName , MSRP 를 조회하시오.
-- 단, MSRP 기준 오름차순으로 정렬하세요.
SELECT productCode , productName , MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products)
ORDER BY MSRP;

# 문제 2
-- 테이블 customers 에서 2003년 1월 6일과 2003년 3월 26일 사이에 주문(order)을 한 고객의 customerNumber, customerName 를 조회하시오.
-- 단, customerNumber 기준 오름차순으로 정렬하세요.
SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
    FROM orders
    WHERE orderDate < '2003-03-27')
ORDER BY customerNumber;

SELECT *
FROM orders
WHERE orderDate < '2003-03-27'
ORDER BY customerNumber;

SELECT * FROM products;

# 문제 3
-- productLine 가 Classic Cars 인 제품(product) 중 MSRP가 가장 큰 제품의 productCode , productName , productLine , MSRP 를 조회하시오.
-- 제품 데이터는 products 테이블을 활용합니다.
SELECT productCode , productName , productLine, MSRP
FROM products
WHERE 
	productLine = 'Classic Cars'
ORDER BY MSRP DESC
LIMIT 1;


# 문제 4
-- 가장 많은 고객(customer)이 사는 나라(country)의 customerNumber , customerName , country 를 조회하시오.
-- 고객 데이터는 customers 테이블을 활용합니다.
-- 단, customerNumber 기준 오름차순으로 정렬하세요.

-- 가장 많은 고객이 사는 나라 찾기
SELECT country , count(*) AS f1
FROM customers
GROUP BY country
ORDER BY f1 DESC
LIMIT 1;

SELECT customerNumber , customerName , country
FROM customers
WHERE country = 'USA'
ORDER BY customerNumber;

# 문제 5
-- 가장 많은 주문(order)을 한 고객(customer)의 customerNumber , customerName , 주문 수(order_count) 를 조회하시오.
-- 고객 데이터는 customers 테이블, 주문 테이블은 orders 테이블을 활용합니다.
SELECT * FROM customers;
SELECT * FROM orders;

-- 가장 많이 주문한 고객의 customerNumber와 order_count 구하기
SELECT customerNumber, COUNT(*) AS order_count 
FROM orders
GROUP BY customerNumber
ORDER BY order_count DESC
LIMIT 1;

SELECT customerNumber , customerName , order_count 
FROM (
	SELECT customerNumber , customerName, COUNT(*) AS order_count 
	FROM customers
	INNER JOIN  orders
		USING(customerNumber)
	GROUP BY customerNumber
	ORDER BY order_count DESC
	LIMIT 1
) AS newtable;


# 문제 6
-- 주문 날짜(orderDate)가 2004년인 주문(orderdetail) 제품(product)의 productCode , productName 를 조회하시오.
-- 주문 날짜 데이터는 orders 테이블, 주문 - 제품 데이터는 orderdetails 테이블, 제품 데이터는 products 테이블을 활용합니다.
SELECT * FROM orders;
SELECT * FROM orderdetails;
SELECT * FROM products;

SELECT productCode , productName
FROM products
WHERE productCode IN ( 
	SELECT productCode 
    FROM orders
	NATURAL JOIN orderdetails
    WHERE 
		orderDate > '2004-01-01'
		AND orderDate < '2004-12-31')
ORDER BY productCode DESC;
        
---------        

## 실습조원 답안6-1
SELECT productCode, productName
FROM products
WHERE
    productCode IN (
        SELECT productCode
        FROM orderdetails
        INNER JOIN orders USING (orderNumber)
        WHERE year(orderDate) = 2004
    )
ORDER BY
    productCode DESC
;
## 실습조원 답안6-2
SELECT productCode, productName
FROM products
WHERE EXISTS (
    SELECT *
    FROM orders
    WHERE orderDate LIKE '2004%')
ORDER BY
    productCode DESC;
