-- creates the table unique_id
-- description of table data: id INT with the default value 1, must be unique & name VARCHAR(256)
-- should not fail if exists

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
