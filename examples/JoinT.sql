-- ---------
-- JoinT.sql
-- ---------

use test;

/*
ID, name, and GPA of students who applied in CS
MUST USE subquery
*/

select "query #1";
select sID, sName, GPA
    from Student
    where sID in
        (select sID
            from Apply
            where major = 'CS');

/*
ID, name, and GPA of students who applied in CS
MUST USE inner join
*/

select "query #2";
select distinct sID, sName, GPA
    from Student
    inner join Apply using (sID)
    where major = 'CS';

/*
ID and name of students who have applied in CS but not in EE
*/

select "query #3";
select sID, sName
    from Student
    where
        sID     in (select sID from Apply where major = 'CS')
        and
        sID not in (select sID from Apply where major = 'EE');

exit
