# 1
CREATE TABLE users (
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday date NOT NULL,
    city VARCHAR(100) NULL,
    country VARCHAR(100) NULL,
    email VARCHAR(100) NULL,
    created_at datetime NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);

SELECT * FROM users
ORDER BY created_at ASC;

DROP TABLE users;

# 2
INSERT INTO 
    users (first_name, last_name, birthday, city, country, email)
VALUES 
    ('Beemo', 'Jeong' , '1000-01-01', NULL , NULL , 'beemo@hphk.kr'), 
    ('Jieun', 'Lee' , '1993-05-16', 'Seoul', 'Korea', NULL), 
    ('Dami', 'Kim' , '1995-04-09', 'Seoul', 'Korea', NULL),
    ('Kwangsoo', 'Lee' , '1985-07-14', 'Seoul', 'Korea', NULL);
    
-- INSERT INTO users (first_name,last_name, birthday)
-- VALUE 
-- 	('Beemo','Jeong','1000-01-01'),
-- 	('Jieun','Lee','1993-05-16'),
-- 	('Dami','Kim','1995-04-09'),
-- 	('Kwangsoo','Lee','1985-07-14');
-- UPDATE users
-- SET
-- 	email = 'beemo@hphk.kr'
-- WHERE
-- userId = 1;

# 3
INSERT INTO 
    users (first_name, last_name, birthday, city, country, email)
VALUES 
    ('A', 'a' , '2010-01-01', NULL , NULL , NULL ), 
    ('B', 'b' , '2011-05-16', NULL , NULL , NULL ), 
    ('C', 'c' , '2012-04-09', NULL , NULL , NULL ), 
    ('D', 'd' , '2013-07-14', NULL , NULL , NULL );

# 4
UPDATE 
	users
SET 
	first_name = 'Kim',
    last_name = 'shinhye',
    birthday = '1996-07-11'
WHERE
	userId = 2;

# 5
UPDATE 
	users
SET 
	country = REPLACE (country, NULL, Korea);

# 6
DELETE FROM
    users
WHERE
    first_name = 'Beemo';

# 7
DELETE FROM
    users
WHERE
    first_name = 'Kwangsoo'
	AND last_name = 'Lee';
    
# 8
DELETE FROM
    users
ORDER BY
    TIME(created_at) DESC
LIMIT 1;