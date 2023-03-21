# 1
SELECT DISTINCT
	lastName
FROM
	employees
ORDER BY
	lastName;
    
# 2
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode = 1;

# 3    
SELECT
	lastName, firstName, jobTitle
FROM
	employees
WHERE
	jobtitle != 'Sales Rep';

# 4
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode >= 3 AND
	jobtitle = 'Sales Rep';
    
# 5
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode < 5
    OR jobtitle = 'Sales Rep';

# 6    
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode BETWEEN 1 AND 4;
-- 	officeCode >= 1 
--  AND <= 4;

# 7
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode IN (1,3,4);
-- 	officeCode = 1 
--     OR officeCode = 3 
--     OR officeCode = 4;

# 8
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode NOT IN (1,3,4);

# 9
SELECT
	lastName, firstName
FROM
	employees
WHERE
	lastName LIKE '%son';
    
# 10
SELECT
	lastName, firstName
FROM
	employees
WHERE
	firstName LIKE '___y';

# LIMIT 1
SELECT
	firstName, officeCode 
FROM
	employees
ORDER BY
	officeCode DESC 
LIMIT 3, 5;
-- LIMIT 5 OFFSET 3;

# GROUP 1
SELECT
	country, AVG(creditLimit) AS avgOfCreditLimit
FROM 
	customers
GROUP BY
	country
ORDER BY
	avgOfCreditLimit DESC;
    
# GROUP 2
SELECT
	country, AVG(creditLimit)
FROM 
	customers
-- WHERE
-- 	AVG(creditLimit) > 80000
GROUP BY
	country
HAVING
	AVG(creditLimit) > 80000;

	