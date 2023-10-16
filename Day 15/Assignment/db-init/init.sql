-- init.sql
CREATE TABLE my_data (
    id serial PRIMARY KEY,
    name VARCHAR (255),
    description TEXT
);

INSERT INTO my_data (name, description) VALUES ('Item 1', 'This is item 1');
INSERT INTO my_data (name, description) VALUES ('Item 2', 'This is item 2');

