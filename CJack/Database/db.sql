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
    chips int default 1000,
    wins int default 0,
    losses int default 0,
    chips_won int default 0,
    chips_lost int default 0
);
insert into users (username, u_password) values("morty", "pw")
