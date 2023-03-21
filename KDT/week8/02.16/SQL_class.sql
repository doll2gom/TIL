# 서브쿼리 연습문제1
-- 테이블 확인
SELECT * FROM payments;

-- 한번 소비에 가장 많이 소비한 금액 확인
SELECT MAX(amount)
FROM payments;

-- WHERE 절로 찾은 최댓값을 활용하여 확인
SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);


# 서브쿼리 연습문제2
-- 테이블 확인
SELECT * FROM employees;
SELECT * FROM offices;
-- 미국 사무실에서 일하는 직원의 이름과 성 조회
-- 미국 사무실 코드를 가지고 있는 목록
-- 직원 테이블의 officecode가 1, 2, 3 인지 확인

SELECT officeCode
FROM offices
WHERE country = 'USA';

SELECT lastName, firstName
FROM employees
WHERE officeCode IN
	(
    SELECT officeCode
	FROM offices
	WHERE country = 'USA'
);


# 서브쿼리 연습문제3
-- 테이블 확인
SELECT * FROM customers;
SELECT * FROM orders;
-- orders에는 주문한 고객만 들어있음 -> NOT IN
-- orders에서 고객 주문 목록을 가져와서
-- customers의 모든 정보와 위에서 가져온 고객 주문 목록을 비교
-- 결국 위에서 가져온 고객 주문 목록에 포함되지 않는 고객이 범인

SELECT customerName 
FROM customers
WHERE customerNumber NOT IN 
	(SELECT customerNumber FROM orders);


## (심화) 서브쿼리 연습문제1
-- 테이블 확인
SELECT * FROM customers;
SELECT * FROM payments;

-- case 1 from으로부터 한번에 가져오는 방식
SELECT customerNumber, amount, contactFirstName 
FROM (
	SELECT * 
    FROM payments
	INNER JOIN customers USING (customerNumber)
) AS t1
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);

-- case 2 분할된 표현
SELECT L.customerNumber, L.amount, R.contactFirstName
FROM payments L
INNER JOIN customers R
	ON L.customerNumber = R.customerNumber
WHERE L.amount = (
	SELECT MAX(amount)
	FROM payments
);

-- case 3 교재
SELECT customerNumber, amount, contactFirstName 
FROM (
	SELECT t1.customerNumber, amount, contactFirstName 
	FROM payments t1
	INNER JOIN customers t2
		ON t1.customerNumber = t2.customerNumber
) result
WHERE 
	amount = (SELECT MAX(amount) FROM payments);
        

## EXISTS 연습문제 1
-- 테이블 확인
SELECT * FROM customers;
SELECT * FROM orders;

SELECT
	customerNumber, customerName
FROM
	customers
WHERE EXISTS (
	SELECT * 
    FROM orders
	WHERE customers.customerNumber = orders.customerNumber
);

## EXISTS 연습문제 2
-- 테이블 확인
SELECT * FROM employees;
SELECT * FROM offices;

SELECT
	employeeNumber, firstName, lastName
FROM
	employees
WHERE EXISTS (
	SELECT *
    FROM offices
	WHERE 
		city = 'paris'
		AND employees.officeCode = offices.officeCode
);


## CASE 연습문제 1
SELECT
	contactFirstName, creditLimit,
    (CASE
		WHEN creditLimit > 100000 THEN  'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
	END) AS grade
FROM
	customers;
    
## CASE 연습문제 2
SELECT
	orderNumber, status,
    (CASE
		WHEN status = 'In Process'THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
	END) AS grade
FROM
	orders;
