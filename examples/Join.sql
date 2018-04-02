-- --------
-- Join.sql
-- --------

-- https://www.w3schools.com/sql/sql_join_inner.asp
-- https://www.w3schools.com/sql/sql_join.asp

use test;

select "*** show Student ***";
select * from Student;

select "*** show College ***";
select * from College;

select "*** show Apply ***";
select * from Apply;

-- relational algebra cross join
select "*** query #1 ***";
select *
    from Student
    cross join Apply
    order by Student.sID;

-- relational algebra theta join (with on)
select "*** query #2 ***";
select *
    from Student
    inner join Apply
    on Student.sID = Apply.sID;

-- relational algebra theta join (with using)
select "*** query #3 ***";
select *
    from Student
    inner join Apply using (sID);

-- relational algebra natural join
select "*** query #4 ***";
select *
    from Student
    natural join Apply;

-- relational algebra theta join and select
select "*** query #5 ***";
select *
    from Student
    inner join Apply using (sID)
    where (sizeHS   > 1000)   and
          (major    = 'CS')   and
          (decision = false);

-- relational algebra theta join and select and project
select "*** query #6 ***";
select sName, GPA
    from Student
    inner join Apply using (sID)
    where (sizeHS   > 1000)   and
          (major    = 'CS')   and
          (decision = false);

-- relational algebra theta join and select
select "*** query #7 ***";
select *
    from Student
        inner join Apply   using (sID)
        inner join College using (cName)
    where (sizeHS     > 500)   and
          (major      = 'CS')  and
          (decision   = true)  and
          (enrollment > 20000);

-- relational algebra theta join and select and project
select "*** query #8 ***";
select sName, GPA
    from Student
        inner join Apply   using (sID)
        inner join College using (cName)
    where (sizeHS     > 500)   and
          (major      = 'CS')  and
          (decision   = true)  and
          (enrollment > 20000);

-- relational algebra self join
select "*** query #9 ***";
select R.cName, R.state
    from College as R
    inner join College as S
    where (R.cName != S.cName) and
          (R.state  = S.state);

exit
