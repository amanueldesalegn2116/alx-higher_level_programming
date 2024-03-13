-- create table 'force_name'
-- id INT, name VARCHAR(256) can't be null
-- if table already exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
