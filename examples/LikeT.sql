-- ---------
-- LikeT.sql
-- ---------

use test;

/*
number of schools in California or Texas
MUST USE in
*/

select "query #1";
select count(cName)
    from College
    where state in ("CA", "TX");

/*
min, max, and average enrollment of
schools whose enrollment is between 20000 and 30000
MUST USE between
*/

select "query #2";
select min(enrollment), max(enrollment), avg(enrollment)
    from College
    where enrollment between 20000 and 30000;

/*
names and high school sizes of
students whose names end in "y"
*/

select "query #3";
select sName, sizeHS
    from Student
    where sName like "%y";

/*
min, max, and average high school size of
students whose names have three letters and end in "y"
*/

select "query #4";
select min(sizeHS), max(sizeHS), avg(sizeHS)
    from Student
    where sName like "__y";

/*
GPAs of students who applied in CS
sorted in descending order
MUST USE subquery
*/

select "query #5";
select GPA
    from Student
    where sID in
        (select sID
            from Apply
            where major = 'CS')
    order by GPA desc;

exit
