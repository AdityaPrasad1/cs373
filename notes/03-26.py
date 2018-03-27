# -----------
# Mon, 26 Mar
# -----------

# Java

Mammal x = new Tiger(...); # ok

Tiger x = new Mammal(...); # not ok

# SQL

select distinct cName, decision
from Apply
where major = 'CS' and decision = true
order by cName desc
limit 2;
