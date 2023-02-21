DROP TABLE users;

SET autocommit = 0;

CREATE TABLE users ( 
	id INT AUTO_INCREMENT, 
    name VARCHAR (10) NOT NULL, 
    PRIMARY KEY (id)
);

START TRANSACTION;
INSERT INTO users(name)
VALUES ('harry'),('test');

SELECT * FROM users;

-- ROLLBACK;

COMMIT;

DROP TABLE articles;

CREATE TABLE articles(
	id INT AUTO_INCREMENT, 
    title VARCHAR (100) NOT NULL, 
    createdAt DATETIME NOT NULL, 
    updatedAt DATETIME NOT NULL, 
    PRIMARY KEY (id)
);
INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;

# 1
-- create trigger
DELIMITER //
CREATE TRIGGER myTrigger
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;

UPDATE articles
SET title =  'new title'
WHERE id = 1;

SELECT * FROM articles;

CREATE TABLE articleLogs (
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DROP TRIGGER recordLogs;

# 2 심화
DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articleLogs (description, createdAt)
    VALUES('글이 작성되었어요.', CURRENT_TIME());
END//
DELIMITER ;

심화
DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO articleLogs (description, createdAt)
    VALUES(CONCAT (NEW. id,'번 글이 작성되었습니다. '), CURRENT_TIME());
END//
DELIMITER ;

SHOW TRIGGERS;

INSERT INTO articles (title, createdAt, updatedAt)
VALUE('title2', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;
SELECT * FROM recordLogs;
SELECT * FROM articleLogs;
#3
-- create trigger
CREATE TABLE backupArticles (
	id INT AUTO_INCREMENT, 
    title VARCHAR(100) NOT NULL, 
    createdAt DATETIME NOT NULL, 
    updatedAt DATETIME NOT NULL, 
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backUpLogs
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
    INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES(OLD.title, OLD.createdAt, OLD.updatedAt);
END//
DELIMITER ;

