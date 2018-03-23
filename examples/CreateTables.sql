-- ----------------
-- CreateTables.sql
-- ----------------

-- https://www.w3schools.com/sql/sql_drop_table.asp
-- https://www.w3schools.com/sql/sql_create_table.asp
-- https://www.w3schools.com/sql/sql_primarykey.asp
-- https://www.w3schools.com/sql/sql_foreignkey.asp

use test;

select "*** drop table Apply ***";
drop table if exists Apply;

select "*** drop table College ***";
drop table if exists College;

select "*** drop table Student ***";
drop table if exists Student;

select "*** create table Student ***";
create table Student (
    sID         int not null,
    sName       text,
    GPA         float,
    sizeHS      int,
    primary key (sID))
    engine = innodb;

select "*** create table College ***";
create table College (
    cName       varchar(8) not null,
    state       char(2),
    enrollment  int,
    primary key (cName))
    engine = innodb;

select "*** create table Apply ***";
create table Apply (
    sID         int,
    cName       varchar(8),
    major       text,
    decision    boolean,
    foreign key (sID)   references Student (sID),
    foreign key (cName) references College (cName))
    engine = innodb;

select "*** show tables ***";
show tables;

select "*** describe Student ***";
describe Student;

select "*** describe College ***";
describe College;

select "*** describe Apply ***";
describe Apply;

exit
