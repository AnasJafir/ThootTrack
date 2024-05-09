-- Create database
CREATE DATABASE IF NOT EXISTS ThootTrack;

-- Create user
CREATE USER IF NOT EXISTS 'Anas'@'localhost' IDENTIFIED BY 'alx0723';

GRANT ALL PRIVILEGES ON ThootTrack.* TO 'Anas'@'localhost';

GRANT SELECT ON performance_schema.* TO 'Anas'@'localhost';

FLUSH PRIVILEGES;