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
    primary key (sID));

select "*** create table College ***";
create table College (
    cName       varchar(8) not null,
    state       char(2),
    enrollment  int,
    primary key (cName));

select "*** create table Apply ***";
create table Apply (
    sID         int,
    cName       varchar(8),
    major       text,
    decision    boolean,
    foreign key (sID)   references Student (sID),
    foreign key (cName) references College (cName));

select "*** show tables ***";
show tables;

select "*** describe Student ***";
describe Student;

select "*** describe College ***";
describe College;

select "*** describe Apply ***";
describe Apply;

exit

/*
mysql -uroot -t < CreateTables.sql
+----------------------------+
| *** drop table Student *** |
+----------------------------+
| *** drop table Student *** |
+----------------------------+



+--------------------------+
| *** drop table Apply *** |
+--------------------------+
| *** drop table Apply *** |
+--------------------------+



+----------------------------+
| *** drop table College *** |
+----------------------------+
| *** drop table College *** |
+----------------------------+



+------------------------------+
| *** create table Student *** |
+------------------------------+
| *** create table Student *** |
+------------------------------+



+----------------------------+
| *** create table Apply *** |
+----------------------------+
| *** create table Apply *** |
+----------------------------+



+------------------------------+
| *** create table College *** |
+------------------------------+
| *** create table College *** |
+------------------------------+



+---------------------+
| *** show tables *** |
+---------------------+
| *** show tables *** |
+---------------------+
+----------------+
| Tables_in_test |
+----------------+
| Apply          |
| College        |
| Student        |
+----------------+




+--------------------------+
| *** describe Student *** |
+--------------------------+
| *** describe Student *** |
+--------------------------+
+--------+---------+------+-----+---------+-------+
| Field  | Type    | Null | Key | Default | Extra |
+--------+---------+------+-----+---------+-------+
| sID    | int(11) | NO   | PRI | NULL    |       |
| sName  | text    | YES  |     | NULL    |       |
| GPA    | float   | YES  |     | NULL    |       |
| sizeHS | int(11) | YES  |     | NULL    |       |
+--------+---------+------+-----+---------+-------+



+--------------------------+
| *** describe College *** |
+--------------------------+
| *** describe College *** |
+--------------------------+
+------------+------------+------+-----+---------+-------+
| Field      | Type       | Null | Key | Default | Extra |
+------------+------------+------+-----+---------+-------+
| cName      | varchar(8) | NO   | PRI | NULL    |       |
| state      | char(2)    | YES  |     | NULL    |       |
| enrollment | int(11)    | YES  |     | NULL    |       |
+------------+------------+------+-----+---------+-------+



+------------------------+
| *** describe Apply *** |
+------------------------+
| *** describe Apply *** |
+------------------------+
+----------+------------+------+-----+---------+-------+
| Field    | Type       | Null | Key | Default | Extra |
+----------+------------+------+-----+---------+-------+
| sID      | int(11)    | YES  | MUL | NULL    |       |
| cName    | varchar(8) | YES  | MUL | NULL    |       |
| major    | text       | YES  |     | NULL    |       |
| decision | tinyint(1) | YES  |     | NULL    |       |
+----------+------------+------+-----+---------+-------+
*/
