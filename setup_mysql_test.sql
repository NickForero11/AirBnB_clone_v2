-- Create a testing database with an administrator user

-- Create hbnb_test database and admin user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the testing admin
GRANT ALL PRIVILEGES ON `hbnb_test_db` . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema` . * TO 'hbnb_test'@'localhost';
