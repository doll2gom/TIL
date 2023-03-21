# 1
CREATE TABLE posts (
	postId INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postId)
);

# 2    
ALTER TABLE
	posts
ADD
	writer VARCHAR(100) NULL DEFAULT 'Anonymous',
ADD
	created_at datetime NULL DEFAULT CURRENT_TIMESTAMP;
    
# 3
ALTER TABLE
	posts
MODIFY
	content text NOT NULL;

SHOW COLUMNS FROM posts;

# 4
ALTER TABLE
	posts
DROP COLUMN
	writer;
    
# 5
DROP TABLE posts;

# 6
CREATE TABLE IF NOT EXISTS posts (
	postId INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content text NOT NULL,
	writer VARCHAR(20) NOT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (postId)
);

# 7
