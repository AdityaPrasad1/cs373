-- ----------
-- Select.sql
-- ----------

-- https://www.w3schools.com/sql/sql_select.asp
-- https://www.w3schools.com/sql/sql_distinct.asp
-- https://www.w3schools.com/sql/sql_orderby.asp

use test;

select "*** show Student ***";
select * from Student;

select "*** show College ***";
select * from College;

select "*** show Apply ***";
select * from Apply;

-- relational algebra select
select "*** query #1 ***";
select *
    from Student
    where (GPA > 3.7);

-- relational algebra select
select "*** query #2 ***";
select *
    from Student
    where (GPA > 3.7) and (sizeHS < 1000);

-- relational algebra select
select "*** query #3 ***";
select *
    from Apply
    where (cName = 'Stanford') and (major = 'CS');

-- relational algebra project
select "*** query #4 ***";
select sID, decision
    from Apply;

-- relational algebra select and project
select "*** query #5 ***";
select sID, sName
    from Student
    where (GPA > 3.7);

-- relational algebra project, sort ascending, and limit
select "*** query #6 ***";
select major, decision
    from Apply
    order by major
    limit 6;

-- relational algebra project, uniquely, and sort descending
select "*** query #7 ***";
select distinct major, decision
    from Apply
    order by major desc;

exit
