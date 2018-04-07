-- ---------
-- Joins.sql
-- ---------

use test;

-- -----------------------------------------------------------------------
drop table if exists R;
drop table if exists S;

-- -----------------------------------------------------------------------
create table R (A int);
create table S (B int, C int);

-- -----------------------------------------------------------------------
insert into R values (1);
insert into R values (2);
insert into R values (3);

insert into S values (1, 6);
insert into S values (1, 7);
insert into S values (4, 8);
insert into S values (4, 9);

-- -----------------------------------------------------------------------
select "*** query #1a ***";

select * from R;
select * from S;

select count(*) from R cross join S;
select       *  from R cross join S;

-- -----------------------------------------------------------------------
select "*** query #1b ***";

select * from R;
select * from S;

select count(*) from R inner join S on R.A = S.B;
select       *  from R inner join S on R.A = S.B;

-- -----------------------------------------------------------------------
select "*** query #1c ***";

select * from R;
select * from S;

select count(*) from R left join S on R.A = S.B;
select       *  from R left join S on R.A = S.B;

-- -----------------------------------------------------------------------
select "*** query #1d ***";

select * from R;
select * from S;

select count(*) from R right join S on R.A = S.B;
select       *  from R right join S on R.A = S.B;

-- -----------------------------------------------------------------------
select "*** query #1e ***";

select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

-- -----------------------------------------------------------------------
drop table if exists R;
drop table if exists S;

-- -----------------------------------------------------------------------
create table R (A int);
create table S (A int, C int);

-- -----------------------------------------------------------------------
insert into R values (1);
insert into R values (2);
insert into R values (3);

insert into S values (6, 1);
insert into S values (7, 2);
insert into S values (8, 3);
insert into S values (9, 4);

-- -----------------------------------------------------------------------
select "*** query #2a ***";

select * from R;
select * from S;

select count(*) from R cross join S;
select       *  from R cross join S;

-- -----------------------------------------------------------------------
select "*** query #2b ***";

select * from R;
select * from S;

select count(*) from R inner join S using (A);
select       *  from R inner join S using (A);

-- -----------------------------------------------------------------------
select "*** query #2c ***";

select * from R;
select * from S;

select count(*) from R left join S using (A);
select       *  from R left join S using (A);

-- -----------------------------------------------------------------------
select "*** query #2d ***";

select * from R;
select * from S;

select count(*) from R right join S using (A);
select       *  from R right join S using (A);

-- -----------------------------------------------------------------------
select "*** query #2e ***";

select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

-- -----------------------------------------------------------------------
drop table if exists R;
drop table if exists S;

-- -----------------------------------------------------------------------
create table R (A int);
create table S (A int, C int);

-- -----------------------------------------------------------------------
insert into R values (1);
insert into R values (2);
insert into R values (3);

insert into S values (1, 6);
insert into S values (1, 7);
insert into S values (4, 8);
insert into S values (4, 9);

-- -----------------------------------------------------------------------
select "*** query #3a ***";

select * from R;
select * from S;

select count(*) from R cross join S;
select       *  from R cross join S;

-- -----------------------------------------------------------------------
select "*** query #3b ***";

select * from R;
select * from S;

select count(*) from R inner join S using (A);
select       *  from R inner join S using (A);

-- -----------------------------------------------------------------------
select "*** query #3c ***";

select * from R;
select * from S;

select count(*) from R left join S using (A);
select       *  from R left join S using (A);

-- -----------------------------------------------------------------------
select "*** query #3d ***";

select * from R;
select * from S;

select count(*) from R right join S using (A);
select       *  from R right join S using (A);

-- -----------------------------------------------------------------------
select "*** query #3e ***";

select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

-- -----------------------------------------------------------------------
drop table if exists R;
drop table if exists S;

-- -----------------------------------------------------------------------
create table R (A int, B int);
create table S (A int, C int, D int);

-- -----------------------------------------------------------------------
insert into R values (1, 4);
insert into R values (2, 5);
insert into R values (3, 6);

insert into S values (1, 3, 4);
insert into S values (1, 4, 5);
insert into S values (1, 4, 6);
insert into S values (2, 4, 7);
insert into S values (2, 5, 8);
insert into S values (4, 7, 9);

-- -----------------------------------------------------------------------
select "*** query #4a ***";

select * from R;
select * from S;

select count(*) from R cross join S;
select       *  from R cross join S;

-- -----------------------------------------------------------------------
select "*** query #4b ***";

select * from R;
select * from S;

select count(*) from R inner join S on R.A = S.A;
select       *  from R inner join S on R.A = S.A;

-- -----------------------------------------------------------------------
select "*** query #4c ***";

select * from R;
select * from S;

select count(*) from R left join S on R.A = S.A;
select       *  from R left join S on R.A = S.A;

-- -----------------------------------------------------------------------
select "*** query #4d ***";

select * from R;
select * from S;

select count(*) from R right join S on R.A = S.A;
select       *  from R right join S on R.A = S.A;

-- -----------------------------------------------------------------------
select "*** query #4e ***";

select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

-- -----------------------------------------------------------------------
drop table if exists R;
drop table if exists S;
drop table if exists T;

-- -----------------------------------------------------------------------
create table T (A int);

-- -----------------------------------------------------------------------
insert into T values (1);
insert into T values (2);
insert into T values (3);

-- -----------------------------------------------------------------------
select "*** query #5a ***";

select * from T;

select count(*) from T as R cross join T as S;
select       *  from T as R cross join T as S;

-- -----------------------------------------------------------------------
select "*** query #5b ***";

select * from T;

select count(*) from T as R inner join T as S using (A);
select       *  from T as R inner join T as S using (A);

-- -----------------------------------------------------------------------
select "*** query #5c ***";

select * from T;

select count(*) from T as R left join T as S using (A);
select       *  from T as R left join T as S using (A);

-- -----------------------------------------------------------------------
select "*** query #5d ***";

select * from T;

select count(*) from T as R right join T as S using (A);
select       *  from T as R right join T as S using (A);

-- -----------------------------------------------------------------------
select "*** query #5e ***";

select * from T;

select count(*) from T as R natural join T as S;
select       *  from T as R natural join T as S;

-- -----------------------------------------------------------------------
drop table if exists T;

exit
