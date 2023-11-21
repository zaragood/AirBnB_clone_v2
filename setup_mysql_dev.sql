-- script that prepares a MySQL server for the project
-- creats a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant privilleges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant SELECT privilage on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
