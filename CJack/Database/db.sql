drop database if exists cjack;
create database cjack;

use cjack;

create table users(
	id int primary key auto_increment,
    username varchar(30) not null unique,
    u_password varchar(30) not null,
    joined datetime default now()
);

create table user_data(
	user_id int,
    wins int default 0,
    losses int default 0,
    pushes int default 0
);
#insert into users (username, u_password) values("1", "1");
#insert into user_data (user_id) values (1);
