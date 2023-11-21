-- script that prepares a MySQL server for the project
-- creat database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a new user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
