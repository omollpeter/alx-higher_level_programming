-- Creates a database and user 
-- Grants SELECT privilege on the database to user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
