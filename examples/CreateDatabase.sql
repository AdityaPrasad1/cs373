--  ------------------
--  CreateDatabase.sql
--  ------------------

select "*** drop database test ***";
drop database test;

select "*** create database test ***";
create database test;

select "*** show databases ***";
show databases;
exit

/*
mysql -uroot -t < CreateDatabase.sql
+----------------------------+
| *** drop database test *** |
+----------------------------+
| *** drop database test *** |
+----------------------------+



+------------------------------+
| *** create database test *** |
+------------------------------+
| *** create database test *** |
+------------------------------+



+------------------------+
| *** show databases *** |
+------------------------+
| *** show databases *** |
+------------------------+
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
*/
