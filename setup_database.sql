-- Create database
CREATE DATABASE IF NOT EXISTS ThootTrack;

-- Create user
CREATE USER IF NOT EXISTS 'username'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON ThootTrack.* TO 'username'@'localhost';

GRANT SELECT ON performance_schema.* TO 'username'@'localhost';

FLUSH PRIVILEGES;
