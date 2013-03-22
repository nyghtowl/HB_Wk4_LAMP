CREATE TABLE Users (
id INT PRIMARY KEY,
email varchar(64),
password varchar(64),
fname varchar(64),
lname varchar(64)
);

CREATE TABLE Tasks (
id INT PRIMARY KEY,
title varchar(128),
created_at DATETIME,
due_date DATETIME,
completed_at DATETIME,
user_id INT
);
