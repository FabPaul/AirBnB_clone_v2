--Script that prepares a MySQL server for the given project--
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hdnd_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;