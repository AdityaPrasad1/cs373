# -----------
# Mon,  2 Apr
# -----------

"""
relational algebra
    select  table, unary predicate
    project table, attributes...

    join
        cross join table1, table2
            let's pretend that there are 10 students and 15 applications
            150 rows in result

        theta join table1, table2, predicate
            SQL's inner join with either ON or USING
            ON    allows different  field names
            USING requires the same filed name

        natural join table1, table2

        self join table
"""
