-- --------
-- Like.sql
-- --------

-- https://www.w3schools.com/sql/sql_between.asp
-- https://www.w3schools.com/sql/sql_count_avg_sum.asp
-- https://www.w3schools.com/sql/sql_in.asp
-- https://www.w3schools.com/sql/sql_like.asp
-- https://www.w3schools.com/sql/sql_min_max.asp

use test;

select "*** show Student ***";
select * from Student;

select "*** show College ***";
select * from College;

select "*** show Apply ***";
select * from Apply;

-- students whose names end in "y"
select "*** query #1 ***";
select *
    from Student
    where sName like "%y";

-- students whose names have three letters and end in "y"
select "*** query #2 ***";
select *
    from Student
    where sName like "__y";

-- students whose names are "Amy" or "Jay" or "Mary"
select "*** query #3 ***";
select *
    from Student
    where sName = "Amy" or sName = "Jay" or sName = "Mary";

-- students whose names are "Amy" or "Jay" or "Mary"
select "*** query #4 ***";
select *
    from Student
    where sName in ("Amy", "Jay", "Mary");

-- colleges whose enrollment is between 20,000 and 30,000
select "*** query #5 ***";
select *
    from College
    where enrollment > 20000 and enrollment < 30000;

-- colleges whose enrollment is between 20,000 and 30,000
select "*** query #6 ***";
select *
    from College
    where enrollment between 20000 and 30000;

-- number of colleges
select "*** query #7 ***";
select count(cName)
    from College;

-- smallest enrollment of colleges
select "*** query #8 ***";
select min(enrollment)
    from College;

-- largest enrollment of colleges
select "*** query #9 ***";
select max(enrollment)
    from College;

-- average enrollment of colleges
select "*** query #10 ***";
select avg(enrollment)
    from College;

-- total enrollment of colleges
select "*** query #11 ***";
select sum(enrollment)
    from College;

exit
