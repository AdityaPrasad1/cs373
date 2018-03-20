# -----------
# Mon, 19 Mar
# -----------

"""
relational algebra

algebras
    set of elements
    set of operations
    open/closed on those operations

integer arithmetic
    integers
    +, -, *, /, %
    on +: closed
    on *: closed
    on -: closed
    on %: closed
    on /: open

relational algebra
    relations (tables)
    select, project, many flavors of join
    always closed

movie table

title year director genre
"shane" 1953 "george stevens" "western"
"star wars" 1977 "george lucas" "western"

director table

id name
1 "george stevens"
2 "george lucas"

movie table

title year id genre
"shane" 1953 1 "western"
"star wars" 1977 2 "western"

SQL is a DECLARATIVE language
compare that to a PROCEDURAL language (Pyton, C, JavaScript, ...)

relational algebra
    select
        input
            table
            a predicate
        output
            table

    project
        input
            table
            set of attributes (col names)
        output
            table
"""
