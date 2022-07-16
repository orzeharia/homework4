
create table users
(
    name     varchar(20) not null,
    id       int auto_increment
        primary key,
    email    varchar(50) not null,
    password varchar(20) not null
);

INSERT INTO db.users (name, id, email, password) VALUES ('galgal', 2, 'gal@gmail.com', '1111111');
INSERT INTO db.users (name, id, email, password) VALUES ('gadi', 4, 'gadi@gmail.com', '7878');
INSERT INTO db.users (name, id, email, password) VALUES ('ora', 6, 'ora@gmail.com', '14714');
