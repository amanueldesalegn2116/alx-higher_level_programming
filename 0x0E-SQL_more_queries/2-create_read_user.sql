-- create database 'hbtn_0d_2'
-- if db already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user 'user_0d_2'
-- user password should be set to 'user_0d_2_pwd'
-- if user already exists, script should not fail
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- user 'user_0d_2' should have only SELECT privilege in db 'hbtn_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
