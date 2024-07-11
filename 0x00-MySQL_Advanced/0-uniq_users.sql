-- creates table
CREATE TABLE IF NOT EXISTS users (
    id int AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    PRIMARY KEY (id)
);
