-- create db 'hbtn_0d_usa'
-- if db already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table 'states' in db 'hbtn_0d_usa'
-- id INT unique auto-generated not null and primary key
-- name VARCHAR(256) not null
-- if table already exists, script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
