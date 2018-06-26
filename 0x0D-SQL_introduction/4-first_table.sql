-- create table; shouldn't fail if already exists

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
