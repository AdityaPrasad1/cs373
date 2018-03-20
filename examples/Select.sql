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
select "*** select #1 ***";
select *
    from Student
    where (GPA > 3.7);

-- relational algebra select
select "*** select #2 ***";
select *
    from Student
    where (GPA > 3.7) and (sizeHS < 1000);

-- relational algebra select
select "*** select #3 ***";
select *
    from Apply
    where (cName = 'Stanford') and (major = 'CS');

-- relational algebra project
select "*** select #4 ***";
select sID, decision
    from Apply;

-- relational algebra select and project
select "*** select #5 ***";
select sID, sName
    from Student
    where (GPA > 3.7);

-- relational algebra project and sort ascending, and limit
select "*** select #6 ***";
select major, decision
    from Apply
    order by major
    limit 6;

-- relational algebra project, uniquely, sort descending
select "*** select #7 ***";
select distinct major, decision
    from Apply
    order by major desc;

exit

/*
mysql -t < Select.sql
+----------------------+
| *** show Student *** |
+----------------------+
| *** show Student *** |
+----------------------+
+-----+--------+------+--------+
| sID | sName  | GPA  | sizeHS |
+-----+--------+------+--------+
| 123 | Amy    |  3.9 |   1000 |
| 234 | Bob    |  3.6 |   1500 |
| 320 | Lori   | NULL |   2500 |
| 321 | Mary   |  2.5 |   1200 |
| 345 | Craig  |  3.5 |    500 |
| 432 | Kevin  | NULL |   1500 |
| 456 | Doris  |  3.9 |   1000 |
| 543 | Craig  |  3.4 |   2000 |
| 567 | Edward |  2.9 |   2000 |
| 654 | Amy    |  3.9 |   1000 |
| 678 | Fay    |  3.8 |    200 |
| 765 | Jay    |  2.9 |   1500 |
| 789 | Gary   |  3.4 |    800 |
| 876 | Irene  |  3.9 |    400 |
| 987 | Helen  |  3.7 |    800 |
+-----+--------+------+--------+



+----------------------+
| *** show College *** |
+----------------------+
| *** show College *** |
+----------------------+
+----------+-------+------------+
| cName    | state | enrollment |
+----------+-------+------------+
| Berkeley | CA    |      36000 |
| Cornell  | NY    |      21000 |
| Irene    | TX    |      25000 |
| MIT      | MA    |      10000 |
| Stanford | CA    |      15000 |
+----------+-------+------------+



+--------------------+
| *** show Apply *** |
+--------------------+
| *** show Apply *** |
+--------------------+
+------+----------+----------------+----------+
| sID  | cName    | major          | decision |
+------+----------+----------------+----------+
|  123 | Berkeley | CS             |        1 |
|  123 | Cornell  | EE             |        1 |
|  123 | Stanford | CS             |        1 |
|  123 | Stanford | EE             |        0 |
|  234 | Berkeley | biology        |        0 |
|  321 | MIT      | history        |        0 |
|  321 | MIT      | psychology     |        1 |
|  345 | Cornell  | bioengineering |        0 |
|  345 | Cornell  | CS             |        1 |
|  345 | Cornell  | EE             |        0 |
|  345 | MIT      | bioengineering |        1 |
|  543 | MIT      | CS             |        0 |
|  678 | Stanford | history        |        1 |
|  765 | Cornell  | history        |        0 |
|  765 | Cornell  | psychology     |        1 |
|  765 | Stanford | history        |        1 |
|  876 | MIT      | biology        |        1 |
|  876 | MIT      | marine biology |        0 |
|  876 | Stanford | CS             |        0 |
|  987 | Berkeley | CS             |        1 |
|  987 | Stanford | CS             |        1 |
+------+----------+----------------+----------+



+-------------------+
| *** select #1 *** |
+-------------------+
| *** select #1 *** |
+-------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 123 | Amy   |  3.9 |   1000 |
| 456 | Doris |  3.9 |   1000 |
| 654 | Amy   |  3.9 |   1000 |
| 678 | Fay   |  3.8 |    200 |
| 876 | Irene |  3.9 |    400 |
| 987 | Helen |  3.7 |    800 |
+-----+-------+------+--------+



+-------------------+
| *** select #2 *** |
+-------------------+
| *** select #2 *** |
+-------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 678 | Fay   |  3.8 |    200 |
| 876 | Irene |  3.9 |    400 |
| 987 | Helen |  3.7 |    800 |
+-----+-------+------+--------+



+-------------------+
| *** select #3 *** |
+-------------------+
| *** select #3 *** |
+-------------------+
+------+----------+-------+----------+
| sID  | cName    | major | decision |
+------+----------+-------+----------+
|  123 | Stanford | CS    |        1 |
|  876 | Stanford | CS    |        0 |
|  987 | Stanford | CS    |        1 |
+------+----------+-------+----------+



+-------------------+
| *** select #4 *** |
+-------------------+
| *** select #4 *** |
+-------------------+
+------+----------+
| sID  | decision |
+------+----------+
|  123 |        1 |
|  123 |        1 |
|  123 |        1 |
|  123 |        0 |
|  234 |        0 |
|  321 |        0 |
|  321 |        1 |
|  345 |        0 |
|  345 |        1 |
|  345 |        0 |
|  345 |        1 |
|  543 |        0 |
|  678 |        1 |
|  765 |        0 |
|  765 |        1 |
|  765 |        1 |
|  876 |        1 |
|  876 |        0 |
|  876 |        0 |
|  987 |        1 |
|  987 |        1 |
+------+----------+



+-------------------+
| *** select #5 *** |
+-------------------+
| *** select #5 *** |
+-------------------+
+-----+-------+
| sID | sName |
+-----+-------+
| 123 | Amy   |
| 456 | Doris |
| 654 | Amy   |
| 678 | Fay   |
| 876 | Irene |
| 987 | Helen |
+-----+-------+



+-------------------+
| *** select #6 *** |
+-------------------+
| *** select #6 *** |
+-------------------+
+----------------+----------+
| major          | decision |
+----------------+----------+
| bioengineering |        0 |
| bioengineering |        1 |
| biology        |        0 |
| biology        |        1 |
| CS             |        1 |
| CS             |        1 |
+----------------+----------+



+-------------------+
| *** select #7 *** |
+-------------------+
| *** select #7 *** |
+-------------------+
+----------------+----------+
| major          | decision |
+----------------+----------+
| psychology     |        1 |
| marine biology |        0 |
| history        |        0 |
| history        |        1 |
| EE             |        0 |
| EE             |        1 |
| CS             |        0 |
| CS             |        1 |
| biology        |        0 |
| biology        |        1 |
| bioengineering |        0 |
| bioengineering |        1 |
+----------------+----------+
*/
