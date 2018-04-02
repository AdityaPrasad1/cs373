-- -----------
-- SelectT.sql
-- -----------

use test;

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
