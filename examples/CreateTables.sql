-- ----------------
-- CreateTables.sql
-- ----------------

use test;

select "*** drop table Student ***";
drop table if exists Student;

select "*** drop table Apply ***";
drop table if exists Apply;

select "*** drop table College ***";
drop table if exists College;

select "*** create table Student ***";
create table Student (
    sID    int,
    sName  text,
    GPA    float,
    sizeHS int);

select "*** create table Apply ***";
create table Apply (
    sID      int,
    cName    text,
    major    text,
    decision boolean);

select "*** create table College ***";
create table College (
    cName      text,
    state      char(2),
    enrollment int);

select "*** show tables ***";
show tables;

select "*** describe Student ***";
describe Student;

select "*** describe Apply ***";
describe Apply;

select "*** describe College ***";
describe College;

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
| sID    | int(11) | YES  |     | NULL    |       |
| sName  | text    | YES  |     | NULL    |       |
| GPA    | float   | YES  |     | NULL    |       |
| sizeHS | int(11) | YES  |     | NULL    |       |
+--------+---------+------+-----+---------+-------+



+------------------------+
| *** describe Apply *** |
+------------------------+
| *** describe Apply *** |
+------------------------+
+----------+------------+------+-----+---------+-------+
| Field    | Type       | Null | Key | Default | Extra |
+----------+------------+------+-----+---------+-------+
| sID      | int(11)    | YES  |     | NULL    |       |
| cName    | text       | YES  |     | NULL    |       |
| major    | text       | YES  |     | NULL    |       |
| decision | tinyint(1) | YES  |     | NULL    |       |
+----------+------------+------+-----+---------+-------+



+--------------------------+
| *** describe College *** |
+--------------------------+
| *** describe College *** |
+--------------------------+
+------------+---------+------+-----+---------+-------+
| Field      | Type    | Null | Key | Default | Extra |
+------------+---------+------+-----+---------+-------+
| cName      | text    | YES  |     | NULL    |       |
| state      | char(2) | YES  |     | NULL    |       |
| enrollment | int(11) | YES  |     | NULL    |       |
+------------+---------+------+-----+---------+-------+
*/
