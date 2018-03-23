# -----------
# Fri, 23 Mar
# -----------

"""
how could I best represent a relation (table) in Python?

movie table

title year director genre
"star wars" 1977 "george lucas" "sci-fi"
...

list of dicts
"""

def select (a: Iterable[Dict], up: Callable[[Dict], Bool]) :
    for i in a :
        if up(i) :
            yield i

    return (i for i in a if up(i))

    return filter(up, a)

def project (a: Iterable[Dict], *k: str) :
    for row in a :
        result_row = {}
        for col in k :
            if col in row :
                result_row[col] = row[col]
        yield result_row

    for row in a :
        yield {col: row[col] for col in k if col in row}

    return ({col: row[col] for col in k if col in row} for row in a)_
