-- -----------
-- SelectT.sql
-- -----------

use test;

drop table if exists Apply;
drop table if exists College;
drop table if exists Student;

create table Student (
    sID         int not null,
    sName       text,
    GPA         float,
    sizeHS      int,
    primary key (sID))
    engine = innodb;

create table College (
    cName       varchar(8) not null,
    state       char(2),
    enrollment  int,
    primary key (cName))
    engine = innodb;

create table Apply (
    sID         int,
    cName       varchar(8),
    major       text,
    decision    boolean,
    foreign key (sID)   references Student (sID),
    foreign key (cName) references College (cName))
    engine = innodb;

insert into Student values (123, 'Amy',    3.9,  1000);
insert into Student values (234, 'Bob',    3.6,  1500);
insert into Student values (320, 'Lori',   null, 2500);
insert into Student values (321, 'Mary',   2.5,  1200);
insert into Student values (345, 'Craig',  3.5,   500);
insert into Student values (432, 'Kevin',  null, 1500);
insert into Student values (456, 'Doris',  3.9,  1000);
insert into Student values (543, 'Craig',  3.4,  2000);
insert into Student values (567, 'Edward', 2.9,  2000);
insert into Student values (654, 'Amy',    3.9,  1000);
insert into Student values (678, 'Fay',    3.8,   200);
insert into Student values (765, 'Jay',    2.9,  1500);
insert into Student values (789, 'Gary',   3.4,   800);
insert into Student values (876, 'Irene',  3.9,   400);
insert into Student values (987, 'Helen',  3.7,   800);

insert into College values ('Berkeley', 'CA', 36000);
insert into College values ('Cornell',  'NY', 21000);
insert into College values ('Irene',    'TX', 25000);
insert into College values ('MIT',      'MA', 10000);
insert into College values ('Stanford', 'CA', 15000);

insert into Apply values (123, 'Berkeley', 'CS',             true);
insert into Apply values (123, 'Cornell',  'EE',             true);
insert into Apply values (123, 'Stanford', 'CS',             true);
insert into Apply values (123, 'Stanford', 'EE',             false);
insert into Apply values (234, 'Berkeley', 'biology',        false);
insert into Apply values (321, 'MIT',      'history',        false);
insert into Apply values (321, 'MIT',      'psychology',     true);
insert into Apply values (345, 'Cornell',  'bioengineering', false);
insert into Apply values (345, 'Cornell',  'CS',             true);
insert into Apply values (345, 'Cornell',  'EE',             false);
insert into Apply values (345, 'MIT',      'bioengineering', true);
insert into Apply values (543, 'MIT',      'CS',             false);
insert into Apply values (678, 'Stanford', 'history',        true);
insert into Apply values (765, 'Cornell',  'history',        false);
insert into Apply values (765, 'Cornell',  'psychology',     true);
insert into Apply values (765, 'Stanford', 'history',        true);
insert into Apply values (876, 'MIT',      'biology',        true);
insert into Apply values (876, 'MIT',      'marine biology', false);
insert into Apply values (876, 'Stanford', 'CS',             false);
insert into Apply values (987, 'Berkeley', 'CS',             true);
insert into Apply values (987, 'Stanford', 'CS',             true);

/*
school names and decisions of
applications to CS that were accepted
sorted by school in ascending order
*/

select "query #1";
select cName, decision
    from Apply
    where major = "CS" and decision = true
    order by cName;

/*
distinct school names and decisions of
applications to CS that were accepted
sorted by school in descending order
limited to two results
*/

select "query #2";
select distinct cName, decision
    from Apply
    where major = "CS" and decision = true
    order by cName desc
    limit 2;

exit