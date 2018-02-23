#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# --------
# Range.py
# --------

# https://docs.python.org/3/library/functions.html#func-range

def test1 () :
    x = range(2, 2)
    a = []
    for v in x :
        a.append(v)
    assert a == []

def test2 () :
    x = range(2, 3)
    a = []
    for v in x :
        a.append(v)
    assert a == [2]

def test3 () :
    x = range(2, 4)
    a = []
    for v in x :
        a.append(v)
    assert a == [2, 3]

def test4 () :
    x = range(2, 5)
    assert x[0] == 2
    assert x[1] == 3
    assert x[2] == 4

def test5 () :
    x = range(2, 5)
    assert list(x) == [2, 3, 4]
    assert list(x) == [2, 3, 4]

def main () :
    for n in range(5) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("Range.py")
    main()
    print("Done.")
