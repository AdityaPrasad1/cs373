-- ----------
-- Insert.sql
-- ----------

use test;

select "*** insert Student ***";
insert into Student values (123, 'Amy',    3.9,  1000);
insert into Student values (234, 'Bob',    3.6,  1500);
insert into Student values (320, 'Lori',   null, 2500);
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

select "*** insert Apply ***";
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
insert into Apply values (543, 'MIT',       'CS',            false);
insert into Apply values (678, 'Stanford', 'history',        true);
insert into Apply values (765, 'Cornell',  'history',        false);
insert into Apply values (765, 'Cornell',  'psychology',     true);
insert into Apply values (765, 'Stanford', 'history',        true);
insert into Apply values (876, 'MIT',      'biology',        true);
insert into Apply values (876, 'MIT',      'marine biology', false);
insert into Apply values (876, 'Stanford', 'CS',             false);
insert into Apply values (987, 'Berkeley', 'CS',             true);
insert into Apply values (987, 'Stanford', 'CS',             true);

select "*** insert College ***";
insert into College values ('Berkeley', 'CA', 36000);
insert into College values ('Cornell',  'NY', 21000);
insert into College values ('Irene',    'TX', 25000);
insert into College values ('MIT',      'MA', 10000);
insert into College values ('Stanford', 'CA', 15000);

select "*** show Student ***";
select * from Student;

select "*** show Apply ***";
select * from Apply;

select "*** show College ***";
select * from College;

exit

/*
mysql -uroot -t < Insert.sql
+------------------------+
| *** insert Student *** |
+------------------------+
| *** insert Student *** |
+------------------------+



+----------------------+
| *** insert Apply *** |
+----------------------+
| *** insert Apply *** |
+----------------------+



+------------------------+
| *** insert College *** |
+------------------------+
| *** insert College *** |
+------------------------+



+----------------------+
| *** show Student *** |
+----------------------+
| *** show Student *** |
+----------------------+
+------+--------+------+--------+
| sID  | sName  | GPA  | sizeHS |
+------+--------+------+--------+
|  123 | Amy    |  3.9 |   1000 |
|  234 | Bob    |  3.6 |   1500 |
|  320 | Lori   | NULL |   2500 |
|  345 | Craig  |  3.5 |    500 |
|  432 | Kevin  | NULL |   1500 |
|  456 | Doris  |  3.9 |   1000 |
|  543 | Craig  |  3.4 |   2000 |
|  567 | Edward |  2.9 |   2000 |
|  654 | Amy    |  3.9 |   1000 |
|  678 | Fay    |  3.8 |    200 |
|  765 | Jay    |  2.9 |   1500 |
|  789 | Gary   |  3.4 |    800 |
|  876 | Irene  |  3.9 |    400 |
|  987 | Helen  |  3.7 |    800 |
|  123 | Amy    |  3.9 |   1000 |
|  234 | Bob    |  3.6 |   1500 |
|  320 | Lori   | NULL |   2500 |
|  345 | Craig  |  3.5 |    500 |
|  432 | Kevin  | NULL |   1500 |
|  456 | Doris  |  3.9 |   1000 |
|  543 | Craig  |  3.4 |   2000 |
|  567 | Edward |  2.9 |   2000 |
|  654 | Amy    |  3.9 |   1000 |
|  678 | Fay    |  3.8 |    200 |
|  765 | Jay    |  2.9 |   1500 |
|  789 | Gary   |  3.4 |    800 |
|  876 | Irene  |  3.9 |    400 |
|  987 | Helen  |  3.7 |    800 |
+------+--------+------+--------+



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
| Berkeley | CA    |      36000 |
| Cornell  | NY    |      21000 |
| Irene    | TX    |      25000 |
| MIT      | MA    |      10000 |
| Stanford | CA    |      15000 |
+----------+-------+------------+
*/
